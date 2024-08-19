# ApiV2UsersMeApiKeysGet200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**last_used** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_api_keys_get200_response_inner import ApiV2UsersMeApiKeysGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeApiKeysGet200ResponseInner from a JSON string
api_v2_users_me_api_keys_get200_response_inner_instance = ApiV2UsersMeApiKeysGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeApiKeysGet200ResponseInner.to_json()

# convert the object into a dict
api_v2_users_me_api_keys_get200_response_inner_dict = api_v2_users_me_api_keys_get200_response_inner_instance.to_dict()
# create an instance of ApiV2UsersMeApiKeysGet200ResponseInner from a dict
api_v2_users_me_api_keys_get200_response_inner_from_dict = ApiV2UsersMeApiKeysGet200ResponseInner.from_dict(api_v2_users_me_api_keys_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


