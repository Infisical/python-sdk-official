# ApiV1ScimScimTokensGet200ResponseScimTokensInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**ttl_days** | **float** |  | [optional] [default to 365]
**description** | **str** |  | 
**org_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_scim_tokens_get200_response_scim_tokens_inner import ApiV1ScimScimTokensGet200ResponseScimTokensInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimScimTokensGet200ResponseScimTokensInner from a JSON string
api_v1_scim_scim_tokens_get200_response_scim_tokens_inner_instance = ApiV1ScimScimTokensGet200ResponseScimTokensInner.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimScimTokensGet200ResponseScimTokensInner.to_json()

# convert the object into a dict
api_v1_scim_scim_tokens_get200_response_scim_tokens_inner_dict = api_v1_scim_scim_tokens_get200_response_scim_tokens_inner_instance.to_dict()
# create an instance of ApiV1ScimScimTokensGet200ResponseScimTokensInner from a dict
api_v1_scim_scim_tokens_get200_response_scim_tokens_inner_from_dict = ApiV1ScimScimTokensGet200ResponseScimTokensInner.from_dict(api_v1_scim_scim_tokens_get200_response_scim_tokens_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


