# ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | 
**comment** | **str** |  | [optional] [default to '']
**is_active** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_trusted_ips_post_request import ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest from a JSON string
api_v1_workspace_workspace_id_trusted_ips_post_request_instance = ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_trusted_ips_post_request_dict = api_v1_workspace_workspace_id_trusted_ips_post_request_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest from a dict
api_v1_workspace_workspace_id_trusted_ips_post_request_from_dict = ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest.from_dict(api_v1_workspace_workspace_id_trusted_ips_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


