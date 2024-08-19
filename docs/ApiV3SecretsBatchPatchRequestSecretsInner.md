# ApiV3SecretsBatchPatchRequestSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_name** | **str** |  | 
**type** | **str** |  | [optional] [default to 'shared']
**secret_value_ciphertext** | **str** |  | 
**secret_value_iv** | **str** |  | 
**secret_value_tag** | **str** |  | 
**secret_key_ciphertext** | **str** |  | 
**secret_key_iv** | **str** |  | 
**secret_key_tag** | **str** |  | 
**secret_comment_ciphertext** | **str** |  | [optional] 
**secret_comment_iv** | **str** |  | [optional] 
**secret_comment_tag** | **str** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_patch_request_secrets_inner import ApiV3SecretsBatchPatchRequestSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchPatchRequestSecretsInner from a JSON string
api_v3_secrets_batch_patch_request_secrets_inner_instance = ApiV3SecretsBatchPatchRequestSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchPatchRequestSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_batch_patch_request_secrets_inner_dict = api_v3_secrets_batch_patch_request_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsBatchPatchRequestSecretsInner from a dict
api_v3_secrets_batch_patch_request_secrets_inner_from_dict = ApiV3SecretsBatchPatchRequestSecretsInner.from_dict(api_v3_secrets_batch_patch_request_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


