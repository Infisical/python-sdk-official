# ApiV1AdminConfigPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_sign_up** | **bool** |  | [optional] 
**allowed_sign_up_domain** | **str** |  | [optional] 
**trust_saml_emails** | **bool** |  | [optional] 
**trust_ldap_emails** | **bool** |  | [optional] 
**trust_oidc_emails** | **bool** |  | [optional] 
**default_auth_org_id** | **str** |  | [optional] 
**enabled_login_methods** | **List[str]** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_admin_config_patch_request import ApiV1AdminConfigPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdminConfigPatchRequest from a JSON string
api_v1_admin_config_patch_request_instance = ApiV1AdminConfigPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdminConfigPatchRequest.to_json()

# convert the object into a dict
api_v1_admin_config_patch_request_dict = api_v1_admin_config_patch_request_instance.to_dict()
# create an instance of ApiV1AdminConfigPatchRequest from a dict
api_v1_admin_config_patch_request_from_dict = ApiV1AdminConfigPatchRequest.from_dict(api_v1_admin_config_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


