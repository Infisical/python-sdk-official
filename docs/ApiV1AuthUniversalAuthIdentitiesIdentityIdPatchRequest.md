# ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The new list of IPs or CIDR ranges that the Client Secret can be used from. | [optional] 
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The new list of IPs or CIDR ranges that access tokens can be used from. | [optional] 
**access_token_ttl** | **int** | The new lifetime for an access token in seconds. | [optional] 
**access_token_num_uses_limit** | **int** | The new maximum number of times that an access token can be used. | [optional] 
**access_token_max_ttl** | **int** | The new maximum lifetime for an access token in seconds. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_auth_universal_auth_identities_identity_id_patch_request import ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest from a JSON string
api_v1_auth_universal_auth_identities_identity_id_patch_request_instance = ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest.to_json()

# convert the object into a dict
api_v1_auth_universal_auth_identities_identity_id_patch_request_dict = api_v1_auth_universal_auth_identities_identity_id_patch_request_instance.to_dict()
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest from a dict
api_v1_auth_universal_auth_identities_identity_id_patch_request_from_dict = ApiV1AuthUniversalAuthIdentitiesIdentityIdPatchRequest.from_dict(api_v1_auth_universal_auth_identities_identity_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


