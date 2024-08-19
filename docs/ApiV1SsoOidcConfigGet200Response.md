# ApiV1SsoOidcConfigGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**issuer** | **str** |  | [optional] 
**authorization_endpoint** | **str** |  | [optional] 
**jwks_uri** | **str** |  | [optional] 
**token_endpoint** | **str** |  | [optional] 
**userinfo_endpoint** | **str** |  | [optional] 
**configuration_type** | **str** |  | 
**discovery_url** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**org_id** | **str** |  | 
**allowed_email_domains** | **str** |  | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_sso_oidc_config_get200_response import ApiV1SsoOidcConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoOidcConfigGet200Response from a JSON string
api_v1_sso_oidc_config_get200_response_instance = ApiV1SsoOidcConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoOidcConfigGet200Response.to_json()

# convert the object into a dict
api_v1_sso_oidc_config_get200_response_dict = api_v1_sso_oidc_config_get200_response_instance.to_dict()
# create an instance of ApiV1SsoOidcConfigGet200Response from a dict
api_v1_sso_oidc_config_get200_response_from_dict = ApiV1SsoOidcConfigGet200Response.from_dict(api_v1_sso_oidc_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


