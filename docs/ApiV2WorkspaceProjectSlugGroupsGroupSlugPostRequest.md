# ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role for the group to assume in the project. | [optional] [default to 'no-access']

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_slug_groups_group_slug_post_request import ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest from a JSON string
api_v2_workspace_project_slug_groups_group_slug_post_request_instance = ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest.to_json()

# convert the object into a dict
api_v2_workspace_project_slug_groups_group_slug_post_request_dict = api_v2_workspace_project_slug_groups_group_slug_post_request_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest from a dict
api_v2_workspace_project_slug_groups_group_slug_post_request_from_dict = ApiV2WorkspaceProjectSlugGroupsGroupSlugPostRequest.from_dict(api_v2_workspace_project_slug_groups_group_slug_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


