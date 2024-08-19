# ApiV1ExternalKmsIdPatchRequestProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**inputs** | [**ApiV1ExternalKmsIdPatchRequestProviderInputs**](ApiV1ExternalKmsIdPatchRequestProviderInputs.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_id_patch_request_provider import ApiV1ExternalKmsIdPatchRequestProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsIdPatchRequestProvider from a JSON string
api_v1_external_kms_id_patch_request_provider_instance = ApiV1ExternalKmsIdPatchRequestProvider.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsIdPatchRequestProvider.to_json()

# convert the object into a dict
api_v1_external_kms_id_patch_request_provider_dict = api_v1_external_kms_id_patch_request_provider_instance.to_dict()
# create an instance of ApiV1ExternalKmsIdPatchRequestProvider from a dict
api_v1_external_kms_id_patch_request_provider_from_dict = ApiV1ExternalKmsIdPatchRequestProvider.from_dict(api_v1_external_kms_id_patch_request_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


