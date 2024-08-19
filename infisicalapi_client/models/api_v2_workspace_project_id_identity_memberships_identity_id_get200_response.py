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
from infisicalapi_client.models.api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner import ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner

class ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response(BaseModel):
    """
    ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response
    """
    identity_membership: ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner = Field(default=..., alias="identityMembership")
    __properties = ["identityMembership"]

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
    def from_json(cls, json_str: str) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response:
        """Create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of identity_membership
        if self.identity_membership:
            _dict['identityMembership'] = self.identity_membership.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response:
        """Create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response.parse_obj(obj)

        _obj = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdGet200Response.parse_obj({
            "identity_membership": ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner.from_dict(obj.get("identityMembership")) if obj.get("identityMembership") is not None else None
        })
        return _obj


