# ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc_discovery_url** | **str** | The new URL used to retrieve the OpenID Connect configuration from the identity provider. | [optional] 
**ca_cert** | **str** | The new PEM-encoded CA cert for establishing secure communication with the Identity Provider endpoints. | [optional] [default to '']
**bound_issuer** | **str** | The new unique identifier of the identity provider issuing the JWT. | [optional] 
**bound_audiences** | **str** | The new list of intended recipients. | [optional] [default to '']
**bound_claims** | **Dict[str, str]** | The new attributes that should be present in the JWT for it to be valid. | [optional] 
**bound_subject** | **str** | The new expected principal that is the subject of the JWT. | [optional] [default to '']
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The new IPs or CIDR ranges that access tokens can be used from. | [optional] [default to [{"ipAddress":"0.0.0.0/0"},{"ipAddress":"::/0"}]]
**access_token_ttl** | **int** | The new lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_max_ttl** | **int** | The new maximum lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_num_uses_limit** | **int** | The new maximum number of times that an access token can be used. | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_auth_oidc_auth_identities_identity_id_patch_request import ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest from a JSON string
api_v1_auth_oidc_auth_identities_identity_id_patch_request_instance = ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest.to_json()

# convert the object into a dict
api_v1_auth_oidc_auth_identities_identity_id_patch_request_dict = api_v1_auth_oidc_auth_identities_identity_id_patch_request_instance.to_dict()
# create an instance of ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest from a dict
api_v1_auth_oidc_auth_identities_identity_id_patch_request_from_dict = ApiV1AuthOidcAuthIdentitiesIdentityIdPatchRequest.from_dict(api_v1_auth_oidc_auth_identities_identity_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


