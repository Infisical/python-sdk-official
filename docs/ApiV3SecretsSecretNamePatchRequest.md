# ApiV3SecretsSecretNamePatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**environment** | **str** |  | 
**secret_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'shared']
**secret_path** | **str** |  | [optional] [default to '/']
**secret_value_ciphertext** | **str** |  | 
**secret_value_iv** | **str** |  | 
**secret_value_tag** | **str** |  | 
**secret_comment_ciphertext** | **str** |  | [optional] 
**secret_comment_iv** | **str** |  | [optional] 
**secret_comment_tag** | **str** |  | [optional] 
**secret_reminder_repeat_days** | **float** |  | [optional] 
**secret_reminder_note** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] 
**secret_name** | **str** |  | [optional] 
**secret_key_iv** | **str** |  | [optional] 
**secret_key_tag** | **str** |  | [optional] 
**secret_key_ciphertext** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_secret_name_patch_request import ApiV3SecretsSecretNamePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsSecretNamePatchRequest from a JSON string
api_v3_secrets_secret_name_patch_request_instance = ApiV3SecretsSecretNamePatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsSecretNamePatchRequest.to_json()

# convert the object into a dict
api_v3_secrets_secret_name_patch_request_dict = api_v3_secrets_secret_name_patch_request_instance.to_dict()
# create an instance of ApiV3SecretsSecretNamePatchRequest from a dict
api_v3_secrets_secret_name_patch_request_from_dict = ApiV3SecretsSecretNamePatchRequest.from_dict(api_v3_secrets_secret_name_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


