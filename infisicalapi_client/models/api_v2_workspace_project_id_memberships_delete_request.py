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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class ApiV2WorkspaceProjectIdMembershipsDeleteRequest(BaseModel):
    """
    ApiV2WorkspaceProjectIdMembershipsDeleteRequest
    """
    emails: Optional[conlist(StrictStr)] = Field(default=None, description="A list of organization member emails to remove from the project.")
    usernames: Optional[conlist(StrictStr)] = Field(default=None, description="A list of usernames to remove from the project.")
    __properties = ["emails", "usernames"]

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
    def from_json(cls, json_str: str) -> ApiV2WorkspaceProjectIdMembershipsDeleteRequest:
        """Create an instance of ApiV2WorkspaceProjectIdMembershipsDeleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2WorkspaceProjectIdMembershipsDeleteRequest:
        """Create an instance of ApiV2WorkspaceProjectIdMembershipsDeleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2WorkspaceProjectIdMembershipsDeleteRequest.parse_obj(obj)

        _obj = ApiV2WorkspaceProjectIdMembershipsDeleteRequest.parse_obj({
            "emails": obj.get("emails"),
            "usernames": obj.get("usernames")
        })
        return _obj


