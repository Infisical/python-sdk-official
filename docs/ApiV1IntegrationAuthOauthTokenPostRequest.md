# ApiV1IntegrationAuthOauthTokenPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**code** | **str** |  | 
**integration** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_integration_auth_oauth_token_post_request import ApiV1IntegrationAuthOauthTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IntegrationAuthOauthTokenPostRequest from a JSON string
api_v1_integration_auth_oauth_token_post_request_instance = ApiV1IntegrationAuthOauthTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1IntegrationAuthOauthTokenPostRequest.to_json()

# convert the object into a dict
api_v1_integration_auth_oauth_token_post_request_dict = api_v1_integration_auth_oauth_token_post_request_instance.to_dict()
# create an instance of ApiV1IntegrationAuthOauthTokenPostRequest from a dict
api_v1_integration_auth_oauth_token_post_request_from_dict = ApiV1IntegrationAuthOauthTokenPostRequest.from_dict(api_v1_integration_auth_oauth_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


