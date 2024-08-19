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
from infisicalapi_client.models.api_v1_organization_get200_response_organizations_inner import ApiV1OrganizationGet200ResponseOrganizationsInner

class ApiV1OrganizationGet200Response(BaseModel):
    """
    ApiV1OrganizationGet200Response
    """
    organizations: conlist(ApiV1OrganizationGet200ResponseOrganizationsInner) = Field(...)
    __properties = ["organizations"]

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
    def from_json(cls, json_str: str) -> ApiV1OrganizationGet200Response:
        """Create an instance of ApiV1OrganizationGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in organizations (list)
        _items = []
        if self.organizations:
            for _item in self.organizations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['organizations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationGet200Response:
        """Create an instance of ApiV1OrganizationGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationGet200Response.parse_obj(obj)

        _obj = ApiV1OrganizationGet200Response.parse_obj({
            "organizations": [ApiV1OrganizationGet200ResponseOrganizationsInner.from_dict(_item) for _item in obj.get("organizations")] if obj.get("organizations") is not None else None
        })
        return _obj


