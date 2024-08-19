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
from pydantic import BaseModel, Field, StrictStr, validator
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions import ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions

class ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner(BaseModel):
    """
    ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner
    """
    action: StrictStr = Field(default=..., description="Describe what action an entity can take. Possible actions: create, edit, delete, and read")
    subject: StrictStr = Field(default=..., description="The entity this permission pertains to. Possible options: secrets, environments")
    conditions: Optional[ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions] = None
    __properties = ["action", "subject", "conditions"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('read', 'create', 'edit', 'delete'):
            raise ValueError("must be one of enum values ('read', 'create', 'edit', 'delete')")
        return value

    @validator('subject')
    def subject_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('role', 'member', 'groups', 'settings', 'integrations', 'webhooks', 'service-tokens', 'environments', 'tags', 'audit-logs', 'ip-allowlist', 'workspace', 'secrets', 'secret-folders', 'secret-rollback', 'secret-approval', 'secret-rotation', 'identity', 'certificate-authorities', 'certificates', 'kms'):
            raise ValueError("must be one of enum values ('role', 'member', 'groups', 'settings', 'integrations', 'webhooks', 'service-tokens', 'environments', 'tags', 'audit-logs', 'ip-allowlist', 'workspace', 'secrets', 'secret-folders', 'secret-rollback', 'secret-approval', 'secret-rotation', 'identity', 'certificate-authorities', 'certificates', 'kms')")
        return value

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
    def from_json(cls, json_str: str) -> ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner:
        """Create an instance of ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner:
        """Create an instance of ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.parse_obj(obj)

        _obj = ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.parse_obj({
            "action": obj.get("action"),
            "subject": obj.get("subject"),
            "conditions": ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions.from_dict(obj.get("conditions")) if obj.get("conditions") is not None else None
        })
        return _obj

