# ApiV1LdapConfigConfigIdGroupMapsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldap_group_cn** | **str** |  | 
**group_slug** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_config_id_group_maps_post_request import ApiV1LdapConfigConfigIdGroupMapsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigConfigIdGroupMapsPostRequest from a JSON string
api_v1_ldap_config_config_id_group_maps_post_request_instance = ApiV1LdapConfigConfigIdGroupMapsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigConfigIdGroupMapsPostRequest.to_json()

# convert the object into a dict
api_v1_ldap_config_config_id_group_maps_post_request_dict = api_v1_ldap_config_config_id_group_maps_post_request_instance.to_dict()
# create an instance of ApiV1LdapConfigConfigIdGroupMapsPostRequest from a dict
api_v1_ldap_config_config_id_group_maps_post_request_from_dict = ApiV1LdapConfigConfigIdGroupMapsPostRequest.from_dict(api_v1_ldap_config_config_id_group_maps_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


