# ApiV1LdapConfigConfigIdGroupMapsPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ldap_config_id** | **str** |  | 
**ldap_group_cn** | **str** |  | 
**group_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_config_id_group_maps_post200_response import ApiV1LdapConfigConfigIdGroupMapsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigConfigIdGroupMapsPost200Response from a JSON string
api_v1_ldap_config_config_id_group_maps_post200_response_instance = ApiV1LdapConfigConfigIdGroupMapsPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigConfigIdGroupMapsPost200Response.to_json()

# convert the object into a dict
api_v1_ldap_config_config_id_group_maps_post200_response_dict = api_v1_ldap_config_config_id_group_maps_post200_response_instance.to_dict()
# create an instance of ApiV1LdapConfigConfigIdGroupMapsPost200Response from a dict
api_v1_ldap_config_config_id_group_maps_post200_response_from_dict = ApiV1LdapConfigConfigIdGroupMapsPost200Response.from_dict(api_v1_ldap_config_config_id_group_maps_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


