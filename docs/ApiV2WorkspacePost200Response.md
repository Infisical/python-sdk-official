# ApiV2WorkspacePost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**ApiV1WorkspaceGet200ResponseWorkspacesInner**](ApiV1WorkspaceGet200ResponseWorkspacesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_post200_response import ApiV2WorkspacePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspacePost200Response from a JSON string
api_v2_workspace_post200_response_instance = ApiV2WorkspacePost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspacePost200Response.to_json()

# convert the object into a dict
api_v2_workspace_post200_response_dict = api_v2_workspace_post200_response_instance.to_dict()
# create an instance of ApiV2WorkspacePost200Response from a dict
api_v2_workspace_post200_response_from_dict = ApiV2WorkspacePost200Response.from_dict(api_v2_workspace_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


