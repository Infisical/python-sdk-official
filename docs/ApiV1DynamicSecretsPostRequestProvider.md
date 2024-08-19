# ApiV1DynamicSecretsPostRequestProvider

The type of dynamic secret.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**inputs** | [**ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs**](ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider import ApiV1DynamicSecretsPostRequestProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsPostRequestProvider from a JSON string
api_v1_dynamic_secrets_post_request_provider_instance = ApiV1DynamicSecretsPostRequestProvider.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsPostRequestProvider.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_post_request_provider_dict = api_v1_dynamic_secrets_post_request_provider_instance.to_dict()
# create an instance of ApiV1DynamicSecretsPostRequestProvider from a dict
api_v1_dynamic_secrets_post_request_provider_from_dict = ApiV1DynamicSecretsPostRequestProvider.from_dict(api_v1_dynamic_secrets_post_request_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


