# ApiV3SecretsRawSecretNamePatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project to update the secret in. | 
**environment** | **str** | The slug of the environment where the secret is located. | 
**secret_value** | **str** | The new value of the secret. | 
**secret_path** | **str** | The path of the secret to update | [optional] [default to '/']
**skip_multiline_encoding** | **bool** | Skip multiline encoding for the secret value. | [optional] 
**type** | **str** | The type of the secret to update. | [optional] [default to 'shared']
**tag_ids** | **List[str]** | The ID of the tags to be attached to the updated secret. | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**secret_reminder_note** | **str** | Note to be attached in notification email | [optional] 
**secret_reminder_repeat_days** | **float** | Interval for secret rotation notifications, measured in days | [optional] 
**new_secret_name** | **str** | The new name for the secret | [optional] 
**secret_comment** | **str** | Update comment to the secret. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_patch_request import ApiV3SecretsRawSecretNamePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawSecretNamePatchRequest from a JSON string
api_v3_secrets_raw_secret_name_patch_request_instance = ApiV3SecretsRawSecretNamePatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawSecretNamePatchRequest.to_json()

# convert the object into a dict
api_v3_secrets_raw_secret_name_patch_request_dict = api_v3_secrets_raw_secret_name_patch_request_instance.to_dict()
# create an instance of ApiV3SecretsRawSecretNamePatchRequest from a dict
api_v3_secrets_raw_secret_name_patch_request_from_dict = ApiV3SecretsRawSecretNamePatchRequest.from_dict(api_v3_secrets_raw_secret_name_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


