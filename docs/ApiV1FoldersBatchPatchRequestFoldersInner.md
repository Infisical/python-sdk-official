# ApiV1FoldersBatchPatchRequestFoldersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the folder to update. | 
**environment** | **str** | The slug of the environment where the folder is located. | 
**name** | **str** | The new name of the folder. | 
**path** | **str** | The path of the folder to update. | [optional] [default to '/']

## Example

```python
from infisicalapi_client.models.api_v1_folders_batch_patch_request_folders_inner import ApiV1FoldersBatchPatchRequestFoldersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FoldersBatchPatchRequestFoldersInner from a JSON string
api_v1_folders_batch_patch_request_folders_inner_instance = ApiV1FoldersBatchPatchRequestFoldersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1FoldersBatchPatchRequestFoldersInner.to_json()

# convert the object into a dict
api_v1_folders_batch_patch_request_folders_inner_dict = api_v1_folders_batch_patch_request_folders_inner_instance.to_dict()
# create an instance of ApiV1FoldersBatchPatchRequestFoldersInner from a dict
api_v1_folders_batch_patch_request_folders_inner_from_dict = ApiV1FoldersBatchPatchRequestFoldersInner.from_dict(api_v1_folders_batch_patch_request_folders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


