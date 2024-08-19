# ApiV1SecretImportsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project you are working in. | 
**environment** | **str** | The slug of the environment to import into. | 
**path** | **str** | The path to import into. | [optional] [default to '/']
**var_import** | [**ApiV1SecretImportsPostRequestImport**](ApiV1SecretImportsPostRequestImport.md) |  | 
**is_replication** | **bool** | When true, secrets from the source will be automatically sent to the destination. If approval policies exist at the destination, the secrets will be sent as approval requests instead of being applied immediately. | [optional] [default to False]

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_post_request import ApiV1SecretImportsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsPostRequest from a JSON string
api_v1_secret_imports_post_request_instance = ApiV1SecretImportsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsPostRequest.to_json()

# convert the object into a dict
api_v1_secret_imports_post_request_dict = api_v1_secret_imports_post_request_instance.to_dict()
# create an instance of ApiV1SecretImportsPostRequest from a dict
api_v1_secret_imports_post_request_from_dict = ApiV1SecretImportsPostRequest.from_dict(api_v1_secret_imports_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


