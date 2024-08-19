# ApiV1DynamicSecretsNamePatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project to update dynamic secret in. | 
**path** | **str** | The path to update the dynamic secret in. | [optional] [default to '/']
**environment_slug** | **str** | The slug of the environment to update the dynamic secret in. | 
**data** | [**ApiV1DynamicSecretsNamePatchRequestData**](ApiV1DynamicSecretsNamePatchRequestData.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_patch_request import ApiV1DynamicSecretsNamePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNamePatchRequest from a JSON string
api_v1_dynamic_secrets_name_patch_request_instance = ApiV1DynamicSecretsNamePatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNamePatchRequest.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_patch_request_dict = api_v1_dynamic_secrets_name_patch_request_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNamePatchRequest from a dict
api_v1_dynamic_secrets_name_patch_request_from_dict = ApiV1DynamicSecretsNamePatchRequest.from_dict(api_v1_dynamic_secrets_name_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


