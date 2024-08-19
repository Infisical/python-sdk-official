# ApiV3SecretsTagsSecretNameDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | The slug of the project where the secret is located | 
**environment** | **str** | The slug of the environment where the secret is located | 
**secret_path** | **str** | The path of the secret to detach tags from. | [optional] [default to '/']
**type** | **str** | The type of the secret to attach tags to. (shared/personal) | [optional] [default to 'shared']
**tag_slugs** | **List[str]** | An array of existing tag slugs to detach from the secret. | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_tags_secret_name_delete_request import ApiV3SecretsTagsSecretNameDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsTagsSecretNameDeleteRequest from a JSON string
api_v3_secrets_tags_secret_name_delete_request_instance = ApiV3SecretsTagsSecretNameDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsTagsSecretNameDeleteRequest.to_json()

# convert the object into a dict
api_v3_secrets_tags_secret_name_delete_request_dict = api_v3_secrets_tags_secret_name_delete_request_instance.to_dict()
# create an instance of ApiV3SecretsTagsSecretNameDeleteRequest from a dict
api_v3_secrets_tags_secret_name_delete_request_from_dict = ApiV3SecretsTagsSecretNameDeleteRequest.from_dict(api_v3_secrets_tags_secret_name_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


