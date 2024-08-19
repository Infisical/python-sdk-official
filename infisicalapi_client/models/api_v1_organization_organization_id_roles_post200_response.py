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



from pydantic import BaseModel, Field
from infisicalapi_client.models.api_v1_organization_organization_id_roles_post200_response_role import ApiV1OrganizationOrganizationIdRolesPost200ResponseRole

class ApiV1OrganizationOrganizationIdRolesPost200Response(BaseModel):
    """
    ApiV1OrganizationOrganizationIdRolesPost200Response
    """
    role: ApiV1OrganizationOrganizationIdRolesPost200ResponseRole = Field(...)
    __properties = ["role"]

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
    def from_json(cls, json_str: str) -> ApiV1OrganizationOrganizationIdRolesPost200Response:
        """Create an instance of ApiV1OrganizationOrganizationIdRolesPost200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationOrganizationIdRolesPost200Response:
        """Create an instance of ApiV1OrganizationOrganizationIdRolesPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationOrganizationIdRolesPost200Response.parse_obj(obj)

        _obj = ApiV1OrganizationOrganizationIdRolesPost200Response.parse_obj({
            "role": ApiV1OrganizationOrganizationIdRolesPost200ResponseRole.from_dict(obj.get("role")) if obj.get("role") is not None else None
        })
        return _obj


