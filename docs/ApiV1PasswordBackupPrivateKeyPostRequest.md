# ApiV1PasswordBackupPrivateKeyPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_proof** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**salt** | **str** |  | 
**verifier** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_password_backup_private_key_post_request import ApiV1PasswordBackupPrivateKeyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PasswordBackupPrivateKeyPostRequest from a JSON string
api_v1_password_backup_private_key_post_request_instance = ApiV1PasswordBackupPrivateKeyPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PasswordBackupPrivateKeyPostRequest.to_json()

# convert the object into a dict
api_v1_password_backup_private_key_post_request_dict = api_v1_password_backup_private_key_post_request_instance.to_dict()
# create an instance of ApiV1PasswordBackupPrivateKeyPostRequest from a dict
api_v1_password_backup_private_key_post_request_from_dict = ApiV1PasswordBackupPrivateKeyPostRequest.from_dict(api_v1_password_backup_private_key_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


