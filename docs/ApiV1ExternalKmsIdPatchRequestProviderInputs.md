# ApiV1ExternalKmsIdPatchRequestProviderInputs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**ApiV1ExternalKmsPostRequestProviderInputsCredential**](ApiV1ExternalKmsPostRequestProviderInputsCredential.md) |  | [optional] 
**aws_region** | **str** | AWS region to connect | [optional] 
**kms_key_id** | **str** | A pre existing AWS KMS key id to be used for encryption. If not provided a kms key will be generated. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_id_patch_request_provider_inputs import ApiV1ExternalKmsIdPatchRequestProviderInputs

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsIdPatchRequestProviderInputs from a JSON string
api_v1_external_kms_id_patch_request_provider_inputs_instance = ApiV1ExternalKmsIdPatchRequestProviderInputs.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsIdPatchRequestProviderInputs.to_json()

# convert the object into a dict
api_v1_external_kms_id_patch_request_provider_inputs_dict = api_v1_external_kms_id_patch_request_provider_inputs_instance.to_dict()
# create an instance of ApiV1ExternalKmsIdPatchRequestProviderInputs from a dict
api_v1_external_kms_id_patch_request_provider_inputs_from_dict = ApiV1ExternalKmsIdPatchRequestProviderInputs.from_dict(api_v1_external_kms_id_patch_request_provider_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


