# ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_membership_id** | **str** |  | 
**workspace_encrypted_key** | **str** |  | 
**workspace_encrypted_nonce** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_post_request_members_inner import ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner from a JSON string
api_v1_workspace_workspace_id_memberships_post_request_members_inner_instance = ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_memberships_post_request_members_inner_dict = api_v1_workspace_workspace_id_memberships_post_request_members_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner from a dict
api_v1_workspace_workspace_id_memberships_post_request_members_inner_from_dict = ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner.from_dict(api_v1_workspace_workspace_id_memberships_post_request_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


