# ApiV1SsoConfigPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**auth_provider** | **str** |  | 
**is_active** | **bool** |  | 
**encrypted_entry_point** | **str** |  | [optional] 
**entry_point_iv** | **str** |  | [optional] 
**entry_point_tag** | **str** |  | [optional] 
**encrypted_issuer** | **str** |  | [optional] 
**issuer_tag** | **str** |  | [optional] 
**issuer_iv** | **str** |  | [optional] 
**encrypted_cert** | **str** |  | [optional] 
**cert_iv** | **str** |  | [optional] 
**cert_tag** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**org_id** | **str** |  | 
**last_used** | **datetime** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_sso_config_post200_response import ApiV1SsoConfigPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SsoConfigPost200Response from a JSON string
api_v1_sso_config_post200_response_instance = ApiV1SsoConfigPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SsoConfigPost200Response.to_json()

# convert the object into a dict
api_v1_sso_config_post200_response_dict = api_v1_sso_config_post200_response_instance.to_dict()
# create an instance of ApiV1SsoConfigPost200Response from a dict
api_v1_sso_config_post200_response_from_dict = ApiV1SsoConfigPost200Response.from_dict(api_v1_sso_config_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


