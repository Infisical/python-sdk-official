# ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**access_token_ttl** | **float** |  | [optional] [default to 7200]
**access_token_max_ttl** | **float** |  | [optional] [default to 7200]
**access_token_num_uses_limit** | **float** |  | [optional] [default to 0]
**access_token_trusted_ips** | **object** |  | [optional] 
**identity_id** | **str** |  | 
**oidc_discovery_url** | **str** |  | 
**bound_issuer** | **str** |  | 
**bound_audiences** | **str** |  | 
**bound_claims** | **object** |  | [optional] 
**bound_subject** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**ca_cert** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_oidc_auth_identities_identity_id_get200_response_identity_oidc_auth import ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth from a JSON string
api_v1_auth_oidc_auth_identities_identity_id_get200_response_identity_oidc_auth_instance = ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth.to_json()

# convert the object into a dict
api_v1_auth_oidc_auth_identities_identity_id_get200_response_identity_oidc_auth_dict = api_v1_auth_oidc_auth_identities_identity_id_get200_response_identity_oidc_auth_instance.to_dict()
# create an instance of ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth from a dict
api_v1_auth_oidc_auth_identities_identity_id_get200_response_identity_oidc_auth_from_dict = ApiV1AuthOidcAuthIdentitiesIdentityIdGet200ResponseIdentityOidcAuth.from_dict(api_v1_auth_oidc_auth_identities_identity_id_get200_response_identity_oidc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


