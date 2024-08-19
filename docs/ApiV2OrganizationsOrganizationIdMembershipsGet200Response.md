# ApiV2OrganizationsOrganizationIdMembershipsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner]**](ApiV2OrganizationsOrganizationIdMembershipsGet200ResponseUsersInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_organizations_organization_id_memberships_get200_response import ApiV2OrganizationsOrganizationIdMembershipsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200Response from a JSON string
api_v2_organizations_organization_id_memberships_get200_response_instance = ApiV2OrganizationsOrganizationIdMembershipsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdMembershipsGet200Response.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_memberships_get200_response_dict = api_v2_organizations_organization_id_memberships_get200_response_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdMembershipsGet200Response from a dict
api_v2_organizations_organization_id_memberships_get200_response_from_dict = ApiV2OrganizationsOrganizationIdMembershipsGet200Response.from_dict(api_v2_organizations_organization_id_memberships_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


