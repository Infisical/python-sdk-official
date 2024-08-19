# ApiV2WorkspaceProjectIdMembershipsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | A list of organization member emails to invite to the project. | [optional] [default to []]
**usernames** | **List[str]** | A list of usernames to invite to the project. | [optional] [default to []]

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_memberships_post_request import ApiV2WorkspaceProjectIdMembershipsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdMembershipsPostRequest from a JSON string
api_v2_workspace_project_id_memberships_post_request_instance = ApiV2WorkspaceProjectIdMembershipsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdMembershipsPostRequest.to_json()

# convert the object into a dict
api_v2_workspace_project_id_memberships_post_request_dict = api_v2_workspace_project_id_memberships_post_request_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdMembershipsPostRequest from a dict
api_v2_workspace_project_id_memberships_post_request_from_dict = ApiV2WorkspaceProjectIdMembershipsPostRequest.from_dict(api_v2_workspace_project_id_memberships_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


