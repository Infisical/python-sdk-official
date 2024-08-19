# ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**project_id** | **str** |  | 
**user** | [**ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInnerUser**](ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInnerUser.md) |  | 
**roles** | [**List[ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner]**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner import ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner from a JSON string
api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner_instance = ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner_dict = api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner from a dict
api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner_from_dict = ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner.from_dict(api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


