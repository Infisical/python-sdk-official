# ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Describe what action an entity can take. Possible actions: create, edit, delete, and read | 
**subject** | **str** | The entity this permission pertains to. Possible options: secrets, environments | 
**conditions** | [**ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions**](ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_post_request_permissions_inner import ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner from a JSON string
api_v1_workspace_project_slug_roles_post_request_permissions_inner_instance = ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.to_json()

# convert the object into a dict
api_v1_workspace_project_slug_roles_post_request_permissions_inner_dict = api_v1_workspace_project_slug_roles_post_request_permissions_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner from a dict
api_v1_workspace_project_slug_roles_post_request_permissions_inner_from_dict = ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.from_dict(api_v1_workspace_project_slug_roles_post_request_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


