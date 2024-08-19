# ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**scopes** | **object** |  | [optional] 
**permissions** | **List[str]** |  | 
**last_used** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** |  | 
**project_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_service_token_data_get200_response_service_token_data_inner import ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner from a JSON string
api_v1_workspace_workspace_id_service_token_data_get200_response_service_token_data_inner_instance = ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_service_token_data_get200_response_service_token_data_inner_dict = api_v1_workspace_workspace_id_service_token_data_get200_response_service_token_data_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner from a dict
api_v1_workspace_workspace_id_service_token_data_get200_response_service_token_data_inner_from_dict = ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner.from_dict(api_v1_workspace_workspace_id_service_token_data_get200_response_service_token_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


