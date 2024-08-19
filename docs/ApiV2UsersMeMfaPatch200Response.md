# ApiV2UsersMeMfaPatch200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser**](ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_mfa_patch200_response import ApiV2UsersMeMfaPatch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeMfaPatch200Response from a JSON string
api_v2_users_me_mfa_patch200_response_instance = ApiV2UsersMeMfaPatch200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeMfaPatch200Response.to_json()

# convert the object into a dict
api_v2_users_me_mfa_patch200_response_dict = api_v2_users_me_mfa_patch200_response_instance.to_dict()
# create an instance of ApiV2UsersMeMfaPatch200Response from a dict
api_v2_users_me_mfa_patch200_response_from_dict = ApiV2UsersMeMfaPatch200Response.from_dict(api_v2_users_me_mfa_patch200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


