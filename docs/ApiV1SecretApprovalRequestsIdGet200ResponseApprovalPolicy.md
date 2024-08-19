# ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**approvals** | **float** |  | 
**approvers** | [**List[ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser]**](ApiV1SecretApprovalRequestsGet200ResponseApprovalsInnerCommitterUser.md) |  | 
**secret_path** | **str** |  | [optional] 
**enforcement_level** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_policy import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy from a JSON string
api_v1_secret_approval_requests_id_get200_response_approval_policy_instance = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_id_get200_response_approval_policy_dict = api_v1_secret_approval_requests_id_get200_response_approval_policy_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy from a dict
api_v1_secret_approval_requests_id_get200_response_approval_policy_from_dict = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalPolicy.from_dict(api_v1_secret_approval_requests_id_get200_response_approval_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


