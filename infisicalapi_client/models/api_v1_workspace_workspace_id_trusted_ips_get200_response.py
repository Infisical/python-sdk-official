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
from infisicalapi_client.models.api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner import ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner

class ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response
    """
    trusted_ips: conlist(ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner) = Field(default=..., alias="trustedIps")
    __properties = ["trustedIps"]

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
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response:
        """Create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in trusted_ips (list)
        _items = []
        if self.trusted_ips:
            for _item in self.trusted_ips:
                if _item:
                    _items.append(_item.to_dict())
            _dict['trustedIps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response:
        """Create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response.parse_obj({
            "trusted_ips": [ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner.from_dict(_item) for _item in obj.get("trustedIps")] if obj.get("trustedIps") is not None else None
        })
        return _obj


