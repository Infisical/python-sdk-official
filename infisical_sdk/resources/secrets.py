from typing import List, Union, Optional, Dict, Any

from infisical_sdk.infisical_requests import InfisicalRequests
from infisical_sdk.api_types import ListSecretsResponse, SingleSecretResponse, BaseSecret
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
            project_slug: str = None) -> ListSecretsResponse:

        params = {
            "workspaceId": project_id,
            "environment": environment_slug,
            "secretPath": secret_path,
            "viewSecretValue": str(view_secret_value).lower(),
            "expandSecretReferences": str(expand_secret_references).lower(),
            "recursive": str(recursive).lower(),
            "include_imports": str(include_imports).lower(),
            "workspaceSlug": project_slug
        }

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        if tag_filters:
            params["tagSlugs"] = ",".join(tag_filters)

        
        cache_key = self.cache.compute_cache_key(CACHE_KEY_LIST_SECRETS, **params)
        if self.cache.enabled:
          cached_response = self.cache.get(cache_key)

          if cached_response is not None and isinstance(cached_response, ListSecretsResponse):
            return cached_response

        result = self.requests.get(
            path="/api/v3/secrets/raw",
            params=params,
            model=ListSecretsResponse
        )

        if self.cache.enabled:
          self.cache.set(cache_key, result.data)

        return result.data

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
            version: str = None) -> BaseSecret:

        params = {
          "workspaceId": project_id,
          "workspaceSlug": project_slug,
          "viewSecretValue": str(view_secret_value).lower(),
          "environment": environment_slug,
          "secretPath": secret_path,
          "expandSecretReferences": str(expand_secret_references).lower(),
          "include_imports": str(include_imports).lower(),
          "version": version
        }

        if project_slug is None and project_id is None:
            raise ValueError("project_slug or project_id must be provided")

        # Key on every request parameter, like list_secrets: secrets of other
        # projects (by slug), other versions or masked values must not be shared.
        cache_key = self.cache.compute_cache_key(
            CACHE_KEY_SINGLE_SECRET, secret_name=secret_name, **params
        )

        if self.cache.enabled:
          cached_response = self.cache.get(cache_key)

          if cached_response is not None and isinstance(cached_response, BaseSecret):
            return cached_response

        result = self.requests.get(
            path=f"/api/v3/secrets/raw/{secret_name}",
            params=params,
            model=SingleSecretResponse
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
            model=SingleSecretResponse
        )


        if self.cache.enabled:
          # The secret may be cached under any project reference (id or slug) and
          # read options, so drop every cached single secret and list
          self.cache.invalidate_operation(CACHE_KEY_SINGLE_SECRET)
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
            model=SingleSecretResponse
        )

        if self.cache.enabled:
          # The secret may be cached under any project reference (id or slug) and
          # read options, so drop every cached single secret and list
          self.cache.invalidate_operation(CACHE_KEY_SINGLE_SECRET)
          self.cache.invalidate_operation(CACHE_KEY_LIST_SECRETS)

        return result.data.secret

    def delete_secret_by_name(
            self,
            secret_name: str,
            secret_path: str,
            environment_slug: str,
            project_id: str = None,
            project_slug: str = None) -> BaseSecret:

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
            model=SingleSecretResponse
        )

        if self.cache.enabled:
          # The secret may be cached under any project reference (id or slug) and
          # read options, so drop every cached single secret and list
          self.cache.invalidate_operation(CACHE_KEY_SINGLE_SECRET)
          self.cache.invalidate_operation(CACHE_KEY_LIST_SECRETS)

        return result.data.secret