# ApiV1LdapConfigPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**bind_dn** | **str** |  | [optional] 
**bind_pass** | **str** |  | [optional] 
**unique_user_attribute** | **str** |  | [optional] 
**search_base** | **str** |  | [optional] 
**search_filter** | **str** |  | [optional] 
**group_search_base** | **str** |  | [optional] 
**group_search_filter** | **str** |  | [optional] 
**ca_cert** | **str** |  | [optional] 
**organization_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_patch_request import ApiV1LdapConfigPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigPatchRequest from a JSON string
api_v1_ldap_config_patch_request_instance = ApiV1LdapConfigPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigPatchRequest.to_json()

# convert the object into a dict
api_v1_ldap_config_patch_request_dict = api_v1_ldap_config_patch_request_instance.to_dict()
# create an instance of ApiV1LdapConfigPatchRequest from a dict
api_v1_ldap_config_patch_request_from_dict = ApiV1LdapConfigPatchRequest.from_dict(api_v1_ldap_config_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


