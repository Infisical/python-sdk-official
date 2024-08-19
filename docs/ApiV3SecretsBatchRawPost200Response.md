# ApiV3SecretsBatchRawPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner]**](ApiV1SecretSecretIdSecretVersionsGet200ResponseSecretVersionsInner.md) |  | 
**approval** | [**ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval**](ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_batch_raw_post200_response import ApiV3SecretsBatchRawPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsBatchRawPost200Response from a JSON string
api_v3_secrets_batch_raw_post200_response_instance = ApiV3SecretsBatchRawPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsBatchRawPost200Response.to_json()

# convert the object into a dict
api_v3_secrets_batch_raw_post200_response_dict = api_v3_secrets_batch_raw_post200_response_instance.to_dict()
# create an instance of ApiV3SecretsBatchRawPost200Response from a dict
api_v3_secrets_batch_raw_post200_response_from_dict = ApiV3SecretsBatchRawPost200Response.from_dict(api_v3_secrets_batch_raw_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


