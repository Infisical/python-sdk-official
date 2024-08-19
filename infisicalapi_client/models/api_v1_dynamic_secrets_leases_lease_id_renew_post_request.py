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
from pydantic import BaseModel, Field, StrictStr, constr

class ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest(BaseModel):
    """
    ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest
    """
    ttl: Optional[StrictStr] = Field(default=None, description="The renew TTL that gets added with current expiry (ensure it's below max TTL) for a total less than creation time + max TTL.")
    project_slug: constr(strict=True, min_length=1) = Field(default=..., alias="projectSlug", description="The slug of the project of the dynamic secret in.")
    path: Optional[constr(strict=True, min_length=1)] = Field(default='/', description="The path of the dynamic secret in.")
    environment_slug: constr(strict=True, min_length=1) = Field(default=..., alias="environmentSlug", description="The slug of the environment of the dynamic secret in.")
    __properties = ["ttl", "projectSlug", "path", "environmentSlug"]

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
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest:
        """Create an instance of ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest:
        """Create an instance of ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest.parse_obj(obj)

        _obj = ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest.parse_obj({
            "ttl": obj.get("ttl"),
            "project_slug": obj.get("projectSlug"),
            "path": obj.get("path") if obj.get("path") is not None else '/',
            "environment_slug": obj.get("environmentSlug")
        })
        return _obj


