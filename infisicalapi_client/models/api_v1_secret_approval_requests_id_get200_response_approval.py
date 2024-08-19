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
from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from infisicalapi_client.models.api_v1_secret_approval_requests_get200_response_approvals_inner_committer_user import ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_commits_inner import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_policy import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner

class ApiV1SecretApprovalRequestsIdGet200ResponseApproval(BaseModel):
    """
    ApiV1SecretApprovalRequestsIdGet200ResponseApproval
    """
    id: StrictStr = Field(...)
    policy_id: StrictStr = Field(default=..., alias="policyId")
    has_merged: Optional[StrictBool] = Field(default=False, alias="hasMerged")
    status: Optional[StrictStr] = 'open'
    conflicts: Optional[Any] = None
    slug: StrictStr = Field(...)
    folder_id: StrictStr = Field(default=..., alias="folderId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    is_replicated: Optional[StrictBool] = Field(default=None, alias="isReplicated")
    committer_user_id: StrictStr = Field(default=..., alias="committerUserId")
    status_changed_by_user_id: Optional[StrictStr] = Field(default=None, alias="statusChangedByUserId")
    bypass_reason: Optional[StrictStr] = Field(default=None, alias="bypassReason")
    policy: ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy = Field(...)
    environment: StrictStr = Field(...)
    status_changed_by_user: Optional[ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser] = Field(default=None, alias="statusChangedByUser")
    committer_user: ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser = Field(default=..., alias="committerUser")
    reviewers: conlist(ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner) = Field(...)
    secret_path: StrictStr = Field(default=..., alias="secretPath")
    commits: conlist(ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner) = Field(...)
    __properties = ["id", "policyId", "hasMerged", "status", "conflicts", "slug", "folderId", "createdAt", "updatedAt", "isReplicated", "committerUserId", "statusChangedByUserId", "bypassReason", "policy", "environment", "statusChangedByUser", "committerUser", "reviewers", "secretPath", "commits"]

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
    def from_json(cls, json_str: str) -> ApiV1SecretApprovalRequestsIdGet200ResponseApproval:
        """Create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApproval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_changed_by_user
        if self.status_changed_by_user:
            _dict['statusChangedByUser'] = self.status_changed_by_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of committer_user
        if self.committer_user:
            _dict['committerUser'] = self.committer_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reviewers (list)
        _items = []
        if self.reviewers:
            for _item in self.reviewers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reviewers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in commits (list)
        _items = []
        if self.commits:
            for _item in self.commits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['commits'] = _items
        # set to None if conflicts (nullable) is None
        # and __fields_set__ contains the field
        if self.conflicts is None and "conflicts" in self.__fields_set__:
            _dict['conflicts'] = None

        # set to None if is_replicated (nullable) is None
        # and __fields_set__ contains the field
        if self.is_replicated is None and "is_replicated" in self.__fields_set__:
            _dict['isReplicated'] = None

        # set to None if status_changed_by_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.status_changed_by_user_id is None and "status_changed_by_user_id" in self.__fields_set__:
            _dict['statusChangedByUserId'] = None

        # set to None if bypass_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.bypass_reason is None and "bypass_reason" in self.__fields_set__:
            _dict['bypassReason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretApprovalRequestsIdGet200ResponseApproval:
        """Create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApproval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretApprovalRequestsIdGet200ResponseApproval.parse_obj(obj)

        _obj = ApiV1SecretApprovalRequestsIdGet200ResponseApproval.parse_obj({
            "id": obj.get("id"),
            "policy_id": obj.get("policyId"),
            "has_merged": obj.get("hasMerged") if obj.get("hasMerged") is not None else False,
            "status": obj.get("status") if obj.get("status") is not None else 'open',
            "conflicts": obj.get("conflicts"),
            "slug": obj.get("slug"),
            "folder_id": obj.get("folderId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "is_replicated": obj.get("isReplicated"),
            "committer_user_id": obj.get("committerUserId"),
            "status_changed_by_user_id": obj.get("statusChangedByUserId"),
            "bypass_reason": obj.get("bypassReason"),
            "policy": ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy.from_dict(obj.get("policy")) if obj.get("policy") is not None else None,
            "environment": obj.get("environment"),
            "status_changed_by_user": ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser.from_dict(obj.get("statusChangedByUser")) if obj.get("statusChangedByUser") is not None else None,
            "committer_user": ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser.from_dict(obj.get("committerUser")) if obj.get("committerUser") is not None else None,
            "reviewers": [ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner.from_dict(_item) for _item in obj.get("reviewers")] if obj.get("reviewers") is not None else None,
            "secret_path": obj.get("secretPath"),
            "commits": [ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner.from_dict(_item) for _item in obj.get("commits")] if obj.get("commits") is not None else None
        })
        return _obj


