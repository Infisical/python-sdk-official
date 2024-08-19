# ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The new role of the membership. | [optional] 
**is_active** | **bool** | The active status of the membership | [optional] 

## Example

```python
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_membership_id_patch_request import ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest from a JSON string
api_v2_organizations_organization_id_memberships_membership_id_patch_request_instance = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_memberships_membership_id_patch_request_dict = api_v2_organizations_organization_id_memberships_membership_id_patch_request_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest from a dict
api_v2_organizations_organization_id_memberships_membership_id_patch_request_from_dict = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdPatchRequest.from_dict(api_v2_organizations_organization_id_memberships_membership_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


