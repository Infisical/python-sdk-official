# ApiV1LdapConfigGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**organization** | **str** |  | 
**is_active** | **bool** |  | 
**url** | **str** |  | 
**bind_dn** | **str** |  | 
**bind_pass** | **str** |  | 
**unique_user_attribute** | **str** |  | 
**search_base** | **str** |  | 
**search_filter** | **str** |  | 
**group_search_base** | **str** |  | 
**group_search_filter** | **str** |  | 
**ca_cert** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_get200_response import ApiV1LdapConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigGet200Response from a JSON string
api_v1_ldap_config_get200_response_instance = ApiV1LdapConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigGet200Response.to_json()

# convert the object into a dict
api_v1_ldap_config_get200_response_dict = api_v1_ldap_config_get200_response_instance.to_dict()
# create an instance of ApiV1LdapConfigGet200Response from a dict
api_v1_ldap_config_get200_response_from_dict = ApiV1LdapConfigGet200Response.from_dict(api_v1_ldap_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


