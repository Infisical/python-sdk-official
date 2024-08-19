# ApiV1PasswordEmailPasswordResetVerifyPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_password_email_password_reset_verify_post_request import ApiV1PasswordEmailPasswordResetVerifyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PasswordEmailPasswordResetVerifyPostRequest from a JSON string
api_v1_password_email_password_reset_verify_post_request_instance = ApiV1PasswordEmailPasswordResetVerifyPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PasswordEmailPasswordResetVerifyPostRequest.to_json()

# convert the object into a dict
api_v1_password_email_password_reset_verify_post_request_dict = api_v1_password_email_password_reset_verify_post_request_instance.to_dict()
# create an instance of ApiV1PasswordEmailPasswordResetVerifyPostRequest from a dict
api_v1_password_email_password_reset_verify_post_request_from_dict = ApiV1PasswordEmailPasswordResetVerifyPostRequest.from_dict(api_v1_password_email_password_reset_verify_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


