# ApiV1WebhooksPost200ResponseWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**secret_path** | **str** |  | [optional] [default to '/']
**last_status** | **str** |  | [optional] 
**last_run_error_message** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] [default to False]
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**env_id** | **str** |  | 
**type** | **str** |  | [optional] [default to 'general']
**project_id** | **str** |  | 
**environment** | [**ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_webhooks_post200_response_webhook import ApiV1WebhooksPost200ResponseWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksPost200ResponseWebhook from a JSON string
api_v1_webhooks_post200_response_webhook_instance = ApiV1WebhooksPost200ResponseWebhook.from_json(json)
# print the JSON string representation of the object
print ApiV1WebhooksPost200ResponseWebhook.to_json()

# convert the object into a dict
api_v1_webhooks_post200_response_webhook_dict = api_v1_webhooks_post200_response_webhook_instance.to_dict()
# create an instance of ApiV1WebhooksPost200ResponseWebhook from a dict
api_v1_webhooks_post200_response_webhook_from_dict = ApiV1WebhooksPost200ResponseWebhook.from_dict(api_v1_webhooks_post200_response_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


