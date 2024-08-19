# ApiV1WorkspaceProjectIdTagsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The slug of the tag to create. | 
**color** | **str** | The color of the tag to create. | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_id_tags_post_request import ApiV1WorkspaceProjectIdTagsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectIdTagsPostRequest from a JSON string
api_v1_workspace_project_id_tags_post_request_instance = ApiV1WorkspaceProjectIdTagsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectIdTagsPostRequest.to_json()

# convert the object into a dict
api_v1_workspace_project_id_tags_post_request_dict = api_v1_workspace_project_id_tags_post_request_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectIdTagsPostRequest from a dict
api_v1_workspace_project_id_tags_post_request_from_dict = ApiV1WorkspaceProjectIdTagsPostRequest.from_dict(api_v1_workspace_project_id_tags_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


