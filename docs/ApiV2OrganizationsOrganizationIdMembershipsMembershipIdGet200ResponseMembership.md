# ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership


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
**user** | [**ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser**](ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership import ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership from a JSON string
api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_instance = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_dict = api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership from a dict
api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_from_dict = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembership.from_dict(api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


