# ApiV2ServiceTokenPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**workspace_id** | **str** |  | 
**scopes** | [**List[ApiV2ServiceTokenPostRequestScopesInner]**](ApiV2ServiceTokenPostRequestScopesInner.md) |  | 
**encrypted_key** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**expires_in** | **float** |  | 
**permissions** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_service_token_post_request import ApiV2ServiceTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ServiceTokenPostRequest from a JSON string
api_v2_service_token_post_request_instance = ApiV2ServiceTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2ServiceTokenPostRequest.to_json()

# convert the object into a dict
api_v2_service_token_post_request_dict = api_v2_service_token_post_request_instance.to_dict()
# create an instance of ApiV2ServiceTokenPostRequest from a dict
api_v2_service_token_post_request_from_dict = ApiV2ServiceTokenPostRequest.from_dict(api_v2_service_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


