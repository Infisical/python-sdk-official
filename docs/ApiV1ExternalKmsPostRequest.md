# ApiV1ExternalKmsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**description** | **str** |  | [optional] 
**provider** | [**ApiV1ExternalKmsPostRequestProvider**](ApiV1ExternalKmsPostRequestProvider.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_external_kms_post_request import ApiV1ExternalKmsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ExternalKmsPostRequest from a JSON string
api_v1_external_kms_post_request_instance = ApiV1ExternalKmsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ExternalKmsPostRequest.to_json()

# convert the object into a dict
api_v1_external_kms_post_request_dict = api_v1_external_kms_post_request_instance.to_dict()
# create an instance of ApiV1ExternalKmsPostRequest from a dict
api_v1_external_kms_post_request_from_dict = ApiV1ExternalKmsPostRequest.from_dict(api_v1_external_kms_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


