# ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**user_agent_type** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**org_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**event** | [**ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInnerEvent**](ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInnerEvent.md) |  | 
**actor** | [**ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInnerEvent**](ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInnerEvent.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_audit_logs_get200_response_audit_logs_inner import ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner from a JSON string
api_v1_workspace_workspace_id_audit_logs_get200_response_audit_logs_inner_instance = ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_audit_logs_get200_response_audit_logs_inner_dict = api_v1_workspace_workspace_id_audit_logs_get200_response_audit_logs_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner from a dict
api_v1_workspace_workspace_id_audit_logs_get200_response_audit_logs_inner_from_dict = ApiV1WorkspaceWorkspaceIdAuditLogsGet200ResponseAuditLogsInner.from_dict(api_v1_workspace_workspace_id_audit_logs_get200_response_audit_logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


