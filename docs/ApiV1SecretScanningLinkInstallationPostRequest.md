# ApiV1SecretScanningLinkInstallationPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_id** | **str** |  | 
**session_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_scanning_link_installation_post_request import ApiV1SecretScanningLinkInstallationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretScanningLinkInstallationPostRequest from a JSON string
api_v1_secret_scanning_link_installation_post_request_instance = ApiV1SecretScanningLinkInstallationPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretScanningLinkInstallationPostRequest.to_json()

# convert the object into a dict
api_v1_secret_scanning_link_installation_post_request_dict = api_v1_secret_scanning_link_installation_post_request_instance.to_dict()
# create an instance of ApiV1SecretScanningLinkInstallationPostRequest from a dict
api_v1_secret_scanning_link_installation_post_request_from_dict = ApiV1SecretScanningLinkInstallationPostRequest.from_dict(api_v1_secret_scanning_link_installation_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


