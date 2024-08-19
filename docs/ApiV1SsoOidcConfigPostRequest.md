# ApiV1SsoOidcConfigPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_email_domains** | **str** |  | [optional] [default to '']
**configuration_type** | **str** |  | 
**issuer** | **str** |  | [optional] [default to '']
**discovery_url** | **str** |  | [optional] [default to '']
**authorization_endpoint** | **str** |  | [optional] [default to '']
**jwks_uri** | **str** |  | [optional] [default to '']
**token_endpoint** | **str** |  | [optional] [default to '']
**userinfo_endpoint** | **str** |  | [optional] [default to '']
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**is_active** | **bool** |  | 
**org_slug** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_sso_oidc_config_post_request import ApiV1SsoOidcConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoOidcConfigPostRequest from a JSON string
api_v1_sso_oidc_config_post_request_instance = ApiV1SsoOidcConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoOidcConfigPostRequest.to_json()

# convert the object into a dict
api_v1_sso_oidc_config_post_request_dict = api_v1_sso_oidc_config_post_request_instance.to_dict()
# create an instance of ApiV1SsoOidcConfigPostRequest from a dict
api_v1_sso_oidc_config_post_request_from_dict = ApiV1SsoOidcConfigPostRequest.from_dict(api_v1_sso_oidc_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


