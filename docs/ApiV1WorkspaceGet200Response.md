# ApiV1WorkspaceGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[ApiV1WorkspaceGet200ResponseWorkspacesInner]**](ApiV1WorkspaceGet200ResponseWorkspacesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_get200_response import ApiV1WorkspaceGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceGet200Response from a JSON string
api_v1_workspace_get200_response_instance = ApiV1WorkspaceGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceGet200Response.to_json()

# convert the object into a dict
api_v1_workspace_get200_response_dict = api_v1_workspace_get200_response_instance.to_dict()
# create an instance of ApiV1WorkspaceGet200Response from a dict
api_v1_workspace_get200_response_from_dict = ApiV1WorkspaceGet200Response.from_dict(api_v1_workspace_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


