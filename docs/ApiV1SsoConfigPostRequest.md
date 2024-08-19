# ApiV1SsoConfigPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**auth_provider** | **str** |  | 
**is_active** | **bool** |  | 
**entry_point** | **str** |  | 
**issuer** | **str** |  | 
**cert** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_sso_config_post_request import ApiV1SsoConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoConfigPostRequest from a JSON string
api_v1_sso_config_post_request_instance = ApiV1SsoConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoConfigPostRequest.to_json()

# convert the object into a dict
api_v1_sso_config_post_request_dict = api_v1_sso_config_post_request_instance.to_dict()
# create an instance of ApiV1SsoConfigPostRequest from a dict
api_v1_sso_config_post_request_from_dict = ApiV1SsoConfigPostRequest.from_dict(api_v1_sso_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


