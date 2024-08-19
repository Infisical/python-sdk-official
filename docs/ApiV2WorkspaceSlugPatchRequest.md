# ApiV2WorkspaceSlugPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the project. | [optional] 
**auto_capitalization** | **bool** | The new auto-capitalization setting. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_slug_patch_request import ApiV2WorkspaceSlugPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceSlugPatchRequest from a JSON string
api_v2_workspace_slug_patch_request_instance = ApiV2WorkspaceSlugPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceSlugPatchRequest.to_json()

# convert the object into a dict
api_v2_workspace_slug_patch_request_dict = api_v2_workspace_slug_patch_request_instance.to_dict()
# create an instance of ApiV2WorkspaceSlugPatchRequest from a dict
api_v2_workspace_slug_patch_request_from_dict = ApiV2WorkspaceSlugPatchRequest.from_dict(api_v2_workspace_slug_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


