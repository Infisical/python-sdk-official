# ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**integration** | **str** |  | 
**team_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner import ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner from a JSON string
api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner_instance = ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner_dict = api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner from a dict
api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner_from_dict = ApiV1WorkspaceWorkspaceIdAuthorizationsGet200ResponseAuthorizationsInner.from_dict(api_v1_workspace_workspace_id_authorizations_get200_response_authorizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


