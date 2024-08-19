# ApiV3SecretsBatchDeleteRequestSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_name** | **str** |  | 
**type** | **str** |  | [optional] [default to 'shared']

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_delete_request_secrets_inner import ApiV3SecretsBatchDeleteRequestSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchDeleteRequestSecretsInner from a JSON string
api_v3_secrets_batch_delete_request_secrets_inner_instance = ApiV3SecretsBatchDeleteRequestSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchDeleteRequestSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_batch_delete_request_secrets_inner_dict = api_v3_secrets_batch_delete_request_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsBatchDeleteRequestSecretsInner from a dict
api_v3_secrets_batch_delete_request_secrets_inner_from_dict = ApiV3SecretsBatchDeleteRequestSecretsInner.from_dict(api_v3_secrets_batch_delete_request_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


