# ApiV3SecretsBatchRawDeleteRequestSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | The name of the secret to delete. | 
**type** | **str** |  | [optional] [default to 'shared']

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_delete_request_secrets_inner import ApiV3SecretsBatchRawDeleteRequestSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawDeleteRequestSecretsInner from a JSON string
api_v3_secrets_batch_raw_delete_request_secrets_inner_instance = ApiV3SecretsBatchRawDeleteRequestSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawDeleteRequestSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_delete_request_secrets_inner_dict = api_v3_secrets_batch_raw_delete_request_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawDeleteRequestSecretsInner from a dict
api_v3_secrets_batch_raw_delete_request_secrets_inner_from_dict = ApiV3SecretsBatchRawDeleteRequestSecretsInner.from_dict(api_v3_secrets_batch_raw_delete_request_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


