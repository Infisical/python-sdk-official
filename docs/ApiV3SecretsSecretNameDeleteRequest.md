# ApiV3SecretsSecretNameDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'shared']
**secret_path** | **str** |  | [optional] [default to '/']
**secret_id** | **str** |  | [optional] 
**workspace_id** | **str** |  | 
**environment** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_secret_name_delete_request import ApiV3SecretsSecretNameDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsSecretNameDeleteRequest from a JSON string
api_v3_secrets_secret_name_delete_request_instance = ApiV3SecretsSecretNameDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsSecretNameDeleteRequest.to_json()

# convert the object into a dict
api_v3_secrets_secret_name_delete_request_dict = api_v3_secrets_secret_name_delete_request_instance.to_dict()
# create an instance of ApiV3SecretsSecretNameDeleteRequest from a dict
api_v3_secrets_secret_name_delete_request_from_dict = ApiV3SecretsSecretNameDeleteRequest.from_dict(api_v3_secrets_secret_name_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


