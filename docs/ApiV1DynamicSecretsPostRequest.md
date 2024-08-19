# ApiV1DynamicSecretsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project to create dynamic secret in. | 
**provider** | [**ApiV1DynamicSecretsPostRequestProvider**](ApiV1DynamicSecretsPostRequestProvider.md) |  | 
**default_ttl** | **str** | The default TTL that will be applied for all the leases. | 
**max_ttl** | **str** | The maximum limit a TTL can be leases or renewed. | [optional] 
**path** | **str** | The path to create the dynamic secret in. | [optional] [default to '/']
**environment_slug** | **str** | The slug of the environment to create the dynamic secret in. | 
**name** | **str** | The name of the dynamic secret. | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request import ApiV1DynamicSecretsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsPostRequest from a JSON string
api_v1_dynamic_secrets_post_request_instance = ApiV1DynamicSecretsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsPostRequest.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_post_request_dict = api_v1_dynamic_secrets_post_request_instance.to_dict()
# create an instance of ApiV1DynamicSecretsPostRequest from a dict
api_v1_dynamic_secrets_post_request_from_dict = ApiV1DynamicSecretsPostRequest.from_dict(api_v1_dynamic_secrets_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


