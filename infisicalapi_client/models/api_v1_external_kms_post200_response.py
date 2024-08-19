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



from pydantic import BaseModel, Field
from infisicalapi_client.models.api_v1_external_kms_post200_response_external_kms import ApiV1ExternalKmsPost200ResponseExternalKms

class ApiV1ExternalKmsPost200Response(BaseModel):
    """
    ApiV1ExternalKmsPost200Response
    """
    external_kms: ApiV1ExternalKmsPost200ResponseExternalKms = Field(default=..., alias="externalKms")
    __properties = ["externalKms"]

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
    def from_json(cls, json_str: str) -> ApiV1ExternalKmsPost200Response:
        """Create an instance of ApiV1ExternalKmsPost200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of external_kms
        if self.external_kms:
            _dict['externalKms'] = self.external_kms.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ExternalKmsPost200Response:
        """Create an instance of ApiV1ExternalKmsPost200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ExternalKmsPost200Response.parse_obj(obj)

        _obj = ApiV1ExternalKmsPost200Response.parse_obj({
            "external_kms": ApiV1ExternalKmsPost200ResponseExternalKms.from_dict(obj.get("externalKms")) if obj.get("externalKms") is not None else None
        })
        return _obj


