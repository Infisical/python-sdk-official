# ApiV1WorkspaceProjectSlugRolesPost200ResponseRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**slug** | **str** |  | 
**permissions** | [**List[ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInner]**](ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInner.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**project_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_post200_response_role import ApiV1WorkspaceProjectSlugRolesPost200ResponseRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectSlugRolesPost200ResponseRole from a JSON string
api_v1_workspace_project_slug_roles_post200_response_role_instance = ApiV1WorkspaceProjectSlugRolesPost200ResponseRole.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectSlugRolesPost200ResponseRole.to_json()

# convert the object into a dict
api_v1_workspace_project_slug_roles_post200_response_role_dict = api_v1_workspace_project_slug_roles_post200_response_role_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectSlugRolesPost200ResponseRole from a dict
api_v1_workspace_project_slug_roles_post200_response_role_from_dict = ApiV1WorkspaceProjectSlugRolesPost200ResponseRole.from_dict(api_v1_workspace_project_slug_roles_post200_response_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


