# ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**policy_id** | **str** |  | 
**has_merged** | **bool** |  | [optional] [default to False]
**status** | **str** |  | [optional] [default to 'open']
**conflicts** | **object** |  | [optional] 
**slug** | **str** |  | 
**folder_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_replicated** | **bool** |  | [optional] 
**committer_user_id** | **str** |  | 
**status_changed_by_user_id** | **str** |  | [optional] 
**bypass_reason** | **str** |  | [optional] 
**policy** | [**ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy**](ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy.md) |  | 
**committer_user** | [**ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser**](ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser.md) |  | 
**commits** | [**List[ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitsInner]**](ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitsInner.md) |  | 
**environment** | **str** |  | 
**reviewers** | [**List[ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerReviewersInner]**](ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerReviewersInner.md) |  | 
**approvers** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_get200_response_approvals_inner import ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner from a JSON string
api_v1_secret_approval_requests_get200_response_approvals_inner_instance = ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_get200_response_approvals_inner_dict = api_v1_secret_approval_requests_get200_response_approvals_inner_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner from a dict
api_v1_secret_approval_requests_get200_response_approvals_inner_from_dict = ApiV1SecretApprovalRequestsGet200ResponseApprovalsInner.from_dict(api_v1_secret_approval_requests_get200_response_approvals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


