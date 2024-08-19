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
from infisicalapi_client.models.api_v1_workspace_project_id_permissions_get200_response_data_membership_roles_inner import ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembershipRolesInner

class ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership(BaseModel):
    """
    ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    user_id: StrictStr = Field(default=..., alias="userId")
    project_id: StrictStr = Field(default=..., alias="projectId")
    roles: conlist(ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembershipRolesInner) = Field(...)
    __properties = ["id", "createdAt", "updatedAt", "userId", "projectId", "roles"]

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
    def from_json(cls, json_str: str) -> ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership:
        """Create an instance of ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership:
        """Create an instance of ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership.parse_obj(obj)

        _obj = ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "user_id": obj.get("userId"),
            "project_id": obj.get("projectId"),
            "roles": [ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembershipRolesInner.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None
        })
        return _obj


