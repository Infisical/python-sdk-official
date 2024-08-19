# ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | [optional] 
**auth_methods** | **List[str]** |  | [optional] 
**super_admin** | **bool** |  | [optional] [default to False]
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**is_accepted** | **bool** |  | [optional] [default to False]
**is_mfa_enabled** | **bool** |  | [optional] [default to False]
**mfa_methods** | **List[str]** |  | [optional] 
**devices** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_ghost** | **bool** |  | [optional] [default to False]
**username** | **str** |  | 
**is_email_verified** | **bool** |  | [optional] [default to False]
**consecutive_failed_mfa_attempts** | **float** |  | [optional] [default to 0]
**is_locked** | **bool** |  | [optional] [default to False]
**temporary_lock_date_end** | **datetime** |  | [optional] 
**consecutive_failed_password_attempts** | **float** |  | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_password_email_password_reset_verify_post200_response_user import ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser from a JSON string
api_v1_password_email_password_reset_verify_post200_response_user_instance = ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser.from_json(json)
# print the JSON string representation of the object
print ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser.to_json()

# convert the object into a dict
api_v1_password_email_password_reset_verify_post200_response_user_dict = api_v1_password_email_password_reset_verify_post200_response_user_instance.to_dict()
# create an instance of ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser from a dict
api_v1_password_email_password_reset_verify_post200_response_user_from_dict = ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser.from_dict(api_v1_password_email_password_reset_verify_post200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


