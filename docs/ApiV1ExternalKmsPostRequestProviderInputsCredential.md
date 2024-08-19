# ApiV1ExternalKmsPostRequestProviderInputsCredential

AWS credential information to connect

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**data** | [**ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data**](ApiV1ExternalKmsPostRequestProviderInputsCredentialAnyOf1Data.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs_credential import ApiV1ExternalKmsPostRequestProviderInputsCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsPostRequestProviderInputsCredential from a JSON string
api_v1_external_kms_post_request_provider_inputs_credential_instance = ApiV1ExternalKmsPostRequestProviderInputsCredential.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsPostRequestProviderInputsCredential.to_json()

# convert the object into a dict
api_v1_external_kms_post_request_provider_inputs_credential_dict = api_v1_external_kms_post_request_provider_inputs_credential_instance.to_dict()
# create an instance of ApiV1ExternalKmsPostRequestProviderInputsCredential from a dict
api_v1_external_kms_post_request_provider_inputs_credential_from_dict = ApiV1ExternalKmsPostRequestProviderInputsCredential.from_dict(api_v1_external_kms_post_request_provider_inputs_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


