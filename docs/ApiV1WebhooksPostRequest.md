# ApiV1WebhooksPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'general']
**workspace_id** | **str** |  | 
**environment** | **str** |  | 
**webhook_url** | **str** |  | 
**webhook_secret_key** | **str** |  | [optional] 
**secret_path** | **str** |  | [optional] [default to '/']

## Example

```python
from infisicalapi_client.models.api_v1_webhooks_post_request import ApiV1WebhooksPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WebhooksPostRequest from a JSON string
api_v1_webhooks_post_request_instance = ApiV1WebhooksPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WebhooksPostRequest.to_json()

# convert the object into a dict
api_v1_webhooks_post_request_dict = api_v1_webhooks_post_request_instance.to_dict()
# create an instance of ApiV1WebhooksPostRequest from a dict
api_v1_webhooks_post_request_from_dict = ApiV1WebhooksPostRequest.from_dict(api_v1_webhooks_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


