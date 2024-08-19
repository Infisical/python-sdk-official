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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner(BaseModel):
    """
    ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    description: StrictStr = Field(...)
    client_secret_prefix: StrictStr = Field(default=..., alias="clientSecretPrefix")
    client_secret_num_uses: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="clientSecretNumUses")
    client_secret_num_uses_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="clientSecretNumUsesLimit")
    client_secret_ttl: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="clientSecretTTL")
    identity_uaid: StrictStr = Field(default=..., alias="identityUAId")
    is_client_secret_revoked: Optional[StrictBool] = Field(default=False, alias="isClientSecretRevoked")
    __properties = ["id", "createdAt", "updatedAt", "description", "clientSecretPrefix", "clientSecretNumUses", "clientSecretNumUsesLimit", "clientSecretTTL", "identityUAId", "isClientSecretRevoked"]

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
    def from_json(cls, json_str: str) -> ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner:
        """Create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner:
        """Create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner.parse_obj(obj)

        _obj = ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "description": obj.get("description"),
            "client_secret_prefix": obj.get("clientSecretPrefix"),
            "client_secret_num_uses": obj.get("clientSecretNumUses") if obj.get("clientSecretNumUses") is not None else 0,
            "client_secret_num_uses_limit": obj.get("clientSecretNumUsesLimit") if obj.get("clientSecretNumUsesLimit") is not None else 0,
            "client_secret_ttl": obj.get("clientSecretTTL") if obj.get("clientSecretTTL") is not None else 0,
            "identity_uaid": obj.get("identityUAId"),
            "is_client_secret_revoked": obj.get("isClientSecretRevoked") if obj.get("isClientSecretRevoked") is not None else False
        })
        return _obj


