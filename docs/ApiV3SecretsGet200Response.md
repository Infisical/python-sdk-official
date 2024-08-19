# ApiV3SecretsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[ApiV3SecretsGet200ResponseSecretsInner]**](ApiV3SecretsGet200ResponseSecretsInner.md) |  | 
**imports** | [**List[ApiV3SecretsGet200ResponseImportsInner]**](ApiV3SecretsGet200ResponseImportsInner.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_get200_response import ApiV3SecretsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsGet200Response from a JSON string
api_v3_secrets_get200_response_instance = ApiV3SecretsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsGet200Response.to_json()

# convert the object into a dict
api_v3_secrets_get200_response_dict = api_v3_secrets_get200_response_instance.to_dict()
# create an instance of ApiV3SecretsGet200Response from a dict
api_v3_secrets_get200_response_from_dict = ApiV3SecretsGet200Response.from_dict(api_v3_secrets_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


