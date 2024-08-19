# ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The IPs or CIDR ranges that access tokens can be used from. | [optional] [default to [{"ipAddress":"0.0.0.0/0"},{"ipAddress":"::/0"}]]
**access_token_ttl** | **int** | The lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_max_ttl** | **int** | The maximum lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_num_uses_limit** | **int** | The maximum number of times that an access token can be used. | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_auth_token_auth_identities_identity_id_post_request import ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest from a JSON string
api_v1_auth_token_auth_identities_identity_id_post_request_instance = ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest.to_json()

# convert the object into a dict
api_v1_auth_token_auth_identities_identity_id_post_request_dict = api_v1_auth_token_auth_identities_identity_id_post_request_instance.to_dict()
# create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest from a dict
api_v1_auth_token_auth_identities_identity_id_post_request_from_dict = ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequest.from_dict(api_v1_auth_token_auth_identities_identity_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


