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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner(BaseModel):
    """
    ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner
    """
    name: StrictStr = Field(...)
    slug: StrictStr = Field(...)
    uuid: StrictStr = Field(...)
    type: StrictStr = Field(...)
    is_private: StrictBool = Field(...)
    created_on: StrictStr = Field(...)
    updated_on: Optional[StrictStr] = None
    __properties = ["name", "slug", "uuid", "type", "is_private", "created_on", "updated_on"]

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
    def from_json(cls, json_str: str) -> ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner:
        """Create an instance of ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner:
        """Create an instance of ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner.parse_obj(obj)

        _obj = ApiV1IntegrationAuthIntegrationAuthIdBitbucketWorkspacesGet200ResponseWorkspacesInner.parse_obj({
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "uuid": obj.get("uuid"),
            "type": obj.get("type"),
            "is_private": obj.get("is_private"),
            "created_on": obj.get("created_on"),
            "updated_on": obj.get("updated_on")
        })
        return _obj

