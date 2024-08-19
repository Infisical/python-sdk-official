# ApiV1WebhooksGet200ResponseWebhooksInner


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
**url** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_webhooks_get200_response_webhooks_inner import ApiV1WebhooksGet200ResponseWebhooksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksGet200ResponseWebhooksInner from a JSON string
api_v1_webhooks_get200_response_webhooks_inner_instance = ApiV1WebhooksGet200ResponseWebhooksInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WebhooksGet200ResponseWebhooksInner.to_json()

# convert the object into a dict
api_v1_webhooks_get200_response_webhooks_inner_dict = api_v1_webhooks_get200_response_webhooks_inner_instance.to_dict()
# create an instance of ApiV1WebhooksGet200ResponseWebhooksInner from a dict
api_v1_webhooks_get200_response_webhooks_inner_from_dict = ApiV1WebhooksGet200ResponseWebhooksInner.from_dict(api_v1_webhooks_get200_response_webhooks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


