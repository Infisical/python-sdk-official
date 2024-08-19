# ApiV1SecretApprovalsGet200ResponseApprovalsInner


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
**user_approvers** | [**List[ApiV1SecretApprovalsGet200ResponseApprovalsInnerUserApproversInner]**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerUserApproversInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approvals_get200_response_approvals_inner import ApiV1SecretApprovalsGet200ResponseApprovalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalsGet200ResponseApprovalsInner from a JSON string
api_v1_secret_approvals_get200_response_approvals_inner_instance = ApiV1SecretApprovalsGet200ResponseApprovalsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalsGet200ResponseApprovalsInner.to_json()

# convert the object into a dict
api_v1_secret_approvals_get200_response_approvals_inner_dict = api_v1_secret_approvals_get200_response_approvals_inner_instance.to_dict()
# create an instance of ApiV1SecretApprovalsGet200ResponseApprovalsInner from a dict
api_v1_secret_approvals_get200_response_approvals_inner_from_dict = ApiV1SecretApprovalsGet200ResponseApprovalsInner.from_dict(api_v1_secret_approvals_get200_response_approvals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


