# ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**version** | **float** |  | 
**type** | **str** |  | 
**default_ttl** | **str** |  | 
**max_ttl** | **str** |  | [optional] 
**folder_id** | **str** |  | 
**status** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner import ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner from a JSON string
api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner_instance = ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner_dict = api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner_instance.to_dict()
# create an instance of ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner from a dict
api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner_from_dict = ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner.from_dict(api_v1_dynamic_secrets_get200_response_dynamic_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


