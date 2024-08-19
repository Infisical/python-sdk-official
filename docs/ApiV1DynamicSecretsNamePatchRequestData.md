# ApiV1DynamicSecretsNamePatchRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **object** | The new partial values for the configurated provider of the dynamic secret | [optional] 
**default_ttl** | **str** | The default TTL that will be applied for all the leases. | [optional] 
**max_ttl** | **str** | The maximum limit a TTL can be leases or renewed. | [optional] 
**new_name** | **str** | The new name for the dynamic secret. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_patch_request_data import ApiV1DynamicSecretsNamePatchRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNamePatchRequestData from a JSON string
api_v1_dynamic_secrets_name_patch_request_data_instance = ApiV1DynamicSecretsNamePatchRequestData.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNamePatchRequestData.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_patch_request_data_dict = api_v1_dynamic_secrets_name_patch_request_data_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNamePatchRequestData from a dict
api_v1_dynamic_secrets_name_patch_request_data_from_dict = ApiV1DynamicSecretsNamePatchRequestData.from_dict(api_v1_dynamic_secrets_name_patch_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


