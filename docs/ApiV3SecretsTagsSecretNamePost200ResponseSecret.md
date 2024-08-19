# ApiV3SecretsTagsSecretNamePost200ResponseSecret


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **float** |  | [optional] [default to 1]
**type** | **str** |  | [optional] [default to 'shared']
**secret_key_ciphertext** | **str** |  | 
**secret_key_iv** | **str** |  | 
**secret_key_tag** | **str** |  | 
**secret_value_ciphertext** | **str** |  | 
**secret_value_iv** | **str** |  | 
**secret_value_tag** | **str** |  | 
**secret_comment_ciphertext** | **str** |  | [optional] 
**secret_comment_iv** | **str** |  | [optional] 
**secret_comment_tag** | **str** |  | [optional] 
**secret_reminder_note** | **str** |  | [optional] 
**secret_reminder_repeat_days** | **float** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] [default to False]
**algorithm** | **str** |  | [optional] [default to 'aes-256-gcm']
**key_encoding** | **str** |  | [optional] [default to 'utf8']
**metadata** | **object** |  | [optional] 
**user_id** | **str** |  | [optional] 
**folder_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**tags** | [**List[ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner]**](ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_tags_secret_name_post200_response_secret import ApiV3SecretsTagsSecretNamePost200ResponseSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsTagsSecretNamePost200ResponseSecret from a JSON string
api_v3_secrets_tags_secret_name_post200_response_secret_instance = ApiV3SecretsTagsSecretNamePost200ResponseSecret.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsTagsSecretNamePost200ResponseSecret.to_json()

# convert the object into a dict
api_v3_secrets_tags_secret_name_post200_response_secret_dict = api_v3_secrets_tags_secret_name_post200_response_secret_instance.to_dict()
# create an instance of ApiV3SecretsTagsSecretNamePost200ResponseSecret from a dict
api_v3_secrets_tags_secret_name_post200_response_secret_from_dict = ApiV3SecretsTagsSecretNamePost200ResponseSecret.from_dict(api_v3_secrets_tags_secret_name_post200_response_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

