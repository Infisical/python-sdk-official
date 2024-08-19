# ApiV1FoldersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project to create the folder in. | 
**environment** | **str** | The slug of the environment to create the folder in. | 
**name** | **str** | The name of the folder to create. | 
**path** | **str** | The path of the folder to create. | [optional] [default to '/']
**directory** | **str** | The directory of the folder to create. (Deprecated in favor of path) | [optional] [default to '/']

## Example

```python
from infisicalapi_client.models.api_v1_folders_post_request import ApiV1FoldersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FoldersPostRequest from a JSON string
api_v1_folders_post_request_instance = ApiV1FoldersPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1FoldersPostRequest.to_json()

# convert the object into a dict
api_v1_folders_post_request_dict = api_v1_folders_post_request_instance.to_dict()
# create an instance of ApiV1FoldersPostRequest from a dict
api_v1_folders_post_request_from_dict = ApiV1FoldersPostRequest.from_dict(api_v1_folders_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


