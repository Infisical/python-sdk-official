import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from infisical_sdk.api_types import (
    BaseSecret,
    ListSecretsResponse,
    SingleSecretResponse,
)
from infisical_sdk.infisical_requests import InfisicalRequests
from infisical_sdk.util import SecretsCache

CACHE_KEY_LIST_SECRETS = "cache-list-secrets"
CACHE_KEY_SINGLE_SECRET = "cache-single-secret"


class V3RawSecrets:
    def __init__(self, requests: InfisicalRequests, cache: SecretsCache) -> None:
        self.requests = requests
        self.cache = cache

    def list_secrets(
        self,
        environment_slug: str,
        secret_path: str,
        project_id: str = None,
        expand_secret_references: bool = True,
        view_secret_value: bool = True,
        recursive: bool = False,
        include_imports: bool = True,
        tag_filters: List[str] = [],
        project_slug: str = None,
        sync_env_vars: bool = False,
        env_path: str = ".env",
    ) -> ListSecretsResponse:

        params = {
            "workspaceId": project_id,
            "environment": environment_slug,
            "secretPath": secret_path,
            "viewSecretValue": str(view_secret_value).lower(),
            "expandSecretReferences": str(expand_secret_references).lower(),
            "recursive": str(recursive).lower(),
            "include_imports": str(include_imports).lower(),
            "workspaceSlug": project_slug,
        }

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        if tag_filters:
            params["tagSlugs"] = ",".join(tag_filters)

        cache_key = self.cache.compute_cache_key(CACHE_KEY_LIST_SECRETS, **params)
        if self.cache.enabled:
            cached_response = self.cache.get(cache_key)

            if cached_response is not None and isinstance(
                cached_response, ListSecretsResponse
            ):
                return cached_response

        result = self.requests.get(
            path="/api/v3/secrets/raw", params=params, model=ListSecretsResponse
        )
        if sync_env_vars:
            self._perform_sync_and_report(result.data, env_path)

        if self.cache.enabled:
            self.cache.set(cache_key, result.data)

        return result.data

    def _perform_sync_and_report(self, result: ListSecretsResponse, env_path: str):
        report_path = ".infisical-sync-report.txt"
        self._ensure_ignored(report_path)

        # 1. Setup Data
        timestamp = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        added_count = 0
        updated_count = 0
        change_logs = []

        # 2. Read the entire .env file (if exists) to maintain order and comments
        file_lines = []
        if os.path.exists(env_path):
            with open(env_path, "r") as f:
                file_lines = f.readlines()

        # Create a mapping of key to line index for quick updates
        env_map = {}
        for idx, line in enumerate(file_lines):
            clean_line = line.strip()
            if "=" in clean_line and not clean_line.startswith("#"):
                k, v = clean_line.split("=", 1)
                env_map[k.strip()] = {"index": idx, "value": v.strip()}

        added_count = 0
        updated_count = 0
        new_entries = []

        # 3. Process API Secrets
        for secret in result.secrets:
            key = secret.secretKey
            api_val = secret.secretValue

            if key in env_map:
                # Check for conflict
                if env_map[key]["value"] != api_val:
                    old_val = env_map[key]["value"]
                    # Update the line in the original file list
                    line_index = env_map[key]["index"]
                    file_lines[line_index] = f"{key}={api_val}\n"

                    change_logs.append(
                        f"  [UPDATED] {key.ljust(20)} : '{old_val}' -> '{api_val}'"
                    )
                    updated_count += 1
            else:
                # Key doesn't exist, prepare to append
                new_entries.append(f"{key}={api_val}\n")
                change_logs.append(f"  [ADDED]   {key}")
                added_count += 1

        # 4. Write back to .env
        # Combine existing (potentially modified) lines with brand new entries
        with open(env_path, "w") as f:
            f.writelines(file_lines)
            if new_entries:
                if file_lines and not file_lines[-1].endswith("\n"):
                    f.write("\n")
                f.writelines(new_entries)

        # 5. Finalize and Write Report
        report_block = [
            "\n" + "═" * 60 + "\n",
            f" 📅 SYNC DATE: {timestamp}\n",
            f" 📁 TARGET:    {env_path}\n",
            f" 📥 FETCHED:   {len(result.secrets)} secrets\n",
            "─" * 60 + "\n",
        ]

        if not change_logs:
            report_block.append("  ✨ No changes detected. Local file is up to date.\n")
        else:
            report_block.extend([line + "\n" for line in change_logs])

        report_block.extend([
            "─" * 60 + "\n",
            f" ✅ SUMMARY:   {added_count} added | {updated_count} updated\n",
            "═" * 60 + "\n",
        ])

        with open(report_path, "a") as f:
            f.writelines(report_block)

    def _ensure_ignored(self, filename: str):
        """Adds the filename to .gitignore if not already present."""

        gitignore_path = ".gitignore"
        if not os.path.exists(gitignore_path):
            with open(gitignore_path, "w") as f:
                f.write(f"{filename}\n")
            return

        with open(gitignore_path, "r") as f:
            lines = f.readlines()

        if not any(filename in line for line in lines):
            with open(gitignore_path, "a") as f:
                f.write(f"\n\n# Infisical temporary sync reports\n{filename}\n")

    def get_secret_by_name(
        self,
        secret_name: str,
        environment_slug: str,
        secret_path: str,
        project_id: str = None,
        project_slug: str = None,
        expand_secret_references: bool = True,
        include_imports: bool = True,
        view_secret_value: bool = True,
        version: str = None,
    ) -> BaseSecret:

        params = {
            "workspaceId": project_id,
            "workspaceSlug": project_slug,
            "viewSecretValue": str(view_secret_value).lower(),
            "environment": environment_slug,
            "secretPath": secret_path,
            "expandSecretReferences": str(expand_secret_references).lower(),
            "include_imports": str(include_imports).lower(),
            "version": version,
        }

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        cache_params = {
            "project_id": project_id,
            "environment_slug": environment_slug,
            "secret_path": secret_path,
            "secret_name": secret_name,
        }

        cache_key = self.cache.compute_cache_key(
            CACHE_KEY_SINGLE_SECRET, **cache_params
        )

        if self.cache.enabled:
            cached_response = self.cache.get(cache_key)

            if cached_response is not None and isinstance(cached_response, BaseSecret):
                return cached_response

        result = self.requests.get(
            path=f"/api/v3/secrets/raw/{secret_name}",
            params=params,
            model=SingleSecretResponse,
        )

        if self.cache.enabled:
            self.cache.set(cache_key, result.data.secret)

        return result.data.secret

    def create_secret_by_name(
        self,
        secret_name: str,
        secret_path: str,
        environment_slug: str,
        project_id: str = None,
        secret_value: str = None,
        secret_comment: str = None,
        skip_multiline_encoding: bool = False,
        secret_reminder_repeat_days: Union[float, int] = None,
        secret_reminder_note: str = None,
        project_slug: str = None,
        secret_metadata: Optional[List[Dict[str, Any]]] = None,
        tags_ids: Optional[List[str]] = None,
    ) -> BaseSecret:

        requestBody = {
            "workspaceId": project_id,
            "projectSlug": project_slug,
            "environment": environment_slug,
            "secretPath": secret_path,
            "secretValue": secret_value,
            "secretComment": secret_comment,
            "tagIds": tags_ids,
            "skipMultilineEncoding": skip_multiline_encoding,
            "type": "shared",
            "secretReminderRepeatDays": secret_reminder_repeat_days,
            "secretReminderNote": secret_reminder_note,
            "secretMetadata": secret_metadata,
        }

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        result = self.requests.post(
            path=f"/api/v3/secrets/raw/{secret_name}",
            json=requestBody,
            model=SingleSecretResponse,
        )

        if self.cache.enabled:
            cache_params = {
                "project_id": project_id,
                "environment_slug": environment_slug,
                "secret_path": secret_path,
                "secret_name": secret_name,
            }

            cache_key = self.cache.compute_cache_key(
                CACHE_KEY_SINGLE_SECRET, **cache_params
            )
            self.cache.set(cache_key, result.data.secret)

            # Invalidates all list secret cache
            self.cache.invalidate_operation(CACHE_KEY_LIST_SECRETS)

        return result.data.secret

    def update_secret_by_name(
        self,
        current_secret_name: str,
        secret_path: str,
        environment_slug: str,
        project_id: str = None,
        secret_value: str = None,
        secret_comment: str = None,
        skip_multiline_encoding: bool = False,
        secret_reminder_repeat_days: Union[float, int] = None,
        secret_reminder_note: str = None,
        new_secret_name: str = None,
        project_slug: str = None,
        secret_metadata: Optional[List[Dict[str, Any]]] = None,
        tags_ids: Optional[List[str]] = None,
    ) -> BaseSecret:

        requestBody = {
            "workspaceId": project_id,
            "projectSlug": project_slug,
            "environment": environment_slug,
            "secretPath": secret_path,
            "secretValue": secret_value,
            "secretComment": secret_comment,
            "newSecretName": new_secret_name,
            "tagIds": tags_ids,
            "skipMultilineEncoding": skip_multiline_encoding,
            "type": "shared",
            "secretReminderRepeatDays": secret_reminder_repeat_days,
            "secretReminderNote": secret_reminder_note,
            "secretMetadata": secret_metadata,
        }

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        result = self.requests.patch(
            path=f"/api/v3/secrets/raw/{current_secret_name}",
            json=requestBody,
            model=SingleSecretResponse,
        )

        if self.cache.enabled:
            cache_params = {
                "project_id": project_id,
                "environment_slug": environment_slug,
                "secret_path": secret_path,
                "secret_name": current_secret_name,
            }

            cache_key = self.cache.compute_cache_key(
                CACHE_KEY_SINGLE_SECRET, **cache_params
            )
            self.cache.unset(cache_key)

            # Invalidates all list secret cache
            self.cache.invalidate_operation(CACHE_KEY_LIST_SECRETS)

        return result.data.secret

    def delete_secret_by_name(
        self,
        secret_name: str,
        secret_path: str,
        environment_slug: str,
        project_id: str = None,
        project_slug: str = None,
    ) -> BaseSecret:

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        requestBody = {
            "workspaceId": project_id,
            "projectSlug": project_slug,
            "environment": environment_slug,
            "secretPath": secret_path,
            "type": "shared",
        }

        result = self.requests.delete(
            path=f"/api/v3/secrets/raw/{secret_name}",
            json=requestBody,
            model=SingleSecretResponse,
        )

        if self.cache.enabled:
            cache_params = {
                "project_id": project_id,
                "environment_slug": environment_slug,
                "secret_path": secret_path,
                "secret_name": secret_name,
            }

            cache_key = self.cache.compute_cache_key(
                CACHE_KEY_SINGLE_SECRET, **cache_params
            )
            self.cache.unset(cache_key)

            # Invalidates all list secret cache
            self.cache.invalidate_operation(CACHE_KEY_LIST_SECRETS)

        return result.data.secret
