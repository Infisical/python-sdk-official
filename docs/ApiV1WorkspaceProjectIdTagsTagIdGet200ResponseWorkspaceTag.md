# ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag


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
**name** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_id_tags_tag_id_get200_response_workspace_tag import ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag from a JSON string
api_v1_workspace_project_id_tags_tag_id_get200_response_workspace_tag_instance = ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag.to_json()

# convert the object into a dict
api_v1_workspace_project_id_tags_tag_id_get200_response_workspace_tag_dict = api_v1_workspace_project_id_tags_tag_id_get200_response_workspace_tag_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag from a dict
api_v1_workspace_project_id_tags_tag_id_get200_response_workspace_tag_from_dict = ApiV1WorkspaceProjectIdTagsTagIdGet200ResponseWorkspaceTag.from_dict(api_v1_workspace_project_id_tags_tag_id_get200_response_workspace_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


