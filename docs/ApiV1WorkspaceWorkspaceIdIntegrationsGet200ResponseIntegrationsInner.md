# ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_active** | **bool** |  | 
**url** | **str** |  | [optional] 
**app** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**target_environment** | **str** |  | [optional] 
**target_environment_id** | **str** |  | [optional] 
**target_service** | **str** |  | [optional] 
**target_service_id** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**integration** | **str** |  | 
**metadata** | **object** |  | [optional] 
**integration_auth_id** | **str** |  | 
**env_id** | **str** |  | 
**secret_path** | **str** |  | [optional] [default to '/']
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_used** | **datetime** |  | [optional] 
**is_synced** | **bool** |  | [optional] 
**sync_message** | **str** |  | [optional] 
**last_sync_job_id** | **str** |  | [optional] 
**environment** | [**ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_integrations_get200_response_integrations_inner import ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner from a JSON string
api_v1_workspace_workspace_id_integrations_get200_response_integrations_inner_instance = ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_integrations_get200_response_integrations_inner_dict = api_v1_workspace_workspace_id_integrations_get200_response_integrations_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner from a dict
api_v1_workspace_workspace_id_integrations_get200_response_integrations_inner_from_dict = ApiV1WorkspaceWorkspaceIdIntegrationsGet200ResponseIntegrationsInner.from_dict(api_v1_workspace_workspace_id_integrations_get200_response_integrations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


