# ApiV1ExternalKmsPost200ResponseExternalKms


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] [default to False]
**is_reserved** | **bool** |  | [optional] [default to True]
**org_id** | **str** |  | 
**slug** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**external** | [**ApiV1ExternalKmsPost200ResponseExternalKmsExternal**](ApiV1ExternalKmsPost200ResponseExternalKmsExternal.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_post200_response_external_kms import ApiV1ExternalKmsPost200ResponseExternalKms

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsPost200ResponseExternalKms from a JSON string
api_v1_external_kms_post200_response_external_kms_instance = ApiV1ExternalKmsPost200ResponseExternalKms.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsPost200ResponseExternalKms.to_json()

# convert the object into a dict
api_v1_external_kms_post200_response_external_kms_dict = api_v1_external_kms_post200_response_external_kms_instance.to_dict()
# create an instance of ApiV1ExternalKmsPost200ResponseExternalKms from a dict
api_v1_external_kms_post200_response_external_kms_from_dict = ApiV1ExternalKmsPost200ResponseExternalKms.from_dict(api_v1_external_kms_post200_response_external_kms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


