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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from infisicalapi_client.models.api_v1_integration_integration_id_patch_request_metadata import ApiV1IntegrationIntegrationIdPatchRequestMetadata

class ApiV1IntegrationIntegrationIdPatchRequest(BaseModel):
    """
    ApiV1IntegrationIntegrationIdPatchRequest
    """
    app: Optional[StrictStr] = Field(default=None, description="The name of the external integration providers app entity that you want to sync secrets with. Used in Netlify, GitHub, Vercel integrations.")
    app_id: Optional[StrictStr] = Field(default=None, alias="appId", description="The ID of the external integration providers app entity that you want to sync secrets with. Used in Netlify, GitHub, Vercel integrations.")
    is_active: StrictBool = Field(default=..., alias="isActive", description="Whether the integration should be active or disabled.")
    secret_path: Optional[StrictStr] = Field(default='/', alias="secretPath", description="The path of the secrets to sync secrets from.")
    target_environment: StrictStr = Field(default=..., alias="targetEnvironment", description="The target environment of the integration provider. Used in cloudflare pages, TeamCity, Gitlab integrations.")
    owner: StrictStr = Field(default=..., description="External integration providers service entity owner. Used in Github.")
    environment: StrictStr = Field(default=..., description="The environment to sync secrets from.")
    metadata: Optional[ApiV1IntegrationIntegrationIdPatchRequestMetadata] = None
    __properties = ["app", "appId", "isActive", "secretPath", "targetEnvironment", "owner", "environment", "metadata"]

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
    def from_json(cls, json_str: str) -> ApiV1IntegrationIntegrationIdPatchRequest:
        """Create an instance of ApiV1IntegrationIntegrationIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IntegrationIntegrationIdPatchRequest:
        """Create an instance of ApiV1IntegrationIntegrationIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IntegrationIntegrationIdPatchRequest.parse_obj(obj)

        _obj = ApiV1IntegrationIntegrationIdPatchRequest.parse_obj({
            "app": obj.get("app"),
            "app_id": obj.get("appId"),
            "is_active": obj.get("isActive"),
            "secret_path": obj.get("secretPath") if obj.get("secretPath") is not None else '/',
            "target_environment": obj.get("targetEnvironment"),
            "owner": obj.get("owner"),
            "environment": obj.get("environment"),
            "metadata": ApiV1IntegrationIntegrationIdPatchRequestMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None
        })
        return _obj


