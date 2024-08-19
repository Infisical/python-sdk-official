# ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_path** | **str** |  | 
**environment** | **str** |  | 
**environment_info** | [**ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.md) |  | 
**folder_id** | **str** |  | [optional] 
**secrets** | [**List[ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner]**](ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_secrets_raw_get200_response_secrets_inner import ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner from a JSON string
api_v1_secret_imports_secrets_raw_get200_response_secrets_inner_instance = ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner.to_json()

# convert the object into a dict
api_v1_secret_imports_secrets_raw_get200_response_secrets_inner_dict = api_v1_secret_imports_secrets_raw_get200_response_secrets_inner_instance.to_dict()
# create an instance of ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner from a dict
api_v1_secret_imports_secrets_raw_get200_response_secrets_inner_from_dict = ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner.from_dict(api_v1_secret_imports_secrets_raw_get200_response_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


