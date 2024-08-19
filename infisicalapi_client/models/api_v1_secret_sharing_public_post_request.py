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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictStr, confloat, conint

class ApiV1SecretSharingPublicPostRequest(BaseModel):
    """
    ApiV1SecretSharingPublicPostRequest
    """
    encrypted_value: StrictStr = Field(default=..., alias="encryptedValue")
    hashed_hex: StrictStr = Field(default=..., alias="hashedHex")
    iv: StrictStr = Field(...)
    tag: StrictStr = Field(...)
    expires_at: StrictStr = Field(default=..., alias="expiresAt")
    expires_after_views: Optional[Union[confloat(ge=1, strict=True), conint(ge=1, strict=True)]] = Field(default=None, alias="expiresAfterViews")
    __properties = ["encryptedValue", "hashedHex", "iv", "tag", "expiresAt", "expiresAfterViews"]

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
    def from_json(cls, json_str: str) -> ApiV1SecretSharingPublicPostRequest:
        """Create an instance of ApiV1SecretSharingPublicPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretSharingPublicPostRequest:
        """Create an instance of ApiV1SecretSharingPublicPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretSharingPublicPostRequest.parse_obj(obj)

        _obj = ApiV1SecretSharingPublicPostRequest.parse_obj({
            "encrypted_value": obj.get("encryptedValue"),
            "hashed_hex": obj.get("hashedHex"),
            "iv": obj.get("iv"),
            "tag": obj.get("tag"),
            "expires_at": obj.get("expiresAt"),
            "expires_after_views": obj.get("expiresAfterViews")
        })
        return _obj


