# ApiV3SecretsRawGet200ResponseSecretsInner


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
**secret_path** | **str** |  | [optional] 
**tags** | [**List[ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner]**](ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_get200_response_secrets_inner import ApiV3SecretsRawGet200ResponseSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawGet200ResponseSecretsInner from a JSON string
api_v3_secrets_raw_get200_response_secrets_inner_instance = ApiV3SecretsRawGet200ResponseSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawGet200ResponseSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_raw_get200_response_secrets_inner_dict = api_v3_secrets_raw_get200_response_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsRawGet200ResponseSecretsInner from a dict
api_v3_secrets_raw_get200_response_secrets_inner_from_dict = ApiV3SecretsRawGet200ResponseSecretsInner.from_dict(api_v3_secrets_raw_get200_response_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


