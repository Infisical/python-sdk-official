# ApiV1DynamicSecretsPostRequestProviderAnyOfInputs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **str** |  | 
**host** | **str** |  | 
**port** | **float** |  | 
**database** | **str** |  | 
**username** | **str** |  | 
**password** | **str** |  | 
**creation_statement** | **str** |  | 
**revocation_statement** | **str** |  | 
**renew_statement** | **str** |  | [optional] 
**ca** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of_inputs import ApiV1DynamicSecretsPostRequestProviderAnyOfInputs

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOfInputs from a JSON string
api_v1_dynamic_secrets_post_request_provider_any_of_inputs_instance = ApiV1DynamicSecretsPostRequestProviderAnyOfInputs.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsPostRequestProviderAnyOfInputs.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_post_request_provider_any_of_inputs_dict = api_v1_dynamic_secrets_post_request_provider_any_of_inputs_instance.to_dict()
# create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOfInputs from a dict
api_v1_dynamic_secrets_post_request_provider_any_of_inputs_from_dict = ApiV1DynamicSecretsPostRequestProviderAnyOfInputs.from_dict(api_v1_dynamic_secrets_post_request_provider_any_of_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


