# ApiV3SecretsBatchRawPatchRequestSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | The name of the secret to update. | 
**secret_value** | **str** | The new value of the secret. | 
**secret_comment** | **str** | Update comment to the secret. | [optional] 
**skip_multiline_encoding** | **bool** | Skip multiline encoding for the secret value. | [optional] 
**new_secret_name** | **str** | The new name for the secret | [optional] 
**tag_ids** | **List[str]** | The ID of the tags to be attached to the updated secret. | [optional] 
**secret_reminder_note** | **str** | Note to be attached in notification email | [optional] 
**secret_reminder_repeat_days** | **float** | Interval for secret rotation notifications, measured in days | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_patch_request_secrets_inner import ApiV3SecretsBatchRawPatchRequestSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawPatchRequestSecretsInner from a JSON string
api_v3_secrets_batch_raw_patch_request_secrets_inner_instance = ApiV3SecretsBatchRawPatchRequestSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawPatchRequestSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_patch_request_secrets_inner_dict = api_v3_secrets_batch_raw_patch_request_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawPatchRequestSecretsInner from a dict
api_v3_secrets_batch_raw_patch_request_secrets_inner_from_dict = ApiV3SecretsBatchRawPatchRequestSecretsInner.from_dict(api_v3_secrets_batch_raw_patch_request_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


