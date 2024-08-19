# ApiV1LdapConfigPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**org_id** | **str** |  | 
**is_active** | **bool** |  | 
**url** | **str** |  | 
**encrypted_bind_dn** | **str** |  | 
**bind_dniv** | **str** |  | 
**bind_dn_tag** | **str** |  | 
**encrypted_bind_pass** | **str** |  | 
**bind_pass_iv** | **str** |  | 
**bind_pass_tag** | **str** |  | 
**search_base** | **str** |  | 
**encrypted_ca_cert** | **str** |  | 
**ca_cert_iv** | **str** |  | 
**ca_cert_tag** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**group_search_base** | **str** |  | [optional] [default to '']
**group_search_filter** | **str** |  | [optional] [default to '']
**search_filter** | **str** |  | [optional] [default to '']
**unique_user_attribute** | **str** |  | [optional] [default to '']

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_post200_response import ApiV1LdapConfigPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigPost200Response from a JSON string
api_v1_ldap_config_post200_response_instance = ApiV1LdapConfigPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigPost200Response.to_json()

# convert the object into a dict
api_v1_ldap_config_post200_response_dict = api_v1_ldap_config_post200_response_instance.to_dict()
# create an instance of ApiV1LdapConfigPost200Response from a dict
api_v1_ldap_config_post200_response_from_dict = ApiV1LdapConfigPost200Response.from_dict(api_v1_ldap_config_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


