# ApiV1SecretSharingGet200ResponseSecretsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**encrypted_value** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**hashed_hex** | **str** |  | 
**expires_at** | **datetime** |  | 
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**expires_after_views** | **float** |  | [optional] 
**access_type** | **str** |  | [optional] [default to 'anyone']
**name** | **str** |  | [optional] 
**last_viewed_at** | **datetime** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_sharing_get200_response_secrets_inner import ApiV1SecretSharingGet200ResponseSecretsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretSharingGet200ResponseSecretsInner from a JSON string
api_v1_secret_sharing_get200_response_secrets_inner_instance = ApiV1SecretSharingGet200ResponseSecretsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretSharingGet200ResponseSecretsInner.to_json()

# convert the object into a dict
api_v1_secret_sharing_get200_response_secrets_inner_dict = api_v1_secret_sharing_get200_response_secrets_inner_instance.to_dict()
# create an instance of ApiV1SecretSharingGet200ResponseSecretsInner from a dict
api_v1_secret_sharing_get200_response_secrets_inner_from_dict = ApiV1SecretSharingGet200ResponseSecretsInner.from_dict(api_v1_secret_sharing_get200_response_secrets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


