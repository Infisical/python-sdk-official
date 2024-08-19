# ApiV1AuthUniversalAuthLoginPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Your Machine Identity Client ID. | 
**client_secret** | **str** | Your Machine Identity Client Secret. | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_universal_auth_login_post_request import ApiV1AuthUniversalAuthLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthUniversalAuthLoginPostRequest from a JSON string
api_v1_auth_universal_auth_login_post_request_instance = ApiV1AuthUniversalAuthLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthUniversalAuthLoginPostRequest.to_json()

# convert the object into a dict
api_v1_auth_universal_auth_login_post_request_dict = api_v1_auth_universal_auth_login_post_request_instance.to_dict()
# create an instance of ApiV1AuthUniversalAuthLoginPostRequest from a dict
api_v1_auth_universal_auth_login_post_request_from_dict = ApiV1AuthUniversalAuthLoginPostRequest.from_dict(api_v1_auth_universal_auth_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


