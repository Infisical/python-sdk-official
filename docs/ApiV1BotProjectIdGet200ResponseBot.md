# ApiV1BotProjectIdGet200ResponseBot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_active** | **bool** |  | [optional] [default to False]
**public_key** | **str** |  | 
**encrypted_project_key** | **str** |  | [optional] 
**encrypted_project_key_nonce** | **str** |  | [optional] 
**project_id** | **str** |  | 
**sender_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_bot_project_id_get200_response_bot import ApiV1BotProjectIdGet200ResponseBot

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1BotProjectIdGet200ResponseBot from a JSON string
api_v1_bot_project_id_get200_response_bot_instance = ApiV1BotProjectIdGet200ResponseBot.from_json(json)
# print the JSON string representation of the object
print ApiV1BotProjectIdGet200ResponseBot.to_json()

# convert the object into a dict
api_v1_bot_project_id_get200_response_bot_dict = api_v1_bot_project_id_get200_response_bot_instance.to_dict()
# create an instance of ApiV1BotProjectIdGet200ResponseBot from a dict
api_v1_bot_project_id_get200_response_bot_from_dict = ApiV1BotProjectIdGet200ResponseBot.from_dict(api_v1_bot_project_id_get200_response_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


