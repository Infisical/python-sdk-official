# ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**allowed_service_accounts** | **str** | The new comma-separated list of trusted service account emails corresponding to the GCE resource(s) allowed to authenticate with Infisical. | [optional] [default to '']
**allowed_projects** | **str** | The new comma-separated list of trusted GCP projects that the GCE instance must belong to authenticate with Infisical. | [optional] [default to '']
**allowed_zones** | **str** | The new comma-separated list of trusted zones that the GCE instances must belong to authenticate with Infisical. | [optional] [default to '']
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The new IPs or CIDR ranges that access tokens can be used from. | [optional] 
**access_token_ttl** | **int** | The new lifetime for an acccess token in seconds. | [optional] 
**access_token_num_uses_limit** | **int** | The new maximum number of times that an access token can be used. | [optional] 
**access_token_max_ttl** | **int** | The new maximum lifetime for an acccess token in seconds. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_auth_gcp_auth_identities_identity_id_patch_request import ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest from a JSON string
api_v1_auth_gcp_auth_identities_identity_id_patch_request_instance = ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest.to_json()

# convert the object into a dict
api_v1_auth_gcp_auth_identities_identity_id_patch_request_dict = api_v1_auth_gcp_auth_identities_identity_id_patch_request_instance.to_dict()
# create an instance of ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest from a dict
api_v1_auth_gcp_auth_identities_identity_id_patch_request_from_dict = ApiV1AuthGcpAuthIdentitiesIdentityIdPatchRequest.from_dict(api_v1_auth_gcp_auth_identities_identity_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


