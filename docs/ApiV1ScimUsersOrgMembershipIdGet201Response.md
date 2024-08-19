# ApiV1ScimUsersOrgMembershipIdGet201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**id** | **str** |  | 
**user_name** | **str** |  | 
**name** | [**ApiV1ScimUsersGet200ResponseResourcesInnerName**](ApiV1ScimUsersGet200ResponseResourcesInnerName.md) |  | 
**emails** | [**List[ApiV1ScimUsersGet200ResponseResourcesInnerEmailsInner]**](ApiV1ScimUsersGet200ResponseResourcesInnerEmailsInner.md) |  | 
**display_name** | **str** |  | 
**active** | **bool** |  | 
**groups** | [**List[ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner]**](ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_users_org_membership_id_get201_response import ApiV1ScimUsersOrgMembershipIdGet201Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimUsersOrgMembershipIdGet201Response from a JSON string
api_v1_scim_users_org_membership_id_get201_response_instance = ApiV1ScimUsersOrgMembershipIdGet201Response.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimUsersOrgMembershipIdGet201Response.to_json()

# convert the object into a dict
api_v1_scim_users_org_membership_id_get201_response_dict = api_v1_scim_users_org_membership_id_get201_response_instance.to_dict()
# create an instance of ApiV1ScimUsersOrgMembershipIdGet201Response from a dict
api_v1_scim_users_org_membership_id_get201_response_from_dict = ApiV1ScimUsersOrgMembershipIdGet201Response.from_dict(api_v1_scim_users_org_membership_id_get201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


