# ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**is_temporary** | **bool** |  | 
**temporary_mode** | **str** |  | 
**temporary_range** | **str** |  | 
**temporary_access_start_time** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner import ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner from a JSON string
api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner_instance = ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner_dict = api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner from a dict
api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner_from_dict = ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner.from_dict(api_v1_workspace_workspace_id_memberships_membership_id_patch_request_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


