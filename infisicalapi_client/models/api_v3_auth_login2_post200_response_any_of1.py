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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ApiV3AuthLogin2Post200ResponseAnyOf1(BaseModel):
    """
    ApiV3AuthLogin2Post200ResponseAnyOf1
    """
    mfa_enabled: StrictBool = Field(default=..., alias="mfaEnabled")
    encryption_version: Optional[Union[StrictFloat, StrictInt]] = Field(default=1, alias="encryptionVersion")
    protected_key: Optional[StrictStr] = Field(default=..., alias="protectedKey")
    protected_key_iv: Optional[StrictStr] = Field(default=..., alias="protectedKeyIV")
    protected_key_tag: Optional[StrictStr] = Field(default=..., alias="protectedKeyTag")
    public_key: StrictStr = Field(default=..., alias="publicKey")
    encrypted_private_key: StrictStr = Field(default=..., alias="encryptedPrivateKey")
    iv: StrictStr = Field(...)
    tag: StrictStr = Field(...)
    token: StrictStr = Field(...)
    __properties = ["mfaEnabled", "encryptionVersion", "protectedKey", "protectedKeyIV", "protectedKeyTag", "publicKey", "encryptedPrivateKey", "iv", "tag", "token"]

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
    def from_json(cls, json_str: str) -> ApiV3AuthLogin2Post200ResponseAnyOf1:
        """Create an instance of ApiV3AuthLogin2Post200ResponseAnyOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if encryption_version (nullable) is None
        # and __fields_set__ contains the field
        if self.encryption_version is None and "encryption_version" in self.__fields_set__:
            _dict['encryptionVersion'] = None

        # set to None if protected_key (nullable) is None
        # and __fields_set__ contains the field
        if self.protected_key is None and "protected_key" in self.__fields_set__:
            _dict['protectedKey'] = None

        # set to None if protected_key_iv (nullable) is None
        # and __fields_set__ contains the field
        if self.protected_key_iv is None and "protected_key_iv" in self.__fields_set__:
            _dict['protectedKeyIV'] = None

        # set to None if protected_key_tag (nullable) is None
        # and __fields_set__ contains the field
        if self.protected_key_tag is None and "protected_key_tag" in self.__fields_set__:
            _dict['protectedKeyTag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV3AuthLogin2Post200ResponseAnyOf1:
        """Create an instance of ApiV3AuthLogin2Post200ResponseAnyOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV3AuthLogin2Post200ResponseAnyOf1.parse_obj(obj)

        _obj = ApiV3AuthLogin2Post200ResponseAnyOf1.parse_obj({
            "mfa_enabled": obj.get("mfaEnabled"),
            "encryption_version": obj.get("encryptionVersion") if obj.get("encryptionVersion") is not None else 1,
            "protected_key": obj.get("protectedKey"),
            "protected_key_iv": obj.get("protectedKeyIV"),
            "protected_key_tag": obj.get("protectedKeyTag"),
            "public_key": obj.get("publicKey"),
            "encrypted_private_key": obj.get("encryptedPrivateKey"),
            "iv": obj.get("iv"),
            "tag": obj.get("tag"),
            "token": obj.get("token")
        })
        return _obj


