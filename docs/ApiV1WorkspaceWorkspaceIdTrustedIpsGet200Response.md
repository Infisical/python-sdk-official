# ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trusted_ips** | [**List[ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner]**](ApiV1WorkspaceWorkspaceIdTrustedIpsGet200ResponseTrustedIpsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_workspace_id_trusted_ips_get200_response import ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response from a JSON string
api_v1_workspace_workspace_id_trusted_ips_get200_response_instance = ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response.to_json()

# convert the object into a dict
api_v1_workspace_workspace_id_trusted_ips_get200_response_dict = api_v1_workspace_workspace_id_trusted_ips_get200_response_instance.to_dict()
# create an instance of ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response from a dict
api_v1_workspace_workspace_id_trusted_ips_get200_response_from_dict = ApiV1WorkspaceWorkspaceIdTrustedIpsGet200Response.from_dict(api_v1_workspace_workspace_id_trusted_ips_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


