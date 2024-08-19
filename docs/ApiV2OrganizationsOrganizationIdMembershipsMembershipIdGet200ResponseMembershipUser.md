# ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser


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
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_user import ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser from a JSON string
api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_user_instance = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_user_dict = api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_user_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser from a dict
api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_user_from_dict = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdGet200ResponseMembershipUser.from_dict(api_v2_organizations_organization_id_memberships_membership_id_get200_response_membership_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


