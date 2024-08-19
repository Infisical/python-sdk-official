# ApiV3SecretsRawSecretNamePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project to create the secret in. | 
**environment** | **str** | The slug of the environment to create the secret in. | 
**secret_path** | **str** | The path to create the secret in. | [optional] [default to '/']
**secret_value** | **str** | The value of the secret to create. | 
**secret_comment** | **str** | Attach a comment to the secret. | [optional] [default to '']
**tag_ids** | **List[str]** | The ID of the tags to be attached to the created secret. | [optional] 
**skip_multiline_encoding** | **bool** | Skip multiline encoding for the secret value. | [optional] 
**type** | **str** | The type of the secret to create. | [optional] [default to 'shared']
**secret_reminder_repeat_days** | **float** | Interval for secret rotation notifications, measured in days | [optional] 
**secret_reminder_note** | **str** | Note to be attached in notification email | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_secret_name_post_request import ApiV3SecretsRawSecretNamePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawSecretNamePostRequest from a JSON string
api_v3_secrets_raw_secret_name_post_request_instance = ApiV3SecretsRawSecretNamePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawSecretNamePostRequest.to_json()

# convert the object into a dict
api_v3_secrets_raw_secret_name_post_request_dict = api_v3_secrets_raw_secret_name_post_request_instance.to_dict()
# create an instance of ApiV3SecretsRawSecretNamePostRequest from a dict
api_v3_secrets_raw_secret_name_post_request_from_dict = ApiV3SecretsRawSecretNamePostRequest.from_dict(api_v3_secrets_raw_secret_name_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


