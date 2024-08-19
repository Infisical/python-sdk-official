# ApiV3SecretsGet200ResponseImportsInnerSecretsInner


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
**id** | **str** |  | 
**workspace** | **str** |  | 
**environment** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_get200_response_imports_inner_secrets_inner import ApiV3SecretsGet200ResponseImportsInnerSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsGet200ResponseImportsInnerSecretsInner from a JSON string
api_v3_secrets_get200_response_imports_inner_secrets_inner_instance = ApiV3SecretsGet200ResponseImportsInnerSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsGet200ResponseImportsInnerSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_get200_response_imports_inner_secrets_inner_dict = api_v3_secrets_get200_response_imports_inner_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsGet200ResponseImportsInnerSecretsInner from a dict
api_v3_secrets_get200_response_imports_inner_secrets_inner_from_dict = ApiV3SecretsGet200ResponseImportsInnerSecretsInner.from_dict(api_v3_secrets_get200_response_imports_inner_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


