# ApiV3SecretsSecretNamePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**environment** | **str** |  | 
**type** | **str** |  | [optional] [default to 'shared']
**secret_path** | **str** |  | [optional] [default to '/']
**secret_key_ciphertext** | **str** |  | 
**secret_key_iv** | **str** |  | 
**secret_key_tag** | **str** |  | 
**secret_value_ciphertext** | **str** |  | 
**secret_value_iv** | **str** |  | 
**secret_value_tag** | **str** |  | 
**secret_comment_ciphertext** | **str** |  | [optional] 
**secret_comment_iv** | **str** |  | [optional] 
**secret_comment_tag** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_secret_name_post_request import ApiV3SecretsSecretNamePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsSecretNamePostRequest from a JSON string
api_v3_secrets_secret_name_post_request_instance = ApiV3SecretsSecretNamePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsSecretNamePostRequest.to_json()

# convert the object into a dict
api_v3_secrets_secret_name_post_request_dict = api_v3_secrets_secret_name_post_request_instance.to_dict()
# create an instance of ApiV3SecretsSecretNamePostRequest from a dict
api_v3_secrets_secret_name_post_request_from_dict = ApiV3SecretsSecretNamePostRequest.from_dict(api_v3_secrets_secret_name_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


