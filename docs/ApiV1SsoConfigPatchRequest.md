# ApiV1SsoConfigPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_provider** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**entry_point** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**cert** | **str** |  | [optional] 
**organization_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_sso_config_patch_request import ApiV1SsoConfigPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoConfigPatchRequest from a JSON string
api_v1_sso_config_patch_request_instance = ApiV1SsoConfigPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoConfigPatchRequest.to_json()

# convert the object into a dict
api_v1_sso_config_patch_request_dict = api_v1_sso_config_patch_request_instance.to_dict()
# create an instance of ApiV1SsoConfigPatchRequest from a dict
api_v1_sso_config_patch_request_from_dict = ApiV1SsoConfigPatchRequest.from_dict(api_v1_sso_config_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


