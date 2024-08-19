# ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_id** | **str** |  | 
**is_temporary** | **bool** |  | 
**temporary_mode** | **str** |  | [optional] 
**temporary_range** | **str** |  | [optional] 
**temporary_access_start_time** | **datetime** |  | [optional] 
**temporary_access_end_time** | **datetime** |  | [optional] 
**permissions** | **object** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response_requests_inner_privilege import ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege from a JSON string
api_v1_access_approvals_requests_get200_response_requests_inner_privilege_instance = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege.to_json()

# convert the object into a dict
api_v1_access_approvals_requests_get200_response_requests_inner_privilege_dict = api_v1_access_approvals_requests_get200_response_requests_inner_privilege_instance.to_dict()
# create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege from a dict
api_v1_access_approvals_requests_get200_response_requests_inner_privilege_from_dict = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege.from_dict(api_v1_access_approvals_requests_get200_response_requests_inner_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


