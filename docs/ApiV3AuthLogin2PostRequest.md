# ApiV3AuthLogin2PostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**provider_auth_token** | **str** |  | [optional] 
**client_proof** | **str** |  | 
**captcha_token** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_auth_login2_post_request import ApiV3AuthLogin2PostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3AuthLogin2PostRequest from a JSON string
api_v3_auth_login2_post_request_instance = ApiV3AuthLogin2PostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3AuthLogin2PostRequest.to_json()

# convert the object into a dict
api_v3_auth_login2_post_request_dict = api_v3_auth_login2_post_request_instance.to_dict()
# create an instance of ApiV3AuthLogin2PostRequest from a dict
api_v3_auth_login2_post_request_from_dict = ApiV3AuthLogin2PostRequest.from_dict(api_v3_auth_login2_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


