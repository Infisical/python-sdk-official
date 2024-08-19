# ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner


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
**environment_name** | **str** |  | 
**is_approved** | **bool** |  | 
**privilege** | [**ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege**](ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege.md) |  | 
**policy** | [**ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy**](ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy.md) |  | 
**reviewers** | [**List[ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner]**](ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response_requests_inner import ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner from a JSON string
api_v1_access_approvals_requests_get200_response_requests_inner_instance = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner.to_json()

# convert the object into a dict
api_v1_access_approvals_requests_get200_response_requests_inner_dict = api_v1_access_approvals_requests_get200_response_requests_inner_instance.to_dict()
# create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner from a dict
api_v1_access_approvals_requests_get200_response_requests_inner_from_dict = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner.from_dict(api_v1_access_approvals_requests_get200_response_requests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


