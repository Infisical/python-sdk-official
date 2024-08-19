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


from typing import List
from pydantic import BaseModel, Field, conlist
from infisicalapi_client.models.api_v1_admin_user_management_users_get200_response_users_inner import ApiV1AdminUserManagementUsersGet200ResponseUsersInner

class ApiV1AdminUserManagementUsersGet200Response(BaseModel):
    """
    ApiV1AdminUserManagementUsersGet200Response
    """
    users: conlist(ApiV1AdminUserManagementUsersGet200ResponseUsersInner) = Field(...)
    __properties = ["users"]

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
    def from_json(cls, json_str: str) -> ApiV1AdminUserManagementUsersGet200Response:
        """Create an instance of ApiV1AdminUserManagementUsersGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item in self.users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AdminUserManagementUsersGet200Response:
        """Create an instance of ApiV1AdminUserManagementUsersGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AdminUserManagementUsersGet200Response.parse_obj(obj)

        _obj = ApiV1AdminUserManagementUsersGet200Response.parse_obj({
            "users": [ApiV1AdminUserManagementUsersGet200ResponseUsersInner.from_dict(_item) for _item in obj.get("users")] if obj.get("users") is not None else None
        })
        return _obj


