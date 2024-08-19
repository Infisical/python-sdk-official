# ApiV1AdminConfigGet200ResponseConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**initialized** | **bool** |  | [optional] [default to False]
**allow_sign_up** | **bool** |  | [optional] [default to True]
**allowed_sign_up_domain** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] [default to '00000000-0000-0000-0000-000000000000']
**trust_saml_emails** | **bool** |  | [optional] [default to False]
**trust_ldap_emails** | **bool** |  | [optional] [default to False]
**trust_oidc_emails** | **bool** |  | [optional] [default to False]
**default_auth_org_id** | **str** |  | [optional] 
**enabled_login_methods** | **List[str]** |  | [optional] 
**is_migration_mode_on** | **bool** |  | 
**default_auth_org_slug** | **str** |  | 
**is_secret_scanning_disabled** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_admin_config_get200_response_config import ApiV1AdminConfigGet200ResponseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdminConfigGet200ResponseConfig from a JSON string
api_v1_admin_config_get200_response_config_instance = ApiV1AdminConfigGet200ResponseConfig.from_json(json)
# print the JSON string representation of the object
print ApiV1AdminConfigGet200ResponseConfig.to_json()

# convert the object into a dict
api_v1_admin_config_get200_response_config_dict = api_v1_admin_config_get200_response_config_instance.to_dict()
# create an instance of ApiV1AdminConfigGet200ResponseConfig from a dict
api_v1_admin_config_get200_response_config_from_dict = ApiV1AdminConfigGet200ResponseConfig.from_dict(api_v1_admin_config_get200_response_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


