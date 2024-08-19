# ApiV3SecretsBatchRawPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project to delete the secret in. | [optional] 
**workspace_id** | **str** | The ID of the project where the secret is located. | [optional] 
**environment** | **str** | The slug of the environment where the secret is located. | 
**secret_path** | **str** | The path of the secret to update | [optional] [default to '/']
**secrets** | [**List[ApiV3SecretsBatchRawPatchRequestSecretsInner]**](ApiV3SecretsBatchRawPatchRequestSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_patch_request import ApiV3SecretsBatchRawPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawPatchRequest from a JSON string
api_v3_secrets_batch_raw_patch_request_instance = ApiV3SecretsBatchRawPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawPatchRequest.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_patch_request_dict = api_v3_secrets_batch_raw_patch_request_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawPatchRequest from a dict
api_v3_secrets_batch_raw_patch_request_from_dict = ApiV3SecretsBatchRawPatchRequest.from_dict(api_v3_secrets_batch_raw_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


