# ApiV1WorkspaceWorkspaceIdMembershipsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner]**](ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_post_request import ApiV1WorkspaceWorkspaceIdMembershipsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsPostRequest from a JSON string
api_v1_workspace_workspace_id_memberships_post_request_instance = ApiV1WorkspaceWorkspaceIdMembershipsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdMembershipsPostRequest.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_memberships_post_request_dict = api_v1_workspace_workspace_id_memberships_post_request_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsPostRequest from a dict
api_v1_workspace_workspace_id_memberships_post_request_from_dict = ApiV1WorkspaceWorkspaceIdMembershipsPostRequest.from_dict(api_v1_workspace_workspace_id_memberships_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


