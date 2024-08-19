# ApiV1SecretScanningLinkInstallationPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**installation_id** | **str** |  | 
**user_id** | **str** |  | 
**org_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_scanning_link_installation_post200_response import ApiV1SecretScanningLinkInstallationPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretScanningLinkInstallationPost200Response from a JSON string
api_v1_secret_scanning_link_installation_post200_response_instance = ApiV1SecretScanningLinkInstallationPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretScanningLinkInstallationPost200Response.to_json()

# convert the object into a dict
api_v1_secret_scanning_link_installation_post200_response_dict = api_v1_secret_scanning_link_installation_post200_response_instance.to_dict()
# create an instance of ApiV1SecretScanningLinkInstallationPost200Response from a dict
api_v1_secret_scanning_link_installation_post200_response_from_dict = ApiV1SecretScanningLinkInstallationPost200Response.from_dict(api_v1_secret_scanning_link_installation_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


