# ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | A list of IPs or CIDR ranges that the Client Secret can be used from together with the Client ID to get back an access token. You can use 0.0.0.0/0, to allow usage from any network address. | [optional] [default to [{"ipAddress":"0.0.0.0/0"},{"ipAddress":"::/0"}]]
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | A list of IPs or CIDR ranges that access tokens can be used from. You can use 0.0.0.0/0, to allow usage from any network address. | [optional] [default to [{"ipAddress":"0.0.0.0/0"},{"ipAddress":"::/0"}]]
**access_token_ttl** | **int** | The lifetime for an access token in seconds. This value will be referenced at renewal time. | [optional] [default to 2592000]
**access_token_max_ttl** | **int** | The maximum lifetime for an access token in seconds. This value will be referenced at renewal time. | [optional] [default to 2592000]
**access_token_num_uses_limit** | **int** | The maximum number of times that an access token can be used; a value of 0 implies infinite number of uses. | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_auth_universal_auth_identities_identity_id_post_request import ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest from a JSON string
api_v1_auth_universal_auth_identities_identity_id_post_request_instance = ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest.to_json()

# convert the object into a dict
api_v1_auth_universal_auth_identities_identity_id_post_request_dict = api_v1_auth_universal_auth_identities_identity_id_post_request_instance.to_dict()
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest from a dict
api_v1_auth_universal_auth_identities_identity_id_post_request_from_dict = ApiV1AuthUniversalAuthIdentitiesIdentityIdPostRequest.from_dict(api_v1_auth_universal_auth_identities_identity_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


