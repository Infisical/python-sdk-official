# ApiV1ExternalKmsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**provider** | [**ApiV1ExternalKmsIdPatchRequestProvider**](ApiV1ExternalKmsIdPatchRequestProvider.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_id_patch_request import ApiV1ExternalKmsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsIdPatchRequest from a JSON string
api_v1_external_kms_id_patch_request_instance = ApiV1ExternalKmsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsIdPatchRequest.to_json()

# convert the object into a dict
api_v1_external_kms_id_patch_request_dict = api_v1_external_kms_id_patch_request_instance.to_dict()
# create an instance of ApiV1ExternalKmsIdPatchRequest from a dict
api_v1_external_kms_id_patch_request_from_dict = ApiV1ExternalKmsIdPatchRequest.from_dict(api_v1_external_kms_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


