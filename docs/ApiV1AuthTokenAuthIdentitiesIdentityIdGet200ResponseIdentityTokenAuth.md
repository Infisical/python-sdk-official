# ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**access_token_ttl** | **float** |  | [optional] [default to 7200]
**access_token_max_ttl** | **float** |  | [optional] [default to 7200]
**access_token_num_uses_limit** | **float** |  | [optional] [default to 0]
**access_token_trusted_ips** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**identity_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_token_auth_identities_identity_id_get200_response_identity_token_auth import ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth from a JSON string
api_v1_auth_token_auth_identities_identity_id_get200_response_identity_token_auth_instance = ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth.to_json()

# convert the object into a dict
api_v1_auth_token_auth_identities_identity_id_get200_response_identity_token_auth_dict = api_v1_auth_token_auth_identities_identity_id_get200_response_identity_token_auth_instance.to_dict()
# create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth from a dict
api_v1_auth_token_auth_identities_identity_id_get200_response_identity_token_auth_from_dict = ApiV1AuthTokenAuthIdentitiesIdentityIdGet200ResponseIdentityTokenAuth.from_dict(api_v1_auth_token_auth_identities_identity_id_get200_response_identity_token_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


