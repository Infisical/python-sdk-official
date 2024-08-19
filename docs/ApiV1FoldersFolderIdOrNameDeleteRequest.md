# ApiV1FoldersFolderIdOrNameDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project to delete the folder from. | 
**environment** | **str** | The slug of the environment where the folder is located. | 
**path** | **str** | The path of the folder to delete. | [optional] [default to '/']
**directory** | **str** | The directory of the folder to delete. (Deprecated in favor of path) | [optional] [default to '/']

## Example

```python
from infisicalapi_client.models.api_v1_folders_folder_id_or_name_delete_request import ApiV1FoldersFolderIdOrNameDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FoldersFolderIdOrNameDeleteRequest from a JSON string
api_v1_folders_folder_id_or_name_delete_request_instance = ApiV1FoldersFolderIdOrNameDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1FoldersFolderIdOrNameDeleteRequest.to_json()

# convert the object into a dict
api_v1_folders_folder_id_or_name_delete_request_dict = api_v1_folders_folder_id_or_name_delete_request_instance.to_dict()
# create an instance of ApiV1FoldersFolderIdOrNameDeleteRequest from a dict
api_v1_folders_folder_id_or_name_delete_request_from_dict = ApiV1FoldersFolderIdOrNameDeleteRequest.from_dict(api_v1_folders_folder_id_or_name_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


