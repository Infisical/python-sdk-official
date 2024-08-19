# ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**username** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**id** | **str** |  | 
**public_key** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_users_get200_response_users_inner_user import ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser from a JSON string
api_v1_workspace_workspace_id_users_get200_response_users_inner_user_instance = ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_users_get200_response_users_inner_user_dict = api_v1_workspace_workspace_id_users_get200_response_users_inner_user_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser from a dict
api_v1_workspace_workspace_id_users_get200_response_users_inner_user_from_dict = ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerUser.from_dict(api_v1_workspace_workspace_id_users_get200_response_users_inner_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


