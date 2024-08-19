# ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner]**](ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner.md) | A list of role slugs to assign to the identity project membership. | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_patch_request import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest from a JSON string
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_instance = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest.to_json()

# convert the object into a dict
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_dict = api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest from a dict
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_from_dict = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequest.from_dict(api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


