# ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions

When specified, only matching conditions will be allowed to access given resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The environment slug this permission should allow. | [optional] 
**secret_path** | [**ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditionsSecretPath**](ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditionsSecretPath.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions import ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions from a JSON string
api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions_instance = ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions.to_json()

# convert the object into a dict
api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions_dict = api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions from a dict
api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions_from_dict = ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditions.from_dict(api_v1_workspace_project_slug_roles_post_request_permissions_inner_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


