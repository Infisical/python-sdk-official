# ApiV3WorkspacesProjectIdSecretsNamesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets_to_update** | [**List[ApiV3WorkspacesProjectIdSecretsNamesPostRequestSecretsToUpdateInner]**](ApiV3WorkspacesProjectIdSecretsNamesPostRequestSecretsToUpdateInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_workspaces_project_id_secrets_names_post_request import ApiV3WorkspacesProjectIdSecretsNamesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3WorkspacesProjectIdSecretsNamesPostRequest from a JSON string
api_v3_workspaces_project_id_secrets_names_post_request_instance = ApiV3WorkspacesProjectIdSecretsNamesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3WorkspacesProjectIdSecretsNamesPostRequest.to_json()

# convert the object into a dict
api_v3_workspaces_project_id_secrets_names_post_request_dict = api_v3_workspaces_project_id_secrets_names_post_request_instance.to_dict()
# create an instance of ApiV3WorkspacesProjectIdSecretsNamesPostRequest from a dict
api_v3_workspaces_project_id_secrets_names_post_request_from_dict = ApiV3WorkspacesProjectIdSecretsNamesPostRequest.from_dict(api_v3_workspaces_project_id_secrets_names_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


