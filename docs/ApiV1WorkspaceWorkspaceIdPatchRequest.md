# ApiV1WorkspaceWorkspaceIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the project. | [optional] 
**auto_capitalization** | **bool** | Disable or enable auto-capitalization for the project. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_patch_request import ApiV1WorkspaceWorkspaceIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdPatchRequest from a JSON string
api_v1_workspace_workspace_id_patch_request_instance = ApiV1WorkspaceWorkspaceIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdPatchRequest.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_patch_request_dict = api_v1_workspace_workspace_id_patch_request_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdPatchRequest from a dict
api_v1_workspace_workspace_id_patch_request_from_dict = ApiV1WorkspaceWorkspaceIdPatchRequest.from_dict(api_v1_workspace_workspace_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


