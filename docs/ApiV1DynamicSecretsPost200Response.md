# ApiV1DynamicSecretsPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_secret** | [**ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner**](ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_post200_response import ApiV1DynamicSecretsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsPost200Response from a JSON string
api_v1_dynamic_secrets_post200_response_instance = ApiV1DynamicSecretsPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsPost200Response.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_post200_response_dict = api_v1_dynamic_secrets_post200_response_instance.to_dict()
# create an instance of ApiV1DynamicSecretsPost200Response from a dict
api_v1_dynamic_secrets_post200_response_from_dict = ApiV1DynamicSecretsPost200Response.from_dict(api_v1_dynamic_secrets_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


