# ApiV3SecretsRawGet200ResponseImportsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_path** | **str** |  | 
**environment** | **str** |  | 
**folder_id** | **str** |  | [optional] 
**secrets** | [**List[ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner]**](ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_get200_response_imports_inner import ApiV3SecretsRawGet200ResponseImportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawGet200ResponseImportsInner from a JSON string
api_v3_secrets_raw_get200_response_imports_inner_instance = ApiV3SecretsRawGet200ResponseImportsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawGet200ResponseImportsInner.to_json()

# convert the object into a dict
api_v3_secrets_raw_get200_response_imports_inner_dict = api_v3_secrets_raw_get200_response_imports_inner_instance.to_dict()
# create an instance of ApiV3SecretsRawGet200ResponseImportsInner from a dict
api_v3_secrets_raw_get200_response_imports_inner_from_dict = ApiV3SecretsRawGet200ResponseImportsInner.from_dict(api_v3_secrets_raw_get200_response_imports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


