# ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**algorithm** | **str** |  | 
**key_encoding** | **str** |  | 
**salt** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_password_backup_private_key_get200_response_backup_private_key import ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey from a JSON string
api_v1_password_backup_private_key_get200_response_backup_private_key_instance = ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey.from_json(json)
# print the JSON string representation of the object
print ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey.to_json()

# convert the object into a dict
api_v1_password_backup_private_key_get200_response_backup_private_key_dict = api_v1_password_backup_private_key_get200_response_backup_private_key_instance.to_dict()
# create an instance of ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey from a dict
api_v1_password_backup_private_key_get200_response_backup_private_key_from_dict = ApiV1PasswordBackupPrivateKeyGet200ResponseBackupPrivateKey.from_dict(api_v1_password_backup_private_key_get200_response_backup_private_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


