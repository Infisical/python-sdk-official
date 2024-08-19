# ApiV1ExternalKmsPostRequestProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**inputs** | [**ApiV1ExternalKmsPostRequestProviderInputs**](ApiV1ExternalKmsPostRequestProviderInputs.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_post_request_provider import ApiV1ExternalKmsPostRequestProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsPostRequestProvider from a JSON string
api_v1_external_kms_post_request_provider_instance = ApiV1ExternalKmsPostRequestProvider.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsPostRequestProvider.to_json()

# convert the object into a dict
api_v1_external_kms_post_request_provider_dict = api_v1_external_kms_post_request_provider_instance.to_dict()
# create an instance of ApiV1ExternalKmsPostRequestProvider from a dict
api_v1_external_kms_post_request_provider_from_dict = ApiV1ExternalKmsPostRequestProvider.from_dict(api_v1_external_kms_post_request_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


