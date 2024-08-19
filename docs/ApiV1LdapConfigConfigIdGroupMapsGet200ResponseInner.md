# ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ldap_config_id** | **str** |  | 
**ldap_group_cn** | **str** |  | 
**group** | [**ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_config_id_group_maps_get200_response_inner import ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner from a JSON string
api_v1_ldap_config_config_id_group_maps_get200_response_inner_instance = ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner.to_json()

# convert the object into a dict
api_v1_ldap_config_config_id_group_maps_get200_response_inner_dict = api_v1_ldap_config_config_id_group_maps_get200_response_inner_instance.to_dict()
# create an instance of ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner from a dict
api_v1_ldap_config_config_id_group_maps_get200_response_inner_from_dict = ApiV1LdapConfigConfigIdGroupMapsGet200ResponseInner.from_dict(api_v1_ldap_config_config_id_group_maps_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


