# ApiV3SecretsBatchDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**environment** | **str** |  | 
**secret_path** | **str** |  | [optional] [default to '/']
**secrets** | [**List[ApiV3SecretsBatchDeleteRequestSecretsInner]**](ApiV3SecretsBatchDeleteRequestSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_delete_request import ApiV3SecretsBatchDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchDeleteRequest from a JSON string
api_v3_secrets_batch_delete_request_instance = ApiV3SecretsBatchDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchDeleteRequest.to_json()

# convert the object into a dict
api_v3_secrets_batch_delete_request_dict = api_v3_secrets_batch_delete_request_instance.to_dict()
# create an instance of ApiV3SecretsBatchDeleteRequest from a dict
api_v3_secrets_batch_delete_request_from_dict = ApiV3SecretsBatchDeleteRequest.from_dict(api_v3_secrets_batch_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


