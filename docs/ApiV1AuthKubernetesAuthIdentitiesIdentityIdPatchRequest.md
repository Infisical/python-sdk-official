# ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes_host** | **str** | The new host string, host:port pair, or URL to the base of the Kubernetes API server. | [optional] 
**ca_cert** | **str** | The new PEM-encoded CA cert for the Kubernetes API server. | [optional] 
**token_reviewer_jwt** | **str** | The new long-lived service account JWT token for Infisical to access the TokenReview API to validate other service account JWT tokens submitted by applications/pods. | [optional] 
**allowed_namespaces** | **str** | The new comma-separated list of trusted namespaces that service accounts must belong to authenticate with Infisical. | [optional] 
**allowed_names** | **str** | The new comma-separated list of trusted service account names that can authenticate with Infisical. | [optional] 
**allowed_audience** | **str** | The new optional audience claim that the service account JWT token must have to authenticate with Infisical. | [optional] 
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The new IPs or CIDR ranges that access tokens can be used from. | [optional] 
**access_token_ttl** | **int** | The new lifetime for an acccess token in seconds. | [optional] 
**access_token_num_uses_limit** | **int** | The new maximum number of times that an access token can be used. | [optional] 
**access_token_max_ttl** | **int** | The new maximum lifetime for an acccess token in seconds. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_auth_kubernetes_auth_identities_identity_id_patch_request import ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest from a JSON string
api_v1_auth_kubernetes_auth_identities_identity_id_patch_request_instance = ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest.to_json()

# convert the object into a dict
api_v1_auth_kubernetes_auth_identities_identity_id_patch_request_dict = api_v1_auth_kubernetes_auth_identities_identity_id_patch_request_instance.to_dict()
# create an instance of ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest from a dict
api_v1_auth_kubernetes_auth_identities_identity_id_patch_request_from_dict = ApiV1AuthKubernetesAuthIdentitiesIdentityIdPatchRequest.from_dict(api_v1_auth_kubernetes_auth_identities_identity_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


