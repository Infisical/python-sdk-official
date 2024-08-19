# ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes_host** | **str** | The host string, host:port pair, or URL to the base of the Kubernetes API server. | 
**ca_cert** | **str** | The PEM-encoded CA cert for the Kubernetes API server. | [optional] [default to '']
**token_reviewer_jwt** | **str** | The long-lived service account JWT token for Infisical to access the TokenReview API to validate other service account JWT tokens submitted by applications/pods. | 
**allowed_namespaces** | **str** | The comma-separated list of trusted namespaces that service accounts must belong to authenticate with Infisical. | 
**allowed_names** | **str** | The comma-separated list of trusted service account names that can authenticate with Infisical. | 
**allowed_audience** | **str** | The optional audience claim that the service account JWT token must have to authenticate with Infisical. | 
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The IPs or CIDR ranges that access tokens can be used from. | [optional] [default to [{"ipAddress":"0.0.0.0/0"},{"ipAddress":"::/0"}]]
**access_token_ttl** | **int** | The lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_max_ttl** | **int** | The maximum lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_num_uses_limit** | **int** | The maximum number of times that an access token can be used. | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_auth_kubernetes_auth_identities_identity_id_post_request import ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest from a JSON string
api_v1_auth_kubernetes_auth_identities_identity_id_post_request_instance = ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest.to_json()

# convert the object into a dict
api_v1_auth_kubernetes_auth_identities_identity_id_post_request_dict = api_v1_auth_kubernetes_auth_identities_identity_id_post_request_instance.to_dict()
# create an instance of ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest from a dict
api_v1_auth_kubernetes_auth_identities_identity_id_post_request_from_dict = ApiV1AuthKubernetesAuthIdentitiesIdentityIdPostRequest.from_dict(api_v1_auth_kubernetes_auth_identities_identity_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


