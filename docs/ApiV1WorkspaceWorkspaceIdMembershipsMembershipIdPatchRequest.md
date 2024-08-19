# ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner]**](ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner.md) | A list of roles to update the membership to. | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_membership_id_patch_request import ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest from a JSON string
api_v1_workspace_workspace_id_memberships_membership_id_patch_request_instance = ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_memberships_membership_id_patch_request_dict = api_v1_workspace_workspace_id_memberships_membership_id_patch_request_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest from a dict
api_v1_workspace_workspace_id_memberships_membership_id_patch_request_from_dict = ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequest.from_dict(api_v1_workspace_workspace_id_memberships_membership_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


