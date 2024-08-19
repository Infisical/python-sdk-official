# ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**approvals** | **float** |  | 
**approvers** | **List[str]** |  | 
**secret_path** | **str** |  | [optional] 
**enforcement_level** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_get200_response_approvals_inner_policy import ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy from a JSON string
api_v1_secret_approval_requests_get200_response_approvals_inner_policy_instance = ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_get200_response_approvals_inner_policy_dict = api_v1_secret_approval_requests_get200_response_approvals_inner_policy_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy from a dict
api_v1_secret_approval_requests_get200_response_approvals_inner_policy_from_dict = ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerPolicy.from_dict(api_v1_secret_approval_requests_get200_response_approvals_inner_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


