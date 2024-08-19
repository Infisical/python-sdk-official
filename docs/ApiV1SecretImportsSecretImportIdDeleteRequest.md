# ApiV1SecretImportsSecretImportIdDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project to delete the secret import from. | 
**environment** | **str** | The slug of the environment where the secret import is located. | 
**path** | **str** | The path of the secret import to delete. | [optional] [default to '/']

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_secret_import_id_delete_request import ApiV1SecretImportsSecretImportIdDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsSecretImportIdDeleteRequest from a JSON string
api_v1_secret_imports_secret_import_id_delete_request_instance = ApiV1SecretImportsSecretImportIdDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsSecretImportIdDeleteRequest.to_json()

# convert the object into a dict
api_v1_secret_imports_secret_import_id_delete_request_dict = api_v1_secret_imports_secret_import_id_delete_request_instance.to_dict()
# create an instance of ApiV1SecretImportsSecretImportIdDeleteRequest from a dict
api_v1_secret_imports_secret_import_id_delete_request_from_dict = ApiV1SecretImportsSecretImportIdDeleteRequest.from_dict(api_v1_secret_imports_secret_import_id_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


