# ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ip_address** | **str** |  | 
**type** | **str** |  | 
**prefix** | **float** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**comment** | **str** |  | [optional] 
**project_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner import ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner from a JSON string
api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner_instance = ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner_dict = api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner from a dict
api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner_from_dict = ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner.from_dict(api_v1_workspace_workspace_id_trusted_ips_get200_response_trusted_ips_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


