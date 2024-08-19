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
from pydantic import BaseModel, Field, StrictStr

class ApiV1ExternalKmsPost200ResponseExternalKmsExternal(BaseModel):
    """
    ApiV1ExternalKmsPost200ResponseExternalKmsExternal
    """
    id: StrictStr = Field(...)
    status: Optional[StrictStr] = None
    status_details: Optional[StrictStr] = Field(default=None, alias="statusDetails")
    provider: StrictStr = Field(...)
    __properties = ["id", "status", "statusDetails", "provider"]

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
    def from_json(cls, json_str: str) -> ApiV1ExternalKmsPost200ResponseExternalKmsExternal:
        """Create an instance of ApiV1ExternalKmsPost200ResponseExternalKmsExternal from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ApiV1ExternalKmsPost200ResponseExternalKmsExternal:
        """Create an instance of ApiV1ExternalKmsPost200ResponseExternalKmsExternal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ExternalKmsPost200ResponseExternalKmsExternal.parse_obj(obj)

        _obj = ApiV1ExternalKmsPost200ResponseExternalKmsExternal.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "status_details": obj.get("statusDetails"),
            "provider": obj.get("provider")
        })
        return _obj


