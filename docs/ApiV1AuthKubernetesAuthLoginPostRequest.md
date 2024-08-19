# ApiV1AuthKubernetesAuthLoginPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The ID of the identity to login. | 
**jwt** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_kubernetes_auth_login_post_request import ApiV1AuthKubernetesAuthLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthKubernetesAuthLoginPostRequest from a JSON string
api_v1_auth_kubernetes_auth_login_post_request_instance = ApiV1AuthKubernetesAuthLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthKubernetesAuthLoginPostRequest.to_json()

# convert the object into a dict
api_v1_auth_kubernetes_auth_login_post_request_dict = api_v1_auth_kubernetes_auth_login_post_request_instance.to_dict()
# create an instance of ApiV1AuthKubernetesAuthLoginPostRequest from a dict
api_v1_auth_kubernetes_auth_login_post_request_from_dict = ApiV1AuthKubernetesAuthLoginPostRequest.from_dict(api_v1_auth_kubernetes_auth_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


