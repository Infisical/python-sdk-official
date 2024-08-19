# ApiV1SsoConfigGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**organization** | **str** |  | 
**org_id** | **str** |  | 
**auth_provider** | **str** |  | 
**is_active** | **bool** |  | 
**entry_point** | **str** |  | 
**issuer** | **str** |  | 
**cert** | **str** |  | 
**last_used** | **datetime** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_sso_config_get200_response import ApiV1SsoConfigGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoConfigGet200Response from a JSON string
api_v1_sso_config_get200_response_instance = ApiV1SsoConfigGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoConfigGet200Response.to_json()

# convert the object into a dict
api_v1_sso_config_get200_response_dict = api_v1_sso_config_get200_response_instance.to_dict()
# create an instance of ApiV1SsoConfigGet200Response from a dict
api_v1_sso_config_get200_response_from_dict = ApiV1SsoConfigGet200Response.from_dict(api_v1_sso_config_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


