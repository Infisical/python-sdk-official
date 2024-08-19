# ApiV1PasswordEmailPasswordResetVerifyPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**user** | [**ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser**](ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser.md) |  | 
**token** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_password_email_password_reset_verify_post200_response import ApiV1PasswordEmailPasswordResetVerifyPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PasswordEmailPasswordResetVerifyPost200Response from a JSON string
api_v1_password_email_password_reset_verify_post200_response_instance = ApiV1PasswordEmailPasswordResetVerifyPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1PasswordEmailPasswordResetVerifyPost200Response.to_json()

# convert the object into a dict
api_v1_password_email_password_reset_verify_post200_response_dict = api_v1_password_email_password_reset_verify_post200_response_instance.to_dict()
# create an instance of ApiV1PasswordEmailPasswordResetVerifyPost200Response from a dict
api_v1_password_email_password_reset_verify_post200_response_from_dict = ApiV1PasswordEmailPasswordResetVerifyPost200Response.from_dict(api_v1_password_email_password_reset_verify_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


