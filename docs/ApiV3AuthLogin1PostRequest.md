# ApiV3AuthLogin1PostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**provider_auth_token** | **str** |  | [optional] 
**client_public_key** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v3_auth_login1_post_request import ApiV3AuthLogin1PostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3AuthLogin1PostRequest from a JSON string
api_v3_auth_login1_post_request_instance = ApiV3AuthLogin1PostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3AuthLogin1PostRequest.to_json()

# convert the object into a dict
api_v3_auth_login1_post_request_dict = api_v3_auth_login1_post_request_instance.to_dict()
# create an instance of ApiV3AuthLogin1PostRequest from a dict
api_v3_auth_login1_post_request_from_dict = ApiV3AuthLogin1PostRequest.from_dict(api_v3_auth_login1_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


