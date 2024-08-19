# ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The new slug of the environment. | [optional] 
**name** | **str** | The new name of the environment. | [optional] 
**position** | **float** | The new position of the environment. The lowest number will be displayed as the first environment. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_environments_id_patch_request import ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest from a JSON string
api_v1_workspace_workspace_id_environments_id_patch_request_instance = ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_environments_id_patch_request_dict = api_v1_workspace_workspace_id_environments_id_patch_request_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest from a dict
api_v1_workspace_workspace_id_environments_id_patch_request_from_dict = ApiV1WorkspaceWorkspaceIdEnvironmentsIdPatchRequest.from_dict(api_v1_workspace_workspace_id_environments_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


