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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner(BaseModel):
    """
    ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner
    """
    id: StrictStr = Field(...)
    version: Union[StrictFloat, StrictInt] = Field(...)
    external_entity_id: StrictStr = Field(default=..., alias="externalEntityId")
    expire_at: datetime = Field(default=..., alias="expireAt")
    status: Optional[StrictStr] = None
    status_details: Optional[StrictStr] = Field(default=None, alias="statusDetails")
    dynamic_secret_id: StrictStr = Field(default=..., alias="dynamicSecretId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    __properties = ["id", "version", "externalEntityId", "expireAt", "status", "statusDetails", "dynamicSecretId", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner:
        """Create an instance of ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if status_details (nullable) is None
        # and __fields_set__ contains the field
        if self.status_details is None and "status_details" in self.__fields_set__:
            _dict['statusDetails'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner:
        """Create an instance of ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.parse_obj(obj)

        _obj = ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.parse_obj({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "external_entity_id": obj.get("externalEntityId"),
            "expire_at": obj.get("expireAt"),
            "status": obj.get("status"),
            "status_details": obj.get("statusDetails"),
            "dynamic_secret_id": obj.get("dynamicSecretId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

