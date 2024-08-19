# ApiV1ExternalKmsPostRequestProviderInputs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**ApiV1ExternalKmsPostRequestProviderInputsCredential**](ApiV1ExternalKmsPostRequestProviderInputsCredential.md) |  | 
**aws_region** | **str** | AWS region to connect | 
**kms_key_id** | **str** | A pre existing AWS KMS key id to be used for encryption. If not provided a kms key will be generated. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_post_request_provider_inputs import ApiV1ExternalKmsPostRequestProviderInputs

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsPostRequestProviderInputs from a JSON string
api_v1_external_kms_post_request_provider_inputs_instance = ApiV1ExternalKmsPostRequestProviderInputs.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsPostRequestProviderInputs.to_json()

# convert the object into a dict
api_v1_external_kms_post_request_provider_inputs_dict = api_v1_external_kms_post_request_provider_inputs_instance.to_dict()
# create an instance of ApiV1ExternalKmsPostRequestProviderInputs from a dict
api_v1_external_kms_post_request_provider_inputs_from_dict = ApiV1ExternalKmsPostRequestProviderInputs.from_dict(api_v1_external_kms_post_request_provider_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


