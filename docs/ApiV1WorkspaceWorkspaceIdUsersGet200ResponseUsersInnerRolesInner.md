# ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 
**custom_role_id** | **str** |  | [optional] 
**custom_role_name** | **str** |  | [optional] 
**custom_role_slug** | **str** |  | [optional] 
**is_temporary** | **bool** |  | 
**temporary_mode** | **str** |  | [optional] 
**temporary_range** | **str** |  | [optional] 
**temporary_access_start_time** | **datetime** |  | [optional] 
**temporary_access_end_time** | **datetime** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner import ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner from a JSON string
api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner_instance = ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner_dict = api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner from a dict
api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner_from_dict = ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.from_dict(api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


