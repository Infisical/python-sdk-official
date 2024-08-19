# ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**description** | **str** |  | 
**client_secret_prefix** | **str** |  | 
**client_secret_num_uses** | **float** |  | [optional] [default to 0]
**client_secret_num_uses_limit** | **float** |  | [optional] [default to 0]
**client_secret_ttl** | **float** |  | [optional] [default to 0]
**identity_uaid** | **str** |  | 
**is_client_secret_revoked** | **bool** |  | [optional] [default to False]

## Example

```python
from infisicalapi_client.models.api_v1_auth_universal_auth_identities_identity_id_client_secrets_get200_response_client_secret_data_inner import ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner from a JSON string
api_v1_auth_universal_auth_identities_identity_id_client_secrets_get200_response_client_secret_data_inner_instance = ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner.to_json()

# convert the object into a dict
api_v1_auth_universal_auth_identities_identity_id_client_secrets_get200_response_client_secret_data_inner_dict = api_v1_auth_universal_auth_identities_identity_id_client_secrets_get200_response_client_secret_data_inner_instance.to_dict()
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner from a dict
api_v1_auth_universal_auth_identities_identity_id_client_secrets_get200_response_client_secret_data_inner_from_dict = ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsGet200ResponseClientSecretDataInner.from_dict(api_v1_auth_universal_auth_identities_identity_id_client_secrets_get200_response_client_secret_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


