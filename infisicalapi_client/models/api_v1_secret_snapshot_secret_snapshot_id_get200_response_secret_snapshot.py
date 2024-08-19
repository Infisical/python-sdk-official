# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_environment import ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotEnvironment
from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_folder_version_inner import ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotFolderVersionInner
from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner import ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner

class ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot(BaseModel):
    """
    ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot
    """
    id: StrictStr = Field(...)
    project_id: StrictStr = Field(default=..., alias="projectId")
    environment: ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotEnvironment = Field(...)
    secret_versions: conlist(ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner) = Field(default=..., alias="secretVersions")
    folder_version: conlist(ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotFolderVersionInner) = Field(default=..., alias="folderVersion")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    __properties = ["id", "projectId", "environment", "secretVersions", "folderVersion", "createdAt", "updatedAt"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot:
        """Create an instance of ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in secret_versions (list)
        _items = []
        if self.secret_versions:
            for _item in self.secret_versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secretVersions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in folder_version (list)
        _items = []
        if self.folder_version:
            for _item in self.folder_version:
                if _item:
                    _items.append(_item.to_dict())
            _dict['folderVersion'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot:
        """Create an instance of ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot.parse_obj(obj)

        _obj = ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot.parse_obj({
            "id": obj.get("id"),
            "project_id": obj.get("projectId"),
            "environment": ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotEnvironment.from_dict(obj.get("environment")) if obj.get("environment") is not None else None,
            "secret_versions": [ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner.from_dict(_item) for _item in obj.get("secretVersions")] if obj.get("secretVersions") is not None else None,
            "folder_version": [ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotFolderVersionInner.from_dict(_item) for _item in obj.get("folderVersion")] if obj.get("folderVersion") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


