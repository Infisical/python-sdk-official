# ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the environment to create. | 
**slug** | **str** | The slug of the environment to create. | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_environments_post_request import ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest from a JSON string
api_v1_workspace_workspace_id_environments_post_request_instance = ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_environments_post_request_dict = api_v1_workspace_workspace_id_environments_post_request_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest from a dict
api_v1_workspace_workspace_id_environments_post_request_from_dict = ApiV1WorkspaceWorkspaceIdEnvironmentsPostRequest.from_dict(api_v1_workspace_workspace_id_environments_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


