# ApiV1FoldersBatchPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project where the folder is located. | 
**folders** | [**List[ApiV1FoldersBatchPatchRequestFoldersInner]**](ApiV1FoldersBatchPatchRequestFoldersInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_folders_batch_patch_request import ApiV1FoldersBatchPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FoldersBatchPatchRequest from a JSON string
api_v1_folders_batch_patch_request_instance = ApiV1FoldersBatchPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1FoldersBatchPatchRequest.to_json()

# convert the object into a dict
api_v1_folders_batch_patch_request_dict = api_v1_folders_batch_patch_request_instance.to_dict()
# create an instance of ApiV1FoldersBatchPatchRequest from a dict
api_v1_folders_batch_patch_request_from_dict = ApiV1FoldersBatchPatchRequest.from_dict(api_v1_folders_batch_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


