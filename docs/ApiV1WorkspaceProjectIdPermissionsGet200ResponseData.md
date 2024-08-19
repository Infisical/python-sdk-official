# ApiV1WorkspaceProjectIdPermissionsGet200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership** | [**ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership**](ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership.md) |  | 
**permissions** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_id_permissions_get200_response_data import ApiV1WorkspaceProjectIdPermissionsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectIdPermissionsGet200ResponseData from a JSON string
api_v1_workspace_project_id_permissions_get200_response_data_instance = ApiV1WorkspaceProjectIdPermissionsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectIdPermissionsGet200ResponseData.to_json()

# convert the object into a dict
api_v1_workspace_project_id_permissions_get200_response_data_dict = api_v1_workspace_project_id_permissions_get200_response_data_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectIdPermissionsGet200ResponseData from a dict
api_v1_workspace_project_id_permissions_get200_response_data_from_dict = ApiV1WorkspaceProjectIdPermissionsGet200ResponseData.from_dict(api_v1_workspace_project_id_permissions_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


