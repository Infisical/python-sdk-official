# ApiV1WorkspaceGet200ResponseWorkspacesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**auto_capitalization** | **bool** |  | [optional] [default to True]
**org_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**version** | **float** |  | [optional] [default to 1]
**upgrade_status** | **str** |  | [optional] 
**pit_version_limit** | **float** |  | [optional] [default to 10]
**kms_certificate_key_id** | **str** |  | [optional] 
**audit_logs_retention_days** | **float** |  | [optional] 
**id** | **str** |  | 
**environments** | [**List[ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv]**](ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_get200_response_workspaces_inner import ApiV1WorkspaceGet200ResponseWorkspacesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceGet200ResponseWorkspacesInner from a JSON string
api_v1_workspace_get200_response_workspaces_inner_instance = ApiV1WorkspaceGet200ResponseWorkspacesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceGet200ResponseWorkspacesInner.to_json()

# convert the object into a dict
api_v1_workspace_get200_response_workspaces_inner_dict = api_v1_workspace_get200_response_workspaces_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceGet200ResponseWorkspacesInner from a dict
api_v1_workspace_get200_response_workspaces_inner_from_dict = ApiV1WorkspaceGet200ResponseWorkspacesInner.from_dict(api_v1_workspace_get200_response_workspaces_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


