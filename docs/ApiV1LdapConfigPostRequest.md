# ApiV1LdapConfigPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**is_active** | **bool** |  | 
**url** | **str** |  | 
**bind_dn** | **str** |  | 
**bind_pass** | **str** |  | 
**unique_user_attribute** | **str** |  | [optional] [default to 'uidNumber']
**search_base** | **str** |  | 
**search_filter** | **str** |  | [optional] [default to '(uid={{username}})']
**group_search_base** | **str** |  | 
**group_search_filter** | **str** |  | [optional] [default to '(|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))']
**ca_cert** | **str** |  | [optional] [default to '']

## Example

```python
from infisicalapi_client.models.api_v1_ldap_config_post_request import ApiV1LdapConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1LdapConfigPostRequest from a JSON string
api_v1_ldap_config_post_request_instance = ApiV1LdapConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1LdapConfigPostRequest.to_json()

# convert the object into a dict
api_v1_ldap_config_post_request_dict = api_v1_ldap_config_post_request_instance.to_dict()
# create an instance of ApiV1LdapConfigPostRequest from a dict
api_v1_ldap_config_post_request_from_dict = ApiV1LdapConfigPostRequest.from_dict(api_v1_ldap_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


