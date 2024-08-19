# ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth


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
**tenant_id** | **str** |  | 
**resource** | **str** |  | 
**allowed_service_principal_ids** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_azure_auth_identities_identity_id_get200_response_identity_azure_auth import ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth from a JSON string
api_v1_auth_azure_auth_identities_identity_id_get200_response_identity_azure_auth_instance = ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth.to_json()

# convert the object into a dict
api_v1_auth_azure_auth_identities_identity_id_get200_response_identity_azure_auth_dict = api_v1_auth_azure_auth_identities_identity_id_get200_response_identity_azure_auth_instance.to_dict()
# create an instance of ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth from a dict
api_v1_auth_azure_auth_identities_identity_id_get200_response_identity_azure_auth_from_dict = ApiV1AuthAzureAuthIdentitiesIdentityIdGet200ResponseIdentityAzureAuth.from_dict(api_v1_auth_azure_auth_identities_identity_id_get200_response_identity_azure_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


