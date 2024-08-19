# ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assume_role_arn** | **str** | AWS user role to be assumed by infisical | 
**external_id** | **str** | AWS assume role external id for furthur security in authentication | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs_credential_any_of1_data import ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data from a JSON string
api_v1_external_kms_post_request_provider_inputs_credential_any_of1_data_instance = ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data.to_json()

# convert the object into a dict
api_v1_external_kms_post_request_provider_inputs_credential_any_of1_data_dict = api_v1_external_kms_post_request_provider_inputs_credential_any_of1_data_instance.to_dict()
# create an instance of ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data from a dict
api_v1_external_kms_post_request_provider_inputs_credential_any_of1_data_from_dict = ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data.from_dict(api_v1_external_kms_post_request_provider_inputs_credential_any_of1_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


