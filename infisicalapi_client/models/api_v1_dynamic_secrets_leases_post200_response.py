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


from typing import Any, Optional
from pydantic import BaseModel, Field
from infisicalapi_client.models.api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner import ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner
from infisicalapi_client.models.api_v1_dynamic_secrets_name_leases_get200_response_leases_inner import ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner

class ApiV1DynamicSecretsLeasesPost200Response(BaseModel):
    """
    ApiV1DynamicSecretsLeasesPost200Response
    """
    lease: ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner = Field(...)
    dynamic_secret: ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner = Field(default=..., alias="dynamicSecret")
    data: Optional[Any] = None
    __properties = ["lease", "dynamicSecret", "data"]

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
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsLeasesPost200Response:
        """Create an instance of ApiV1DynamicSecretsLeasesPost200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of lease
        if self.lease:
            _dict['lease'] = self.lease.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dynamic_secret
        if self.dynamic_secret:
            _dict['dynamicSecret'] = self.dynamic_secret.to_dict()
        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsLeasesPost200Response:
        """Create an instance of ApiV1DynamicSecretsLeasesPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsLeasesPost200Response.parse_obj(obj)

        _obj = ApiV1DynamicSecretsLeasesPost200Response.parse_obj({
            "lease": ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.from_dict(obj.get("lease")) if obj.get("lease") is not None else None,
            "dynamic_secret": ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner.from_dict(obj.get("dynamicSecret")) if obj.get("dynamicSecret") is not None else None,
            "data": obj.get("data")
        })
        return _obj


