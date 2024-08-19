# ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**email** | **str** |  | [optional] 
**is_email_verified** | **bool** |  | [optional] [default to False]
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**id** | **str** |  | 
**public_key** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_get200_response_users_inner_user import ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser from a JSON string
api_v2_organizations_organization_id_memberships_get200_response_users_inner_user_instance = ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_memberships_get200_response_users_inner_user_dict = api_v2_organizations_organization_id_memberships_get200_response_users_inner_user_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser from a dict
api_v2_organizations_organization_id_memberships_get200_response_users_inner_user_from_dict = ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser.from_dict(api_v2_organizations_organization_id_memberships_get200_response_users_inner_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


