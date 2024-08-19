# ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **str** |  | 
**secret_access_key** | **str** |  | 
**region** | **str** |  | 
**aws_path** | **str** |  | [optional] 
**permission_boundary_policy_arn** | **str** |  | [optional] 
**policy_document** | **str** |  | [optional] 
**user_groups** | **str** |  | [optional] 
**policy_arns** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of2_inputs import ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs from a JSON string
api_v1_dynamic_secrets_post_request_provider_any_of2_inputs_instance = ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_post_request_provider_any_of2_inputs_dict = api_v1_dynamic_secrets_post_request_provider_any_of2_inputs_instance.to_dict()
# create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs from a dict
api_v1_dynamic_secrets_post_request_provider_any_of2_inputs_from_dict = ApiV1DynamicSecretsPostRequestProviderAnyOf2Inputs.from_dict(api_v1_dynamic_secrets_post_request_provider_any_of2_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


