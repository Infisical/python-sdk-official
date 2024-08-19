# ApiV3SecretsRawSecretNameDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project where the secret is located. | 
**environment** | **str** | The slug of the environment where the secret is located. | 
**secret_path** | **str** | The path of the secret. | [optional] [default to '/']
**type** | **str** | The type of the secret to delete. | [optional] [default to 'shared']

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_delete_request import ApiV3SecretsRawSecretNameDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawSecretNameDeleteRequest from a JSON string
api_v3_secrets_raw_secret_name_delete_request_instance = ApiV3SecretsRawSecretNameDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawSecretNameDeleteRequest.to_json()

# convert the object into a dict
api_v3_secrets_raw_secret_name_delete_request_dict = api_v3_secrets_raw_secret_name_delete_request_instance.to_dict()
# create an instance of ApiV3SecretsRawSecretNameDeleteRequest from a dict
api_v3_secrets_raw_secret_name_delete_request_from_dict = ApiV3SecretsRawSecretNameDeleteRequest.from_dict(api_v3_secrets_raw_secret_name_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


