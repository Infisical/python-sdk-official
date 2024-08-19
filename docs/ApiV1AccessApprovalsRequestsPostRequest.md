# ApiV1AccessApprovalsRequestsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **List[str]** |  | 
**is_temporary** | **bool** |  | 
**temporary_range** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_requests_post_request import ApiV1AccessApprovalsRequestsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsRequestsPostRequest from a JSON string
api_v1_access_approvals_requests_post_request_instance = ApiV1AccessApprovalsRequestsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsRequestsPostRequest.to_json()

# convert the object into a dict
api_v1_access_approvals_requests_post_request_dict = api_v1_access_approvals_requests_post_request_instance.to_dict()
# create an instance of ApiV1AccessApprovalsRequestsPostRequest from a dict
api_v1_access_approvals_requests_post_request_from_dict = ApiV1AccessApprovalsRequestsPostRequest.from_dict(api_v1_access_approvals_requests_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


