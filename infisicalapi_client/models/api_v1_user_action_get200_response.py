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
from pydantic import BaseModel, Field
from infisicalapi_client.models.api_v1_user_action_get200_response_user_action import ApiV1UserActionGet200ResponseUserAction

class ApiV1UserActionGet200Response(BaseModel):
    """
    ApiV1UserActionGet200Response
    """
    user_action: Optional[ApiV1UserActionGet200ResponseUserAction] = Field(default=None, alias="userAction")
    __properties = ["userAction"]

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
    def from_json(cls, json_str: str) -> ApiV1UserActionGet200Response:
        """Create an instance of ApiV1UserActionGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user_action
        if self.user_action:
            _dict['userAction'] = self.user_action.to_dict()
        # set to None if user_action (nullable) is None
        # and __fields_set__ contains the field
        if self.user_action is None and "user_action" in self.__fields_set__:
            _dict['userAction'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1UserActionGet200Response:
        """Create an instance of ApiV1UserActionGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1UserActionGet200Response.parse_obj(obj)

        _obj = ApiV1UserActionGet200Response.parse_obj({
            "user_action": ApiV1UserActionGet200ResponseUserAction.from_dict(obj.get("userAction")) if obj.get("userAction") is not None else None
        })
        return _obj


