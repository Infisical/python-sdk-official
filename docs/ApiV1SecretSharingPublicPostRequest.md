# ApiV1SecretSharingPublicPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** |  | 
**hashed_hex** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**expires_at** | **str** |  | 
**expires_after_views** | **float** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_sharing_public_post_request import ApiV1SecretSharingPublicPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretSharingPublicPostRequest from a JSON string
api_v1_secret_sharing_public_post_request_instance = ApiV1SecretSharingPublicPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretSharingPublicPostRequest.to_json()

# convert the object into a dict
api_v1_secret_sharing_public_post_request_dict = api_v1_secret_sharing_public_post_request_instance.to_dict()
# create an instance of ApiV1SecretSharingPublicPostRequest from a dict
api_v1_secret_sharing_public_post_request_from_dict = ApiV1SecretSharingPublicPostRequest.from_dict(api_v1_secret_sharing_public_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


