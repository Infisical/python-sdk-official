# ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**access_token_ttl** | **float** |  | [optional] [default to 2592000]
**access_token_max_ttl** | **float** |  | [optional] [default to 2592000]
**access_token_num_uses** | **float** |  | [optional] [default to 0]
**access_token_num_uses_limit** | **float** |  | [optional] [default to 0]
**access_token_last_used_at** | **datetime** |  | [optional] 
**access_token_last_renewed_at** | **datetime** |  | [optional] 
**is_access_token_revoked** | **bool** |  | [optional] [default to False]
**identity_ua_client_secret_id** | **str** |  | [optional] 
**identity_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_auth_token_auth_identities_identity_id_tokens_get200_response_tokens_inner import ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner from a JSON string
api_v1_auth_token_auth_identities_identity_id_tokens_get200_response_tokens_inner_instance = ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner.to_json()

# convert the object into a dict
api_v1_auth_token_auth_identities_identity_id_tokens_get200_response_tokens_inner_dict = api_v1_auth_token_auth_identities_identity_id_tokens_get200_response_tokens_inner_instance.to_dict()
# create an instance of ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner from a dict
api_v1_auth_token_auth_identities_identity_id_tokens_get200_response_tokens_inner_from_dict = ApiV1AuthTokenAuthIdentitiesIdentityIdTokensGet200ResponseTokensInner.from_dict(api_v1_auth_token_auth_identities_identity_id_tokens_get200_response_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


