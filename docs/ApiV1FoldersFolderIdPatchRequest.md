# ApiV1FoldersFolderIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project where the folder is located. | 
**environment** | **str** | The slug of the environment where the folder is located. | 
**name** | **str** | The new name of the folder. | 
**path** | **str** | The path of the folder to update. | [optional] [default to '/']
**directory** | **str** | The new directory of the folder to update. (Deprecated in favor of path) | [optional] [default to '/']

## Example

```python
from infisicalapi_client.models.api_v1_folders_folder_id_patch_request import ApiV1FoldersFolderIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FoldersFolderIdPatchRequest from a JSON string
api_v1_folders_folder_id_patch_request_instance = ApiV1FoldersFolderIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1FoldersFolderIdPatchRequest.to_json()

# convert the object into a dict
api_v1_folders_folder_id_patch_request_dict = api_v1_folders_folder_id_patch_request_instance.to_dict()
# create an instance of ApiV1FoldersFolderIdPatchRequest from a dict
api_v1_folders_folder_id_patch_request_from_dict = ApiV1FoldersFolderIdPatchRequest.from_dict(api_v1_folders_folder_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


