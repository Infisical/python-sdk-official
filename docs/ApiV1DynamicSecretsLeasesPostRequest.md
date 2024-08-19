# ApiV1DynamicSecretsLeasesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_secret_name** | **str** | The name of the dynamic secret. | 
**project_slug** | **str** | The slug of the project of the dynamic secret in. | 
**ttl** | **str** | The lease lifetime ttl. If not provided the default TTL of dynamic secret will be used. | [optional] 
**path** | **str** | The path of the dynamic secret in. | [optional] [default to '/']
**environment_slug** | **str** | The path of the dynamic secret in. | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_leases_post_request import ApiV1DynamicSecretsLeasesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsLeasesPostRequest from a JSON string
api_v1_dynamic_secrets_leases_post_request_instance = ApiV1DynamicSecretsLeasesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsLeasesPostRequest.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_leases_post_request_dict = api_v1_dynamic_secrets_leases_post_request_instance.to_dict()
# create an instance of ApiV1DynamicSecretsLeasesPostRequest from a dict
api_v1_dynamic_secrets_leases_post_request_from_dict = ApiV1DynamicSecretsLeasesPostRequest.from_dict(api_v1_dynamic_secrets_leases_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


