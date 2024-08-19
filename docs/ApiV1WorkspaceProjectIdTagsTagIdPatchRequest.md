# ApiV1WorkspaceProjectIdTagsTagIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The slug of the tag to update. | 
**color** | **str** | The color of the tag to update. | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_id_tags_tag_id_patch_request import ApiV1WorkspaceProjectIdTagsTagIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectIdTagsTagIdPatchRequest from a JSON string
api_v1_workspace_project_id_tags_tag_id_patch_request_instance = ApiV1WorkspaceProjectIdTagsTagIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectIdTagsTagIdPatchRequest.to_json()

# convert the object into a dict
api_v1_workspace_project_id_tags_tag_id_patch_request_dict = api_v1_workspace_project_id_tags_tag_id_patch_request_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectIdTagsTagIdPatchRequest from a dict
api_v1_workspace_project_id_tags_tag_id_patch_request_from_dict = ApiV1WorkspaceProjectIdTagsTagIdPatchRequest.from_dict(api_v1_workspace_project_id_tags_tag_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


