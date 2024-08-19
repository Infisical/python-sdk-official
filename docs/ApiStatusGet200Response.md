# ApiStatusGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | 
**message** | **str** |  | 
**email_configured** | **bool** |  | [optional] 
**invite_only_signup** | **bool** |  | [optional] 
**redis_configured** | **bool** |  | [optional] 
**secret_scanning_configured** | **bool** |  | [optional] 
**saml_default_org_slug** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_status_get200_response import ApiStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiStatusGet200Response from a JSON string
api_status_get200_response_instance = ApiStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiStatusGet200Response.to_json()

# convert the object into a dict
api_status_get200_response_dict = api_status_get200_response_instance.to_dict()
# create an instance of ApiStatusGet200Response from a dict
api_status_get200_response_from_dict = ApiStatusGet200Response.from_dict(api_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


