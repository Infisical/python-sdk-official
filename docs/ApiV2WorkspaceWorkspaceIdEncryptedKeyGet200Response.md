# ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**encrypted_key** | **str** |  | 
**nonce** | **str** |  | 
**receiver_id** | **str** |  | 
**sender_id** | **str** |  | [optional] 
**project_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**sender** | [**ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200ResponseSender**](ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200ResponseSender.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_workspace_id_encrypted_key_get200_response import ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response from a JSON string
api_v2_workspace_workspace_id_encrypted_key_get200_response_instance = ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response.to_json()

# convert the object into a dict
api_v2_workspace_workspace_id_encrypted_key_get200_response_dict = api_v2_workspace_workspace_id_encrypted_key_get200_response_instance.to_dict()
# create an instance of ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response from a dict
api_v2_workspace_workspace_id_encrypted_key_get200_response_from_dict = ApiV2WorkspaceWorkspaceIdEncryptedKeyGet200Response.from_dict(api_v2_workspace_workspace_id_encrypted_key_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


