# ApiV1IntegrationIntegrationIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** | The name of the external integration providers app entity that you want to sync secrets with. Used in Netlify, GitHub, Vercel integrations. | [optional] 
**app_id** | **str** | The ID of the external integration providers app entity that you want to sync secrets with. Used in Netlify, GitHub, Vercel integrations. | [optional] 
**is_active** | **bool** | Whether the integration should be active or disabled. | 
**secret_path** | **str** | The path of the secrets to sync secrets from. | [optional] [default to '/']
**target_environment** | **str** | The target environment of the integration provider. Used in cloudflare pages, TeamCity, Gitlab integrations. | 
**owner** | **str** | External integration providers service entity owner. Used in Github. | 
**environment** | **str** | The environment to sync secrets from. | 
**metadata** | [**ApiV1IntegrationIntegrationIdPatchRequestMetadata**](ApiV1IntegrationIntegrationIdPatchRequestMetadata.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_integration_integration_id_patch_request import ApiV1IntegrationIntegrationIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IntegrationIntegrationIdPatchRequest from a JSON string
api_v1_integration_integration_id_patch_request_instance = ApiV1IntegrationIntegrationIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1IntegrationIntegrationIdPatchRequest.to_json()

# convert the object into a dict
api_v1_integration_integration_id_patch_request_dict = api_v1_integration_integration_id_patch_request_instance.to_dict()
# create an instance of ApiV1IntegrationIntegrationIdPatchRequest from a dict
api_v1_integration_integration_id_patch_request_from_dict = ApiV1IntegrationIntegrationIdPatchRequest.from_dict(api_v1_integration_integration_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


