# ApiV3SecretsBatchRawPostRequestSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | The name of the secret to create. | 
**secret_value** | **str** | The value of the secret to create. | 
**secret_comment** | **str** | Attach a comment to the secret. | [optional] [default to '']
**skip_multiline_encoding** | **bool** | Skip multiline encoding for the secret value. | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**tag_ids** | **List[str]** | The ID of the tags to be attached to the created secret. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_post_request_secrets_inner import ApiV3SecretsBatchRawPostRequestSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawPostRequestSecretsInner from a JSON string
api_v3_secrets_batch_raw_post_request_secrets_inner_instance = ApiV3SecretsBatchRawPostRequestSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawPostRequestSecretsInner.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_post_request_secrets_inner_dict = api_v3_secrets_batch_raw_post_request_secrets_inner_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawPostRequestSecretsInner from a dict
api_v3_secrets_batch_raw_post_request_secrets_inner_from_dict = ApiV3SecretsBatchRawPostRequestSecretsInner.from_dict(api_v3_secrets_batch_raw_post_request_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


