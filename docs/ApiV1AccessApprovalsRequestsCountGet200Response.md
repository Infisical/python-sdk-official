# ApiV1AccessApprovalsRequestsCountGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending_count** | **float** |  | 
**finalized_count** | **float** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_requests_count_get200_response import ApiV1AccessApprovalsRequestsCountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsRequestsCountGet200Response from a JSON string
api_v1_access_approvals_requests_count_get200_response_instance = ApiV1AccessApprovalsRequestsCountGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsRequestsCountGet200Response.to_json()

# convert the object into a dict
api_v1_access_approvals_requests_count_get200_response_dict = api_v1_access_approvals_requests_count_get200_response_instance.to_dict()
# create an instance of ApiV1AccessApprovalsRequestsCountGet200Response from a dict
api_v1_access_approvals_requests_count_get200_response_from_dict = ApiV1AccessApprovalsRequestsCountGet200Response.from_dict(api_v1_access_approvals_requests_count_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


