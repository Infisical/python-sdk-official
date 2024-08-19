# ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**id** | **str** |  | 
**workspace** | **str** |  | 
**environment** | **str** |  | 
**version** | **float** |  | 
**type** | **str** |  | 
**secret_key** | **str** |  | 
**secret_value** | **str** |  | 
**secret_comment** | **str** |  | 
**secret_reminder_note** | **str** |  | [optional] 
**secret_reminder_repeat_days** | **float** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] [default to False]
**metadata** | **object** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_raw_get200_response_imports_inner_secrets_inner import ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner from a JSON string
api_v3_secrets_raw_get200_response_imports_inner_secrets_inner_instance = ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_raw_get200_response_imports_inner_secrets_inner_dict = api_v3_secrets_raw_get200_response_imports_inner_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner from a dict
api_v3_secrets_raw_get200_response_imports_inner_secrets_inner_from_dict = ApiV3SecretsRawGet200ResponseImportsInnerSecretsInner.from_dict(api_v3_secrets_raw_get200_response_imports_inner_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


