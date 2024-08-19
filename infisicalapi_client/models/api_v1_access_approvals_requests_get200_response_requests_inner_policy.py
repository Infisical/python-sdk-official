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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist

class ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy(BaseModel):
    """
    ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    approvals: Union[StrictFloat, StrictInt] = Field(...)
    approvers: conlist(StrictStr) = Field(...)
    secret_path: Optional[StrictStr] = Field(default=None, alias="secretPath")
    env_id: StrictStr = Field(default=..., alias="envId")
    enforcement_level: StrictStr = Field(default=..., alias="enforcementLevel")
    __properties = ["id", "name", "approvals", "approvers", "secretPath", "envId", "enforcementLevel"]

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
    def from_json(cls, json_str: str) -> ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy:
        """Create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if secret_path (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_path is None and "secret_path" in self.__fields_set__:
            _dict['secretPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy:
        """Create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy.parse_obj(obj)

        _obj = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "approvals": obj.get("approvals"),
            "approvers": obj.get("approvers"),
            "secret_path": obj.get("secretPath"),
            "env_id": obj.get("envId"),
            "enforcement_level": obj.get("enforcementLevel")
        })
        return _obj

