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



from pydantic import BaseModel, Field, constr

class ApiV1AdditionalPrivilegeIdentityDeleteRequest(BaseModel):
    """
    ApiV1AdditionalPrivilegeIdentityDeleteRequest
    """
    privilege_slug: constr(strict=True, min_length=1) = Field(default=..., alias="privilegeSlug", description="The slug of the privilege to delete.")
    identity_id: constr(strict=True, min_length=1) = Field(default=..., alias="identityId", description="The ID of the identity to delete.")
    project_slug: constr(strict=True, min_length=1) = Field(default=..., alias="projectSlug", description="The slug of the project of the identity in.")
    __properties = ["privilegeSlug", "identityId", "projectSlug"]

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
    def from_json(cls, json_str: str) -> ApiV1AdditionalPrivilegeIdentityDeleteRequest:
        """Create an instance of ApiV1AdditionalPrivilegeIdentityDeleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AdditionalPrivilegeIdentityDeleteRequest:
        """Create an instance of ApiV1AdditionalPrivilegeIdentityDeleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AdditionalPrivilegeIdentityDeleteRequest.parse_obj(obj)

        _obj = ApiV1AdditionalPrivilegeIdentityDeleteRequest.parse_obj({
            "privilege_slug": obj.get("privilegeSlug"),
            "identity_id": obj.get("identityId"),
            "project_slug": obj.get("projectSlug")
        })
        return _obj


