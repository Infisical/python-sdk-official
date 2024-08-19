# ApiV3SecretsBatchRawPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project to update the secret in. | [optional] 
**workspace_id** | **str** | The ID of the project to update the secret in. | [optional] 
**environment** | **str** | The slug of the environment to create the secret in. | 
**secret_path** | **str** | The path to create the secret in. | [optional] [default to '/']
**secrets** | [**List[ApiV3SecretsBatchRawPostRequestSecretsInner]**](ApiV3SecretsBatchRawPostRequestSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_post_request import ApiV3SecretsBatchRawPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawPostRequest from a JSON string
api_v3_secrets_batch_raw_post_request_instance = ApiV3SecretsBatchRawPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawPostRequest.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_post_request_dict = api_v3_secrets_batch_raw_post_request_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawPostRequest from a dict
api_v3_secrets_batch_raw_post_request_from_dict = ApiV3SecretsBatchRawPostRequest.from_dict(api_v3_secrets_batch_raw_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


