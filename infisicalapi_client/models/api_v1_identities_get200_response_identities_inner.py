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
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_identities_get200_response_identities_inner_identity import ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity
from infisicalapi_client.models.api_v1_organization_organization_id_groups_get200_response_groups_inner_custom_role import ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole

class ApiV1IdentitiesGet200ResponseIdentitiesInner(BaseModel):
    """
    ApiV1IdentitiesGet200ResponseIdentitiesInner
    """
    id: StrictStr = Field(...)
    role: StrictStr = Field(...)
    role_id: Optional[StrictStr] = Field(default=None, alias="roleId")
    org_id: StrictStr = Field(default=..., alias="orgId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    identity_id: StrictStr = Field(default=..., alias="identityId")
    custom_role: Optional[ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole] = Field(default=None, alias="customRole")
    identity: ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity = Field(...)
    __properties = ["id", "role", "roleId", "orgId", "createdAt", "updatedAt", "identityId", "customRole", "identity"]

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
    def from_json(cls, json_str: str) -> ApiV1IdentitiesGet200ResponseIdentitiesInner:
        """Create an instance of ApiV1IdentitiesGet200ResponseIdentitiesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of custom_role
        if self.custom_role:
            _dict['customRole'] = self.custom_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # set to None if role_id (nullable) is None
        # and __fields_set__ contains the field
        if self.role_id is None and "role_id" in self.__fields_set__:
            _dict['roleId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IdentitiesGet200ResponseIdentitiesInner:
        """Create an instance of ApiV1IdentitiesGet200ResponseIdentitiesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IdentitiesGet200ResponseIdentitiesInner.parse_obj(obj)

        _obj = ApiV1IdentitiesGet200ResponseIdentitiesInner.parse_obj({
            "id": obj.get("id"),
            "role": obj.get("role"),
            "role_id": obj.get("roleId"),
            "org_id": obj.get("orgId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "identity_id": obj.get("identityId"),
            "custom_role": ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole.from_dict(obj.get("customRole")) if obj.get("customRole") is not None else None,
            "identity": ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity.from_dict(obj.get("identity")) if obj.get("identity") is not None else None
        })
        return _obj

