# ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**slug** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**project_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_get200_response_roles_inner import ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner from a JSON string
api_v1_workspace_project_slug_roles_get200_response_roles_inner_instance = ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner.to_json()

# convert the object into a dict
api_v1_workspace_project_slug_roles_get200_response_roles_inner_dict = api_v1_workspace_project_slug_roles_get200_response_roles_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner from a dict
api_v1_workspace_project_slug_roles_get200_response_roles_inner_from_dict = ApiV1WorkspaceProjectSlugRolesGet200ResponseRolesInner.from_dict(api_v1_workspace_project_slug_roles_get200_response_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


