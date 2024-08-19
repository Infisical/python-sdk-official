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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_get200_response_users_inner_user import ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser

class ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner(BaseModel):
    """
    ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner
    """
    id: StrictStr = Field(...)
    role: StrictStr = Field(...)
    status: Optional[StrictStr] = 'invited'
    invite_email: Optional[StrictStr] = Field(default=None, alias="inviteEmail")
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    org_id: StrictStr = Field(default=..., alias="orgId")
    role_id: Optional[StrictStr] = Field(default=None, alias="roleId")
    project_favorites: Optional[conlist(StrictStr)] = Field(default=None, alias="projectFavorites")
    is_active: Optional[StrictBool] = Field(default=True, alias="isActive")
    user: ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser = Field(...)
    __properties = ["id", "role", "status", "inviteEmail", "userId", "orgId", "roleId", "projectFavorites", "isActive", "user"]

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
    def from_json(cls, json_str: str) -> ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner:
        """Create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # set to None if invite_email (nullable) is None
        # and __fields_set__ contains the field
        if self.invite_email is None and "invite_email" in self.__fields_set__:
            _dict['inviteEmail'] = None

        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['userId'] = None

        # set to None if role_id (nullable) is None
        # and __fields_set__ contains the field
        if self.role_id is None and "role_id" in self.__fields_set__:
            _dict['roleId'] = None

        # set to None if project_favorites (nullable) is None
        # and __fields_set__ contains the field
        if self.project_favorites is None and "project_favorites" in self.__fields_set__:
            _dict['projectFavorites'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner:
        """Create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner.parse_obj(obj)

        _obj = ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner.parse_obj({
            "id": obj.get("id"),
            "role": obj.get("role"),
            "status": obj.get("status") if obj.get("status") is not None else 'invited',
            "invite_email": obj.get("inviteEmail"),
            "user_id": obj.get("userId"),
            "org_id": obj.get("orgId"),
            "role_id": obj.get("roleId"),
            "project_favorites": obj.get("projectFavorites"),
            "is_active": obj.get("isActive") if obj.get("isActive") is not None else True,
            "user": ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj


