# ApiV1SecretSharingPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**encrypted_value** | **str** |  | 
**hashed_hex** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**expires_at** | **str** |  | 
**expires_after_views** | **float** |  | [optional] 
**access_type** | **str** |  | [optional] [default to 'organization']

## Example

```python
from infisicalapi_client.models.api_v1_secret_sharing_post_request import ApiV1SecretSharingPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretSharingPostRequest from a JSON string
api_v1_secret_sharing_post_request_instance = ApiV1SecretSharingPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretSharingPostRequest.to_json()

# convert the object into a dict
api_v1_secret_sharing_post_request_dict = api_v1_secret_sharing_post_request_instance.to_dict()
# create an instance of ApiV1SecretSharingPostRequest from a dict
api_v1_secret_sharing_post_request_from_dict = ApiV1SecretSharingPostRequest.from_dict(api_v1_secret_sharing_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


