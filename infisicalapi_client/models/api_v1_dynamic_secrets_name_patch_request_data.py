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
from pydantic import BaseModel, Field, StrictStr

class ApiV1DynamicSecretsNamePatchRequestData(BaseModel):
    """
    ApiV1DynamicSecretsNamePatchRequestData
    """
    inputs: Optional[Any] = Field(default=None, description="The new partial values for the configurated provider of the dynamic secret")
    default_ttl: Optional[StrictStr] = Field(default=None, alias="defaultTTL", description="The default TTL that will be applied for all the leases.")
    max_ttl: Optional[StrictStr] = Field(default=None, alias="maxTTL", description="The maximum limit a TTL can be leases or renewed.")
    new_name: Optional[StrictStr] = Field(default=None, alias="newName", description="The new name for the dynamic secret.")
    __properties = ["inputs", "defaultTTL", "maxTTL", "newName"]

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
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsNamePatchRequestData:
        """Create an instance of ApiV1DynamicSecretsNamePatchRequestData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if inputs (nullable) is None
        # and __fields_set__ contains the field
        if self.inputs is None and "inputs" in self.__fields_set__:
            _dict['inputs'] = None

        # set to None if max_ttl (nullable) is None
        # and __fields_set__ contains the field
        if self.max_ttl is None and "max_ttl" in self.__fields_set__:
            _dict['maxTTL'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsNamePatchRequestData:
        """Create an instance of ApiV1DynamicSecretsNamePatchRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsNamePatchRequestData.parse_obj(obj)

        _obj = ApiV1DynamicSecretsNamePatchRequestData.parse_obj({
            "inputs": obj.get("inputs"),
            "default_ttl": obj.get("defaultTTL"),
            "max_ttl": obj.get("maxTTL"),
            "new_name": obj.get("newName")
        })
        return _obj


