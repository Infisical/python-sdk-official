# ApiV3SecretsRawSecretNameGet200ResponseSecret


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**id** | **str** |  | 
**workspace** | **str** |  | 
**environment** | **str** |  | 
**version** | **float** |  | 
**type** | **str** |  | 
**secret_key** | **str** |  | 
**secret_value** | **str** |  | 
**secret_comment** | **str** |  | 
**secret_reminder_note** | **str** |  | [optional] 
**secret_reminder_repeat_days** | **float** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] [default to False]
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**tags** | [**List[ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner]**](ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_get200_response_secret import ApiV3SecretsRawSecretNameGet200ResponseSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawSecretNameGet200ResponseSecret from a JSON string
api_v3_secrets_raw_secret_name_get200_response_secret_instance = ApiV3SecretsRawSecretNameGet200ResponseSecret.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawSecretNameGet200ResponseSecret.to_json()

# convert the object into a dict
api_v3_secrets_raw_secret_name_get200_response_secret_dict = api_v3_secrets_raw_secret_name_get200_response_secret_instance.to_dict()
# create an instance of ApiV3SecretsRawSecretNameGet200ResponseSecret from a dict
api_v3_secrets_raw_secret_name_get200_response_secret_from_dict = ApiV3SecretsRawSecretNameGet200ResponseSecret.from_dict(api_v3_secrets_raw_secret_name_get200_response_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


