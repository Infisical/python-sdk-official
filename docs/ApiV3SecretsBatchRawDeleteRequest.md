# ApiV3SecretsBatchRawDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project to delete the secret in. | [optional] 
**workspace_id** | **str** | The ID of the project where the secret is located. | [optional] 
**environment** | **str** | The slug of the environment where the secret is located. | 
**secret_path** | **str** | The path of the secret. | [optional] [default to '/']
**secrets** | [**List[ApiV3SecretsBatchRawDeleteRequestSecretsInner]**](ApiV3SecretsBatchRawDeleteRequestSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_delete_request import ApiV3SecretsBatchRawDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawDeleteRequest from a JSON string
api_v3_secrets_batch_raw_delete_request_instance = ApiV3SecretsBatchRawDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawDeleteRequest.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_delete_request_dict = api_v3_secrets_batch_raw_delete_request_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawDeleteRequest from a dict
api_v3_secrets_batch_raw_delete_request_from_dict = ApiV3SecretsBatchRawDeleteRequest.from_dict(api_v3_secrets_batch_raw_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


