# ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth


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
**type** | **str** |  | 
**allowed_service_accounts** | **str** |  | 
**allowed_projects** | **str** |  | 
**allowed_zones** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_gcp_auth_identities_identity_id_get200_response_identity_gcp_auth import ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth from a JSON string
api_v1_auth_gcp_auth_identities_identity_id_get200_response_identity_gcp_auth_instance = ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth.to_json()

# convert the object into a dict
api_v1_auth_gcp_auth_identities_identity_id_get200_response_identity_gcp_auth_dict = api_v1_auth_gcp_auth_identities_identity_id_get200_response_identity_gcp_auth_instance.to_dict()
# create an instance of ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth from a dict
api_v1_auth_gcp_auth_identities_identity_id_get200_response_identity_gcp_auth_from_dict = ApiV1AuthGcpAuthIdentitiesIdentityIdGet200ResponseIdentityGcpAuth.from_dict(api_v1_auth_gcp_auth_identities_identity_id_get200_response_identity_gcp_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


