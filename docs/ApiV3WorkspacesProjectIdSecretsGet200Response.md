# ApiV3WorkspacesProjectIdSecretsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[ApiV3WorkspacesProjectIdSecretsGet200ResponseSecretsInner]**](ApiV3WorkspacesProjectIdSecretsGet200ResponseSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_workspaces_project_id_secrets_get200_response import ApiV3WorkspacesProjectIdSecretsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3WorkspacesProjectIdSecretsGet200Response from a JSON string
api_v3_workspaces_project_id_secrets_get200_response_instance = ApiV3WorkspacesProjectIdSecretsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV3WorkspacesProjectIdSecretsGet200Response.to_json()

# convert the object into a dict
api_v3_workspaces_project_id_secrets_get200_response_dict = api_v3_workspaces_project_id_secrets_get200_response_instance.to_dict()
# create an instance of ApiV3WorkspacesProjectIdSecretsGet200Response from a dict
api_v3_workspaces_project_id_secrets_get200_response_from_dict = ApiV3WorkspacesProjectIdSecretsGet200Response.from_dict(api_v3_workspaces_project_id_secrets_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


