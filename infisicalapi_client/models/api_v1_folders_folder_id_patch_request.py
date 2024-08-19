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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class ApiV1FoldersFolderIdPatchRequest(BaseModel):
    """
    ApiV1FoldersFolderIdPatchRequest
    """
    workspace_id: StrictStr = Field(default=..., alias="workspaceId", description="The ID of the project where the folder is located.")
    environment: StrictStr = Field(default=..., description="The slug of the environment where the folder is located.")
    name: StrictStr = Field(default=..., description="The new name of the folder.")
    path: Optional[StrictStr] = Field(default='/', description="The path of the folder to update.")
    directory: Optional[StrictStr] = Field(default='/', description="The new directory of the folder to update. (Deprecated in favor of path)")
    __properties = ["workspaceId", "environment", "name", "path", "directory"]

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
    def from_json(cls, json_str: str) -> ApiV1FoldersFolderIdPatchRequest:
        """Create an instance of ApiV1FoldersFolderIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1FoldersFolderIdPatchRequest:
        """Create an instance of ApiV1FoldersFolderIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1FoldersFolderIdPatchRequest.parse_obj(obj)

        _obj = ApiV1FoldersFolderIdPatchRequest.parse_obj({
            "workspace_id": obj.get("workspaceId"),
            "environment": obj.get("environment"),
            "name": obj.get("name"),
            "path": obj.get("path") if obj.get("path") is not None else '/',
            "directory": obj.get("directory") if obj.get("directory") is not None else '/'
        })
        return _obj


