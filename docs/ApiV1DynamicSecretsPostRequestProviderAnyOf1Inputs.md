# ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**port** | **float** |  | 
**local_data_center** | **str** |  | 
**keyspace** | **str** |  | [optional] 
**username** | **str** |  | 
**password** | **str** |  | 
**creation_statement** | **str** |  | 
**revocation_statement** | **str** |  | 
**renew_statement** | **str** |  | [optional] 
**ca** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of1_inputs import ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs from a JSON string
api_v1_dynamic_secrets_post_request_provider_any_of1_inputs_instance = ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_post_request_provider_any_of1_inputs_dict = api_v1_dynamic_secrets_post_request_provider_any_of1_inputs_instance.to_dict()
# create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs from a dict
api_v1_dynamic_secrets_post_request_provider_any_of1_inputs_from_dict = ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs.from_dict(api_v1_dynamic_secrets_post_request_provider_any_of1_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


