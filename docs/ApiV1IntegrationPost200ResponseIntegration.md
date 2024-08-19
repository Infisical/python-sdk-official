# ApiV1IntegrationPost200ResponseIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_active** | **bool** |  | 
**url** | **str** |  | [optional] 
**app** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**target_environment** | **str** |  | [optional] 
**target_environment_id** | **str** |  | [optional] 
**target_service** | **str** |  | [optional] 
**target_service_id** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**integration** | **str** |  | 
**metadata** | **object** |  | [optional] 
**integration_auth_id** | **str** |  | 
**env_id** | **str** |  | 
**secret_path** | **str** |  | [optional] [default to '/']
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_used** | **datetime** |  | [optional] 
**is_synced** | **bool** |  | [optional] 
**sync_message** | **str** |  | [optional] 
**last_sync_job_id** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_integration_post200_response_integration import ApiV1IntegrationPost200ResponseIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IntegrationPost200ResponseIntegration from a JSON string
api_v1_integration_post200_response_integration_instance = ApiV1IntegrationPost200ResponseIntegration.from_json(json)
# print the JSON string representation of the object
print ApiV1IntegrationPost200ResponseIntegration.to_json()

# convert the object into a dict
api_v1_integration_post200_response_integration_dict = api_v1_integration_post200_response_integration_instance.to_dict()
# create an instance of ApiV1IntegrationPost200ResponseIntegration from a dict
api_v1_integration_post200_response_integration_from_dict = ApiV1IntegrationPost200ResponseIntegration.from_dict(api_v1_integration_post200_response_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


