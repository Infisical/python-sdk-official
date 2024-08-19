# ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**roles** | [**List[ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner]**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.md) |  | 
**group** | [**ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInnerGroup**](ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInnerGroup.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner import ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner from a JSON string
api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner_instance = ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner.to_json()

# convert the object into a dict
api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner_dict = api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner from a dict
api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner_from_dict = ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner.from_dict(api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


