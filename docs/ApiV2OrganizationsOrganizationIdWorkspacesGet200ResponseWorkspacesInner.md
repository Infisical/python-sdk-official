# ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**organization** | **str** |  | 
**environments** | [**List[ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner]**](ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInnerEnvironmentsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner import ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner from a JSON string
api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner_instance = ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner.to_json()

# convert the object into a dict
api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner_dict = api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner_instance.to_dict()
# create an instance of ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner from a dict
api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner_from_dict = ApiV2OrganizationsOrganizationIdWorkspacesGet200ResponseWorkspacesInner.from_dict(api_v2_organizations_organization_id_workspaces_get200_response_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


