# ApiV1AccessApprovalsRequestsPost200ResponseApproval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**policy_id** | **str** |  | 
**privilege_id** | **str** |  | [optional] 
**requested_by** | **str** |  | 
**is_temporary** | **bool** |  | 
**temporary_range** | **str** |  | [optional] 
**permissions** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_requests_post200_response_approval import ApiV1AccessApprovalsRequestsPost200ResponseApproval

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsRequestsPost200ResponseApproval from a JSON string
api_v1_access_approvals_requests_post200_response_approval_instance = ApiV1AccessApprovalsRequestsPost200ResponseApproval.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsRequestsPost200ResponseApproval.to_json()

# convert the object into a dict
api_v1_access_approvals_requests_post200_response_approval_dict = api_v1_access_approvals_requests_post200_response_approval_instance.to_dict()
# create an instance of ApiV1AccessApprovalsRequestsPost200ResponseApproval from a dict
api_v1_access_approvals_requests_post200_response_approval_from_dict = ApiV1AccessApprovalsRequestsPost200ResponseApproval.from_dict(api_v1_access_approvals_requests_post200_response_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


