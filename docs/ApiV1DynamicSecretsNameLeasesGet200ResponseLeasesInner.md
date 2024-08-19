# ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **float** |  | 
**external_entity_id** | **str** |  | 
**expire_at** | **datetime** |  | 
**status** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**dynamic_secret_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_leases_get200_response_leases_inner import ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner from a JSON string
api_v1_dynamic_secrets_name_leases_get200_response_leases_inner_instance = ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_leases_get200_response_leases_inner_dict = api_v1_dynamic_secrets_name_leases_get200_response_leases_inner_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner from a dict
api_v1_dynamic_secrets_name_leases_get200_response_leases_inner_from_dict = ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.from_dict(api_v1_dynamic_secrets_name_leases_get200_response_leases_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


