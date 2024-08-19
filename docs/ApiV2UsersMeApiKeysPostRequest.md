# ApiV2UsersMeApiKeysPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**expires_in** | **float** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_api_keys_post_request import ApiV2UsersMeApiKeysPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeApiKeysPostRequest from a JSON string
api_v2_users_me_api_keys_post_request_instance = ApiV2UsersMeApiKeysPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeApiKeysPostRequest.to_json()

# convert the object into a dict
api_v2_users_me_api_keys_post_request_dict = api_v2_users_me_api_keys_post_request_instance.to_dict()
# create an instance of ApiV2UsersMeApiKeysPostRequest from a dict
api_v2_users_me_api_keys_post_request_from_dict = ApiV2UsersMeApiKeysPostRequest.from_dict(api_v2_users_me_api_keys_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


