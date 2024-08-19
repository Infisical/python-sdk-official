# ApiV1SecretImportsSecretsRawGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner]**](ApiV1SecretImportsSecretsRawGet200ResponseSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_secrets_raw_get200_response import ApiV1SecretImportsSecretsRawGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsSecretsRawGet200Response from a JSON string
api_v1_secret_imports_secrets_raw_get200_response_instance = ApiV1SecretImportsSecretsRawGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsSecretsRawGet200Response.to_json()

# convert the object into a dict
api_v1_secret_imports_secrets_raw_get200_response_dict = api_v1_secret_imports_secrets_raw_get200_response_instance.to_dict()
# create an instance of ApiV1SecretImportsSecretsRawGet200Response from a dict
api_v1_secret_imports_secrets_raw_get200_response_from_dict = ApiV1SecretImportsSecretsRawGet200Response.from_dict(api_v1_secret_imports_secrets_raw_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


