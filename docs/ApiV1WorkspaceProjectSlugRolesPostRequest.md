# ApiV1WorkspaceProjectSlugRolesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The slug of the role. | 
**name** | **str** | The name of the role. | 
**description** | **str** | The description for the role. | [optional] 
**permissions** | [**List[ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner]**](ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.md) | The permissions assigned to the role. | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_post_request import ApiV1WorkspaceProjectSlugRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectSlugRolesPostRequest from a JSON string
api_v1_workspace_project_slug_roles_post_request_instance = ApiV1WorkspaceProjectSlugRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectSlugRolesPostRequest.to_json()

# convert the object into a dict
api_v1_workspace_project_slug_roles_post_request_dict = api_v1_workspace_project_slug_roles_post_request_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectSlugRolesPostRequest from a dict
api_v1_workspace_project_slug_roles_post_request_from_dict = ApiV1WorkspaceProjectSlugRolesPostRequest.from_dict(api_v1_workspace_project_slug_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


