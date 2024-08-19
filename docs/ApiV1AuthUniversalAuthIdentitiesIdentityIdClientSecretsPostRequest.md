# ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the client secret. | [optional] [default to '']
**num_uses_limit** | **float** | The maximum number of times that the client secret can be used; a value of 0 implies infinite number of uses. | [optional] [default to 0]
**ttl** | **float** | The lifetime for the client secret in seconds. | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request import ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest from a JSON string
api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request_instance = ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest.to_json()

# convert the object into a dict
api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request_dict = api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request_instance.to_dict()
# create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest from a dict
api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request_from_dict = ApiV1AuthUniversalAuthIdentitiesIdentityIdClientSecretsPostRequest.from_dict(api_v1_auth_universal_auth_identities_identity_id_client_secrets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


