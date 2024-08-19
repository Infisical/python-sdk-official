# ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**provider** | **str** |  | 
**provider_input** | [**ApiV1ExternalKmsPostRequestProviderInputs**](ApiV1ExternalKmsPostRequestProviderInputs.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_id_get200_response_external_kms_external import ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal from a JSON string
api_v1_external_kms_id_get200_response_external_kms_external_instance = ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal.to_json()

# convert the object into a dict
api_v1_external_kms_id_get200_response_external_kms_external_dict = api_v1_external_kms_id_get200_response_external_kms_external_instance.to_dict()
# create an instance of ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal from a dict
api_v1_external_kms_id_get200_response_external_kms_external_from_dict = ApiV1ExternalKmsIdGet200ResponseExternalKmsExternal.from_dict(api_v1_external_kms_id_get200_response_external_kms_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


