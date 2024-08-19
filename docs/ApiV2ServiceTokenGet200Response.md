# ApiV2ServiceTokenGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**scopes** | **object** |  | [optional] 
**permissions** | **List[str]** |  | 
**last_used** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**secret_hash** | **str** |  | 
**encrypted_key** | **str** |  | [optional] 
**iv** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**created_by** | **str** |  | 
**project_id** | **str** |  | 
**workspace** | **str** |  | 
**user** | [**ApiV2ServiceTokenGet200ResponseUser**](ApiV2ServiceTokenGet200ResponseUser.md) |  | 
**id** | **str** |  | 
**v** | **float** |  | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v2_service_token_get200_response import ApiV2ServiceTokenGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ServiceTokenGet200Response from a JSON string
api_v2_service_token_get200_response_instance = ApiV2ServiceTokenGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2ServiceTokenGet200Response.to_json()

# convert the object into a dict
api_v2_service_token_get200_response_dict = api_v2_service_token_get200_response_instance.to_dict()
# create an instance of ApiV2ServiceTokenGet200Response from a dict
api_v2_service_token_get200_response_from_dict = ApiV2ServiceTokenGet200Response.from_dict(api_v2_service_token_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


