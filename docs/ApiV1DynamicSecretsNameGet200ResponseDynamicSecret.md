# ApiV1DynamicSecretsNameGet200ResponseDynamicSecret


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
**inputs** | **object** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_get200_response_dynamic_secret import ApiV1DynamicSecretsNameGet200ResponseDynamicSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNameGet200ResponseDynamicSecret from a JSON string
api_v1_dynamic_secrets_name_get200_response_dynamic_secret_instance = ApiV1DynamicSecretsNameGet200ResponseDynamicSecret.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNameGet200ResponseDynamicSecret.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_get200_response_dynamic_secret_dict = api_v1_dynamic_secrets_name_get200_response_dynamic_secret_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNameGet200ResponseDynamicSecret from a dict
api_v1_dynamic_secrets_name_get200_response_dynamic_secret_from_dict = ApiV1DynamicSecretsNameGet200ResponseDynamicSecret.from_dict(api_v1_dynamic_secrets_name_get200_response_dynamic_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


