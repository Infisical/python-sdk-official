# ApiV1ScimScimTokensPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**ttl_days** | **float** |  | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_scim_scim_tokens_post_request import ApiV1ScimScimTokensPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimScimTokensPostRequest from a JSON string
api_v1_scim_scim_tokens_post_request_instance = ApiV1ScimScimTokensPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimScimTokensPostRequest.to_json()

# convert the object into a dict
api_v1_scim_scim_tokens_post_request_dict = api_v1_scim_scim_tokens_post_request_instance.to_dict()
# create an instance of ApiV1ScimScimTokensPostRequest from a dict
api_v1_scim_scim_tokens_post_request_from_dict = ApiV1ScimScimTokensPostRequest.from_dict(api_v1_scim_scim_tokens_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


