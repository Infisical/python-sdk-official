# ApiV3SecretsBatchRawPost200ResponseAnyOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner]**](ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_post200_response_any_of import ApiV3SecretsBatchRawPost200ResponseAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawPost200ResponseAnyOf from a JSON string
api_v3_secrets_batch_raw_post200_response_any_of_instance = ApiV3SecretsBatchRawPost200ResponseAnyOf.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawPost200ResponseAnyOf.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_post200_response_any_of_dict = api_v3_secrets_batch_raw_post200_response_any_of_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawPost200ResponseAnyOf from a dict
api_v3_secrets_batch_raw_post200_response_any_of_from_dict = ApiV3SecretsBatchRawPost200ResponseAnyOf.from_dict(api_v3_secrets_batch_raw_post200_response_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


