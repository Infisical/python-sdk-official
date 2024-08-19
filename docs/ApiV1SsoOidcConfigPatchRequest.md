# ApiV1SsoOidcConfigPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_email_domains** | **str** |  | [optional] [default to '']
**discovery_url** | **str** |  | [optional] 
**configuration_type** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**authorization_endpoint** | **str** |  | [optional] 
**jwks_uri** | **str** |  | [optional] 
**token_endpoint** | **str** |  | [optional] 
**userinfo_endpoint** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**org_slug** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_sso_oidc_config_patch_request import ApiV1SsoOidcConfigPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoOidcConfigPatchRequest from a JSON string
api_v1_sso_oidc_config_patch_request_instance = ApiV1SsoOidcConfigPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoOidcConfigPatchRequest.to_json()

# convert the object into a dict
api_v1_sso_oidc_config_patch_request_dict = api_v1_sso_oidc_config_patch_request_instance.to_dict()
# create an instance of ApiV1SsoOidcConfigPatchRequest from a dict
api_v1_sso_oidc_config_patch_request_from_dict = ApiV1SsoOidcConfigPatchRequest.from_dict(api_v1_sso_oidc_config_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


