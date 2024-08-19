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
from pydantic import BaseModel, Field, StrictBool, constr

class ApiV1WorkspaceWorkspaceIdPatchRequest(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdPatchRequest
    """
    name: Optional[constr(strict=True, max_length=64)] = Field(default=None, description="The new name of the project.")
    auto_capitalization: Optional[StrictBool] = Field(default=None, alias="autoCapitalization", description="Disable or enable auto-capitalization for the project.")
    __properties = ["name", "autoCapitalization"]

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
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdPatchRequest:
        """Create an instance of ApiV1WorkspaceWorkspaceIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdPatchRequest:
        """Create an instance of ApiV1WorkspaceWorkspaceIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdPatchRequest.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdPatchRequest.parse_obj({
            "name": obj.get("name"),
            "auto_capitalization": obj.get("autoCapitalization")
        })
        return _obj


