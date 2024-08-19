# ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role slug to assign to the newly created identity project membership. | 
**is_temporary** | **bool** | Whether the assigned role is temporary. If isTemporary is set true, must provide temporaryMode, temporaryRange and temporaryAccessStartTime. | [optional] [default to False]

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf from a JSON string
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of_instance = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf.to_json()

# convert the object into a dict
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of_dict = api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf from a dict
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of_from_dict = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInnerAnyOf.from_dict(api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


