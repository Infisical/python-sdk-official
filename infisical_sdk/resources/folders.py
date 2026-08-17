from typing import Optional
from datetime import datetime, timezone

from infisical_sdk.infisical_requests import InfisicalRequests
from infisical_sdk.api_types import (
    ListFoldersResponse,
    SingleFolderResponse,
    SingleFolderResponseItem,
    CreateFolderResponse,
    CreateFolderResponseItem,
    UpdateFolderResponse,
    UpdateFolderResponseItem,
    DeleteFolderResponse,
    DeleteFolderResponseItem,
)


class V2Folders:
    def __init__(self, requests: InfisicalRequests) -> None:
        self.requests = requests

    def create_folder(
            self,
            name: str,
            environment_slug: str,
            project_id: str,
            path: str = "/",
            description: Optional[str] = None) -> CreateFolderResponseItem:

        request_body = {
            "projectId": project_id,
            "environment": environment_slug,
            "name": name,
            "path": path,
            "description": description,
        }

        result = self.requests.post(
            path="/api/v2/folders",
            json=request_body,
            model=CreateFolderResponse
        )

        return result.data.folder

    def list_folders(
            self,
            project_id: str,
            environment_slug: str,
            path: str,
            last_secret_modified: Optional[datetime] = None,
            recursive: bool = False) -> ListFoldersResponse:

        params = {
            "projectId": project_id,
            "environment": environment_slug,
            "path": path,
            "recursive": recursive,
        }

        if last_secret_modified is not None:
            # Convert to UTC and format as RFC 3339 with 'Z' suffix
            # The API expects UTC times in 'Z' format (e.g., 2023-11-07T05:31:56Z)
            utc_datetime = last_secret_modified.astimezone(timezone.utc) if last_secret_modified.tzinfo else last_secret_modified.replace(tzinfo=timezone.utc)
            params["lastSecretModified"] = utc_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')

        result = self.requests.get(
            path="/api/v2/folders",
            params=params,
            model=ListFoldersResponse
        )

        return result.data

    def get_folder_by_id(
            self,
            id: str) -> SingleFolderResponseItem:

        result = self.requests.get(
            path=f"/api/v2/folders/{id}",
            model=SingleFolderResponse
        )

        return result.data.folder

    def update_folder(
            self,
            folder_id: str,
            name: str,
            environment_slug: str,
            project_id: str,
            path: str = "/",
            description: Optional[str] = None) -> UpdateFolderResponseItem:

        request_body = {
            "projectId": project_id,
            "environment": environment_slug,
            "name": name,
            "path": path,
            "description": description,
        }

        result = self.requests.patch(
            path=f"/api/v2/folders/{folder_id}",
            json=request_body,
            model=UpdateFolderResponse
        )

        return result.data.folder

    def delete_folder(
            self,
            folder_id_or_name: str,
            environment_slug: str,
            project_id: str,
            path: str = "/",
            force_delete: bool = False) -> DeleteFolderResponseItem:

        request_body = {
            "projectId": project_id,
            "environment": environment_slug,
            "path": path,
            "forceDelete": force_delete,
        }

        result = self.requests.delete(
            path=f"/api/v2/folders/{folder_id_or_name}",
            json=request_body,
            model=DeleteFolderResponse
        )

        return result.data.folder

