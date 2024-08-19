# ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | [optional] [default to 'invited']
**invite_email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | 
**role_id** | **str** |  | [optional] 
**project_favorites** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**user** | [**ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser**](ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInnerUser.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_get200_response_users_inner import ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner from a JSON string
api_v2_organizations_organization_id_memberships_get200_response_users_inner_instance = ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_memberships_get200_response_users_inner_dict = api_v2_organizations_organization_id_memberships_get200_response_users_inner_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner from a dict
api_v2_organizations_organization_id_memberships_get200_response_users_inner_from_dict = ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner.from_dict(api_v2_organizations_organization_id_memberships_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


