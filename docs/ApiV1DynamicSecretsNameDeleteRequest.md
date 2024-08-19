# ApiV1DynamicSecretsNameDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project to delete dynamic secret in. | 
**path** | **str** | The path to delete the dynamic secret in. | [optional] [default to '/']
**environment_slug** | **str** | The slug of the environment to delete the dynamic secret in. | 
**is_forced** | **bool** | A boolean flag to delete the the dynamic secret from infisical without trying to remove it from external provider. Used when the dynamic secret got modified externally. | [optional] [default to False]

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_delete_request import ApiV1DynamicSecretsNameDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNameDeleteRequest from a JSON string
api_v1_dynamic_secrets_name_delete_request_instance = ApiV1DynamicSecretsNameDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNameDeleteRequest.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_delete_request_dict = api_v1_dynamic_secrets_name_delete_request_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNameDeleteRequest from a dict
api_v1_dynamic_secrets_name_delete_request_from_dict = ApiV1DynamicSecretsNameDeleteRequest.from_dict(api_v1_dynamic_secrets_name_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


