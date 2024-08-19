# ApiV1SsoTokenExchangePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_auth_token** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_sso_token_exchange_post_request import ApiV1SsoTokenExchangePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoTokenExchangePostRequest from a JSON string
api_v1_sso_token_exchange_post_request_instance = ApiV1SsoTokenExchangePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoTokenExchangePostRequest.to_json()

# convert the object into a dict
api_v1_sso_token_exchange_post_request_dict = api_v1_sso_token_exchange_post_request_instance.to_dict()
# create an instance of ApiV1SsoTokenExchangePostRequest from a dict
api_v1_sso_token_exchange_post_request_from_dict = ApiV1SsoTokenExchangePostRequest.from_dict(api_v1_sso_token_exchange_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


