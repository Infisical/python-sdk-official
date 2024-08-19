# ApiV1IntegrationPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_auth_id** | **str** | The ID of the integration auth object to link with integration. | 
**app** | **str** | The name of the external integration providers app entity that you want to sync secrets with. Used in Netlify, GitHub, Vercel integrations. | [optional] 
**is_active** | **bool** | Whether the integration should be active or disabled. | [optional] [default to True]
**app_id** | **str** | The ID of the external integration providers app entity that you want to sync secrets with. Used in Netlify, GitHub, Vercel integrations. | [optional] 
**secret_path** | **str** | The path of the secrets to sync secrets from. | [optional] [default to '/']
**source_environment** | **str** | The environment to sync secret from. | 
**target_environment** | **str** | The target environment of the integration provider. Used in cloudflare pages, TeamCity, Gitlab integrations. | [optional] 
**target_environment_id** | **str** | The target environment id of the integration provider. Used in cloudflare pages, teamcity, gitlab integrations. | [optional] 
**target_service** | **str** | The service based grouping identifier of the external provider. Used in Terraform cloud, Checkly, Railway and NorthFlank | [optional] 
**target_service_id** | **str** | The service based grouping identifier ID of the external provider. Used in Terraform cloud, Checkly, Railway and NorthFlank | [optional] 
**owner** | **str** | External integration providers service entity owner. Used in Github. | [optional] 
**url** | **str** | The self-hosted URL of the platform to integrate with | [optional] 
**path** | **str** | Path to save the synced secrets. Used by Gitlab, AWS Parameter Store, Vault | [optional] 
**region** | **str** | AWS region to sync secrets to. | [optional] 
**scope** | **str** | Scope of the provider. Used by Github, Qovery | [optional] 
**metadata** | [**ApiV1IntegrationPostRequestMetadata**](ApiV1IntegrationPostRequestMetadata.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_integration_post_request import ApiV1IntegrationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IntegrationPostRequest from a JSON string
api_v1_integration_post_request_instance = ApiV1IntegrationPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1IntegrationPostRequest.to_json()

# convert the object into a dict
api_v1_integration_post_request_dict = api_v1_integration_post_request_instance.to_dict()
# create an instance of ApiV1IntegrationPostRequest from a dict
api_v1_integration_post_request_from_dict = ApiV1IntegrationPostRequest.from_dict(api_v1_integration_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


