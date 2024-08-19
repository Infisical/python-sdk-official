# ApiV3SecretsRawGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[ApiV3SecretsRawGet200ResponseSecretsInner]**](ApiV3SecretsRawGet200ResponseSecretsInner.md) |  | 
**imports** | [**List[ApiV3SecretsRawGet200ResponseImportsInner]**](ApiV3SecretsRawGet200ResponseImportsInner.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_get200_response import ApiV3SecretsRawGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawGet200Response from a JSON string
api_v3_secrets_raw_get200_response_instance = ApiV3SecretsRawGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawGet200Response.to_json()

# convert the object into a dict
api_v3_secrets_raw_get200_response_dict = api_v3_secrets_raw_get200_response_instance.to_dict()
# create an instance of ApiV3SecretsRawGet200Response from a dict
api_v3_secrets_raw_get200_response_from_dict = ApiV3SecretsRawGet200Response.from_dict(api_v3_secrets_raw_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


