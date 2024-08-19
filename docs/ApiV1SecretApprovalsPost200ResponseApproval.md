# ApiV1SecretApprovalsPost200ResponseApproval


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

## Example

```python
from infisicalapi_client.models.api_v1_secret_approvals_post200_response_approval import ApiV1SecretApprovalsPost200ResponseApproval

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalsPost200ResponseApproval from a JSON string
api_v1_secret_approvals_post200_response_approval_instance = ApiV1SecretApprovalsPost200ResponseApproval.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalsPost200ResponseApproval.to_json()

# convert the object into a dict
api_v1_secret_approvals_post200_response_approval_dict = api_v1_secret_approvals_post200_response_approval_instance.to_dict()
# create an instance of ApiV1SecretApprovalsPost200ResponseApproval from a dict
api_v1_secret_approvals_post200_response_approval_from_dict = ApiV1SecretApprovalsPost200ResponseApproval.from_dict(api_v1_secret_approvals_post200_response_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


