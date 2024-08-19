# ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The slug of the role. | [optional] 
**name** | **str** | The name of the role. | [optional] 
**permissions** | [**List[ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner]**](ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.md) | The permissions assigned to the role. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_role_id_patch_request import ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest from a JSON string
api_v1_workspace_project_slug_roles_role_id_patch_request_instance = ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest.to_json()

# convert the object into a dict
api_v1_workspace_project_slug_roles_role_id_patch_request_dict = api_v1_workspace_project_slug_roles_role_id_patch_request_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest from a dict
api_v1_workspace_project_slug_roles_role_id_patch_request_from_dict = ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest.from_dict(api_v1_workspace_project_slug_roles_role_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


