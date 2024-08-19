# ApiV1SecretImportsPostRequestImport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The slug of the environment to import from. | 
**path** | **str** | The path to import from. | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_post_request_import import ApiV1SecretImportsPostRequestImport

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsPostRequestImport from a JSON string
api_v1_secret_imports_post_request_import_instance = ApiV1SecretImportsPostRequestImport.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsPostRequestImport.to_json()

# convert the object into a dict
api_v1_secret_imports_post_request_import_dict = api_v1_secret_imports_post_request_import_instance.to_dict()
# create an instance of ApiV1SecretImportsPostRequestImport from a dict
api_v1_secret_imports_post_request_import_from_dict = ApiV1SecretImportsPostRequestImport.from_dict(api_v1_secret_imports_post_request_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


