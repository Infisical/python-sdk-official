# ApiV1SecretSharingPublicIdGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_value** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**expires_at** | **datetime** |  | 
**expires_after_views** | **float** |  | [optional] 
**access_type** | **str** |  | [optional] [default to 'anyone']
**org_name** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_sharing_public_id_get200_response import ApiV1SecretSharingPublicIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretSharingPublicIdGet200Response from a JSON string
api_v1_secret_sharing_public_id_get200_response_instance = ApiV1SecretSharingPublicIdGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretSharingPublicIdGet200Response.to_json()

# convert the object into a dict
api_v1_secret_sharing_public_id_get200_response_dict = api_v1_secret_sharing_public_id_get200_response_instance.to_dict()
# create an instance of ApiV1SecretSharingPublicIdGet200Response from a dict
api_v1_secret_sharing_public_id_get200_response_from_dict = ApiV1SecretSharingPublicIdGet200Response.from_dict(api_v1_secret_sharing_public_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


