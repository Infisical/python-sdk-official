# ApiV1DynamicSecretsNameGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_secret** | [**ApiV1DynamicSecretsNameGet200ResponseDynamicSecret**](ApiV1DynamicSecretsNameGet200ResponseDynamicSecret.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_get200_response import ApiV1DynamicSecretsNameGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNameGet200Response from a JSON string
api_v1_dynamic_secrets_name_get200_response_instance = ApiV1DynamicSecretsNameGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNameGet200Response.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_get200_response_dict = api_v1_dynamic_secrets_name_get200_response_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNameGet200Response from a dict
api_v1_dynamic_secrets_name_get200_response_from_dict = ApiV1DynamicSecretsNameGet200Response.from_dict(api_v1_dynamic_secrets_name_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


