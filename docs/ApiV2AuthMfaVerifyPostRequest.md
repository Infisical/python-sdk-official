# ApiV2AuthMfaVerifyPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_token** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_auth_mfa_verify_post_request import ApiV2AuthMfaVerifyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2AuthMfaVerifyPostRequest from a JSON string
api_v2_auth_mfa_verify_post_request_instance = ApiV2AuthMfaVerifyPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2AuthMfaVerifyPostRequest.to_json()

# convert the object into a dict
api_v2_auth_mfa_verify_post_request_dict = api_v2_auth_mfa_verify_post_request_instance.to_dict()
# create an instance of ApiV2AuthMfaVerifyPostRequest from a dict
api_v2_auth_mfa_verify_post_request_from_dict = ApiV2AuthMfaVerifyPostRequest.from_dict(api_v2_auth_mfa_verify_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


