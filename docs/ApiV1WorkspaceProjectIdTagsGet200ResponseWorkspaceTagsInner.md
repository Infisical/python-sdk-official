# ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**slug** | **str** |  | 
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** |  | [optional] 
**project_id** | **str** |  | 
**created_by_actor_type** | **str** |  | [optional] [default to 'user']

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner import ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner from a JSON string
api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner_instance = ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner.to_json()

# convert the object into a dict
api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner_dict = api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner from a dict
api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner_from_dict = ApiV1WorkspaceProjectIdTagsGet200ResponseWorkspaceTagsInner.from_dict(api_v1_workspace_project_id_tags_get200_response_workspace_tags_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


