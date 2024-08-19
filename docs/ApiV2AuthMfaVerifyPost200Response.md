# ApiV2AuthMfaVerifyPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_version** | **float** |  | [optional] [default to 1]
**protected_key** | **str** |  | 
**protected_key_iv** | **str** |  | 
**protected_key_tag** | **str** |  | 
**public_key** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_auth_mfa_verify_post200_response import ApiV2AuthMfaVerifyPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2AuthMfaVerifyPost200Response from a JSON string
api_v2_auth_mfa_verify_post200_response_instance = ApiV2AuthMfaVerifyPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2AuthMfaVerifyPost200Response.to_json()

# convert the object into a dict
api_v2_auth_mfa_verify_post200_response_dict = api_v2_auth_mfa_verify_post200_response_instance.to_dict()
# create an instance of ApiV2AuthMfaVerifyPost200Response from a dict
api_v2_auth_mfa_verify_post200_response_from_dict = ApiV2AuthMfaVerifyPost200Response.from_dict(api_v2_auth_mfa_verify_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


