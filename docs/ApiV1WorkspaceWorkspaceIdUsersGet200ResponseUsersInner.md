# ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**project_id** | **str** |  | 
**user** | [**ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser.md) |  | 
**project** | [**ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerProject**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerProject.md) |  | 
**roles** | [**List[ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner]**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_users_get200_response_users_inner import ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner from a JSON string
api_v1_workspace_workspace_id_users_get200_response_users_inner_instance = ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_users_get200_response_users_inner_dict = api_v1_workspace_workspace_id_users_get200_response_users_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner from a dict
api_v1_workspace_workspace_id_users_get200_response_users_inner_from_dict = ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInner.from_dict(api_v1_workspace_workspace_id_users_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


