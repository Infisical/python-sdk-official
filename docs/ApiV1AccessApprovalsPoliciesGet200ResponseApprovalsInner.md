# ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**secret_path** | **str** |  | [optional] 
**approvals** | **float** |  | [optional] [default to 1]
**env_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**enforcement_level** | **str** |  | [optional] [default to 'hard']
**environment** | [**ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.md) |  | 
**project_id** | **str** |  | 
**approvers** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_policies_get200_response_approvals_inner import ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner from a JSON string
api_v1_access_approvals_policies_get200_response_approvals_inner_instance = ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner.to_json()

# convert the object into a dict
api_v1_access_approvals_policies_get200_response_approvals_inner_dict = api_v1_access_approvals_policies_get200_response_approvals_inner_instance.to_dict()
# create an instance of ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner from a dict
api_v1_access_approvals_policies_get200_response_approvals_inner_from_dict = ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner.from_dict(api_v1_access_approvals_policies_get200_response_approvals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


