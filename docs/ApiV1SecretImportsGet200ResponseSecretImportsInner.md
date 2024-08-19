# ApiV1SecretImportsGet200ResponseSecretImportsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **float** |  | [optional] [default to 1]
**import_path** | **str** |  | 
**position** | **float** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**folder_id** | **str** |  | 
**is_replication** | **bool** |  | [optional] [default to False]
**is_replication_success** | **bool** |  | [optional] 
**replication_status** | **str** |  | [optional] 
**last_replicated** | **datetime** |  | [optional] 
**is_reserved** | **bool** |  | [optional] [default to False]
**import_env** | [**ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv**](ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_imports_get200_response_secret_imports_inner import ApiV1SecretImportsGet200ResponseSecretImportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretImportsGet200ResponseSecretImportsInner from a JSON string
api_v1_secret_imports_get200_response_secret_imports_inner_instance = ApiV1SecretImportsGet200ResponseSecretImportsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretImportsGet200ResponseSecretImportsInner.to_json()

# convert the object into a dict
api_v1_secret_imports_get200_response_secret_imports_inner_dict = api_v1_secret_imports_get200_response_secret_imports_inner_instance.to_dict()
# create an instance of ApiV1SecretImportsGet200ResponseSecretImportsInner from a dict
api_v1_secret_imports_get200_response_secret_imports_inner_from_dict = ApiV1SecretImportsGet200ResponseSecretImportsInner.from_dict(api_v1_secret_imports_get200_response_secret_imports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


