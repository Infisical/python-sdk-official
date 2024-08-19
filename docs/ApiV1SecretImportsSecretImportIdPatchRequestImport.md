# ApiV1SecretImportsSecretImportIdPatchRequestImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The new environment slug to import from. | [optional] 
**path** | **str** | The new path to import from. | [optional] 
**position** | **float** | The new position of the secret import. The lowest number will be displayed as the first import. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_secret_import_id_patch_request_import import ApiV1SecretImportsSecretImportIdPatchRequestImport

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsSecretImportIdPatchRequestImport from a JSON string
api_v1_secret_imports_secret_import_id_patch_request_import_instance = ApiV1SecretImportsSecretImportIdPatchRequestImport.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsSecretImportIdPatchRequestImport.to_json()

# convert the object into a dict
api_v1_secret_imports_secret_import_id_patch_request_import_dict = api_v1_secret_imports_secret_import_id_patch_request_import_instance.to_dict()
# create an instance of ApiV1SecretImportsSecretImportIdPatchRequestImport from a dict
api_v1_secret_imports_secret_import_id_patch_request_import_from_dict = ApiV1SecretImportsSecretImportIdPatchRequestImport.from_dict(api_v1_secret_imports_secret_import_id_patch_request_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


