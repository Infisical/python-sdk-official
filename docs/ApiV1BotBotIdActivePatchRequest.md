# ApiV1BotBotIdActivePatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | 
**bot_key** | [**ApiV1BotBotIdActivePatchRequestBotKey**](ApiV1BotBotIdActivePatchRequestBotKey.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_bot_bot_id_active_patch_request import ApiV1BotBotIdActivePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1BotBotIdActivePatchRequest from a JSON string
api_v1_bot_bot_id_active_patch_request_instance = ApiV1BotBotIdActivePatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1BotBotIdActivePatchRequest.to_json()

# convert the object into a dict
api_v1_bot_bot_id_active_patch_request_dict = api_v1_bot_bot_id_active_patch_request_instance.to_dict()
# create an instance of ApiV1BotBotIdActivePatchRequest from a dict
api_v1_bot_bot_id_active_patch_request_from_dict = ApiV1BotBotIdActivePatchRequest.from_dict(api_v1_bot_bot_id_active_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


