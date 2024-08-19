# ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **float** |  | 
**secret_key** | **str** |  | 
**secret_value** | **str** |  | [optional] 
**secret_comment** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret from a JSON string
api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret_instance = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret_dict = api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret from a dict
api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret_from_dict = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.from_dict(api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


