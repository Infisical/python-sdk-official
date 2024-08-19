# ApiV2WorkspacePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_name** | **str** | The name of the project to create. | 
**slug** | **str** | An optional slug for the project. | [optional] 
**kms_key_id** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_post_request import ApiV2WorkspacePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspacePostRequest from a JSON string
api_v2_workspace_post_request_instance = ApiV2WorkspacePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspacePostRequest.to_json()

# convert the object into a dict
api_v2_workspace_post_request_dict = api_v2_workspace_post_request_instance.to_dict()
# create an instance of ApiV2WorkspacePostRequest from a dict
api_v2_workspace_post_request_from_dict = ApiV2WorkspacePostRequest.from_dict(api_v2_workspace_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


