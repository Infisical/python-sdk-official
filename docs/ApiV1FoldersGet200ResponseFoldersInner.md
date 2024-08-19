# ApiV1FoldersGet200ResponseFoldersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**version** | **float** |  | [optional] [default to 1]
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**env_id** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**is_reserved** | **bool** |  | [optional] [default to False]

## Example

```python
from infisicalapi_client.models.api_v1_folders_get200_response_folders_inner import ApiV1FoldersGet200ResponseFoldersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FoldersGet200ResponseFoldersInner from a JSON string
api_v1_folders_get200_response_folders_inner_instance = ApiV1FoldersGet200ResponseFoldersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1FoldersGet200ResponseFoldersInner.to_json()

# convert the object into a dict
api_v1_folders_get200_response_folders_inner_dict = api_v1_folders_get200_response_folders_inner_instance.to_dict()
# create an instance of ApiV1FoldersGet200ResponseFoldersInner from a dict
api_v1_folders_get200_response_folders_inner_from_dict = ApiV1FoldersGet200ResponseFoldersInner.from_dict(api_v1_folders_get200_response_folders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


