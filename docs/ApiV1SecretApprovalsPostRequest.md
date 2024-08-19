# ApiV1SecretApprovalsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**name** | **str** |  | [optional] 
**environment** | **str** |  | 
**secret_path** | **str** |  | [optional] [default to '/']
**approvers** | **List[str]** |  | 
**approvals** | **float** |  | [optional] [default to 1]
**enforcement_level** | **str** |  | [optional] [default to 'hard']

## Example

```python
from infisicalapi_client.models.api_v1_secret_approvals_post_request import ApiV1SecretApprovalsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalsPostRequest from a JSON string
api_v1_secret_approvals_post_request_instance = ApiV1SecretApprovalsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalsPostRequest.to_json()

# convert the object into a dict
api_v1_secret_approvals_post_request_dict = api_v1_secret_approvals_post_request_instance.to_dict()
# create an instance of ApiV1SecretApprovalsPostRequest from a dict
api_v1_secret_approvals_post_request_from_dict = ApiV1SecretApprovalsPostRequest.from_dict(api_v1_secret_approvals_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


