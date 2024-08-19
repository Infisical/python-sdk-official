# ApiV2WorkspaceProjectIdMembershipsDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emails** | **List[str]** | A list of organization member emails to remove from the project. | [optional] [default to []]
**usernames** | **List[str]** | A list of usernames to remove from the project. | [optional] [default to []]

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_memberships_delete_request import ApiV2WorkspaceProjectIdMembershipsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdMembershipsDeleteRequest from a JSON string
api_v2_workspace_project_id_memberships_delete_request_instance = ApiV2WorkspaceProjectIdMembershipsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdMembershipsDeleteRequest.to_json()

# convert the object into a dict
api_v2_workspace_project_id_memberships_delete_request_dict = api_v2_workspace_project_id_memberships_delete_request_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdMembershipsDeleteRequest from a dict
api_v2_workspace_project_id_memberships_delete_request_from_dict = ApiV2WorkspaceProjectIdMembershipsDeleteRequest.from_dict(api_v2_workspace_project_id_memberships_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


