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
from typing import Any, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1DynamicSecretsNameGet200ResponseDynamicSecret(BaseModel):
    """
    ApiV1DynamicSecretsNameGet200ResponseDynamicSecret
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    version: Union[StrictFloat, StrictInt] = Field(...)
    type: StrictStr = Field(...)
    default_ttl: StrictStr = Field(default=..., alias="defaultTTL")
    max_ttl: Optional[StrictStr] = Field(default=None, alias="maxTTL")
    folder_id: StrictStr = Field(default=..., alias="folderId")
    status: Optional[StrictStr] = None
    status_details: Optional[StrictStr] = Field(default=None, alias="statusDetails")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    inputs: Optional[Any] = None
    __properties = ["id", "name", "version", "type", "defaultTTL", "maxTTL", "folderId", "status", "statusDetails", "createdAt", "updatedAt", "inputs"]

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
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsNameGet200ResponseDynamicSecret:
        """Create an instance of ApiV1DynamicSecretsNameGet200ResponseDynamicSecret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if max_ttl (nullable) is None
        # and __fields_set__ contains the field
        if self.max_ttl is None and "max_ttl" in self.__fields_set__:
            _dict['maxTTL'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if status_details (nullable) is None
        # and __fields_set__ contains the field
        if self.status_details is None and "status_details" in self.__fields_set__:
            _dict['statusDetails'] = None

        # set to None if inputs (nullable) is None
        # and __fields_set__ contains the field
        if self.inputs is None and "inputs" in self.__fields_set__:
            _dict['inputs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsNameGet200ResponseDynamicSecret:
        """Create an instance of ApiV1DynamicSecretsNameGet200ResponseDynamicSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsNameGet200ResponseDynamicSecret.parse_obj(obj)

        _obj = ApiV1DynamicSecretsNameGet200ResponseDynamicSecret.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "version": obj.get("version"),
            "type": obj.get("type"),
            "default_ttl": obj.get("defaultTTL"),
            "max_ttl": obj.get("maxTTL"),
            "folder_id": obj.get("folderId"),
            "status": obj.get("status"),
            "status_details": obj.get("statusDetails"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "inputs": obj.get("inputs")
        })
        return _obj


