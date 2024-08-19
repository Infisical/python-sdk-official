# ApiV1PasswordPasswordResetPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protected_key** | **str** |  | 
**protected_key_iv** | **str** |  | 
**protected_key_tag** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**encrypted_private_key_iv** | **str** |  | 
**encrypted_private_key_tag** | **str** |  | 
**salt** | **str** |  | 
**verifier** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_password_password_reset_post_request import ApiV1PasswordPasswordResetPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PasswordPasswordResetPostRequest from a JSON string
api_v1_password_password_reset_post_request_instance = ApiV1PasswordPasswordResetPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PasswordPasswordResetPostRequest.to_json()

# convert the object into a dict
api_v1_password_password_reset_post_request_dict = api_v1_password_password_reset_post_request_instance.to_dict()
# create an instance of ApiV1PasswordPasswordResetPostRequest from a dict
api_v1_password_password_reset_post_request_from_dict = ApiV1PasswordPasswordResetPostRequest.from_dict(api_v1_password_password_reset_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


