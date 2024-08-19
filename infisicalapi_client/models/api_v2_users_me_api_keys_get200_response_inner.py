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

class ApiV2UsersMeApiKeysGet200ResponseInner(BaseModel):
    """
    ApiV2UsersMeApiKeysGet200ResponseInner
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    last_used: Optional[datetime] = Field(default=None, alias="lastUsed")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    user_id: StrictStr = Field(default=..., alias="userId")
    __properties = ["id", "name", "lastUsed", "expiresAt", "createdAt", "updatedAt", "userId"]

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
    def from_json(cls, json_str: str) -> ApiV2UsersMeApiKeysGet200ResponseInner:
        """Create an instance of ApiV2UsersMeApiKeysGet200ResponseInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if last_used (nullable) is None
        # and __fields_set__ contains the field
        if self.last_used is None and "last_used" in self.__fields_set__:
            _dict['lastUsed'] = None

        # set to None if expires_at (nullable) is None
        # and __fields_set__ contains the field
        if self.expires_at is None and "expires_at" in self.__fields_set__:
            _dict['expiresAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2UsersMeApiKeysGet200ResponseInner:
        """Create an instance of ApiV2UsersMeApiKeysGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2UsersMeApiKeysGet200ResponseInner.parse_obj(obj)

        _obj = ApiV2UsersMeApiKeysGet200ResponseInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "last_used": obj.get("lastUsed"),
            "expires_at": obj.get("expiresAt"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "user_id": obj.get("userId")
        })
        return _obj


