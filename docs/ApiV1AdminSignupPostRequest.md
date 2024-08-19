# ApiV1AdminSignupPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**protected_key** | **str** |  | 
**protected_key_iv** | **str** |  | 
**protected_key_tag** | **str** |  | 
**public_key** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**encrypted_private_key_iv** | **str** |  | 
**encrypted_private_key_tag** | **str** |  | 
**salt** | **str** |  | 
**verifier** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_admin_signup_post_request import ApiV1AdminSignupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdminSignupPostRequest from a JSON string
api_v1_admin_signup_post_request_instance = ApiV1AdminSignupPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdminSignupPostRequest.to_json()

# convert the object into a dict
api_v1_admin_signup_post_request_dict = api_v1_admin_signup_post_request_instance.to_dict()
# create an instance of ApiV1AdminSignupPostRequest from a dict
api_v1_admin_signup_post_request_from_dict = ApiV1AdminSignupPostRequest.from_dict(api_v1_admin_signup_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


