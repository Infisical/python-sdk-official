# ApiV1UserActionGet200ResponseUserAction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**action** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_user_action_get200_response_user_action import ApiV1UserActionGet200ResponseUserAction

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UserActionGet200ResponseUserAction from a JSON string
api_v1_user_action_get200_response_user_action_instance = ApiV1UserActionGet200ResponseUserAction.from_json(json)
# print the JSON string representation of the object
print ApiV1UserActionGet200ResponseUserAction.to_json()

# convert the object into a dict
api_v1_user_action_get200_response_user_action_dict = api_v1_user_action_get200_response_user_action_instance.to_dict()
# create an instance of ApiV1UserActionGet200ResponseUserAction from a dict
api_v1_user_action_get200_response_user_action_from_dict = ApiV1UserActionGet200ResponseUserAction.from_dict(api_v1_user_action_get200_response_user_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


