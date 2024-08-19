# ApiV1AuthTokenRenewPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token to renew. | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_token_renew_post_request import ApiV1AuthTokenRenewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthTokenRenewPostRequest from a JSON string
api_v1_auth_token_renew_post_request_instance = ApiV1AuthTokenRenewPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthTokenRenewPostRequest.to_json()

# convert the object into a dict
api_v1_auth_token_renew_post_request_dict = api_v1_auth_token_renew_post_request_instance.to_dict()
# create an instance of ApiV1AuthTokenRenewPostRequest from a dict
api_v1_auth_token_renew_post_request_from_dict = ApiV1AuthTokenRenewPostRequest.from_dict(api_v1_auth_token_renew_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


