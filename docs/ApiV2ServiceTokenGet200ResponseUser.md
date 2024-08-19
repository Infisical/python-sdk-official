# ApiV2ServiceTokenGet200ResponseUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_methods** | **List[str]** |  | [optional] 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**devices** | **object** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**mfa_methods** | **List[str]** |  | [optional] 
**v** | **float** |  | [optional] [default to 0]
**id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_service_token_get200_response_user import ApiV2ServiceTokenGet200ResponseUser

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ServiceTokenGet200ResponseUser from a JSON string
api_v2_service_token_get200_response_user_instance = ApiV2ServiceTokenGet200ResponseUser.from_json(json)
# print the JSON string representation of the object
print ApiV2ServiceTokenGet200ResponseUser.to_json()

# convert the object into a dict
api_v2_service_token_get200_response_user_dict = api_v2_service_token_get200_response_user_instance.to_dict()
# create an instance of ApiV2ServiceTokenGet200ResponseUser from a dict
api_v2_service_token_get200_response_user_from_dict = ApiV2ServiceTokenGet200ResponseUser.from_dict(api_v2_service_token_get200_response_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


