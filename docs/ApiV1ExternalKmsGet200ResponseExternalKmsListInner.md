# ApiV1ExternalKmsGet200ResponseExternalKmsListInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] [default to False]
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**slug** | **str** |  | 
**external_kms** | [**ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms**](ApiV1ExternalKmsGet200ResponseExternalKmsListInnerExternalKms.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_get200_response_external_kms_list_inner import ApiV1ExternalKmsGet200ResponseExternalKmsListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsGet200ResponseExternalKmsListInner from a JSON string
api_v1_external_kms_get200_response_external_kms_list_inner_instance = ApiV1ExternalKmsGet200ResponseExternalKmsListInner.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsGet200ResponseExternalKmsListInner.to_json()

# convert the object into a dict
api_v1_external_kms_get200_response_external_kms_list_inner_dict = api_v1_external_kms_get200_response_external_kms_list_inner_instance.to_dict()
# create an instance of ApiV1ExternalKmsGet200ResponseExternalKmsListInner from a dict
api_v1_external_kms_get200_response_external_kms_list_inner_from_dict = ApiV1ExternalKmsGet200ResponseExternalKmsListInner.from_dict(api_v1_external_kms_get200_response_external_kms_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


