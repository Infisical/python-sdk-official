# ApiV1SecretRotationsGet200ResponseSecretRotationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**provider** | **str** |  | 
**secret_path** | **str** |  | 
**interval** | **float** |  | 
**last_rotated_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**status_message** | **str** |  | [optional] 
**encrypted_data** | **str** |  | [optional] 
**encrypted_data_iv** | **str** |  | [optional] 
**encrypted_data_tag** | **str** |  | [optional] 
**algorithm** | **str** |  | [optional] 
**key_encoding** | **str** |  | [optional] 
**env_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**environment** | [**ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment**](ApiV1SecretApprovalsGet200ResponseApprovalsInnerEnvironment.md) |  | 
**outputs** | [**List[ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner]**](ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_rotations_get200_response_secret_rotations_inner import ApiV1SecretRotationsGet200ResponseSecretRotationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretRotationsGet200ResponseSecretRotationsInner from a JSON string
api_v1_secret_rotations_get200_response_secret_rotations_inner_instance = ApiV1SecretRotationsGet200ResponseSecretRotationsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretRotationsGet200ResponseSecretRotationsInner.to_json()

# convert the object into a dict
api_v1_secret_rotations_get200_response_secret_rotations_inner_dict = api_v1_secret_rotations_get200_response_secret_rotations_inner_instance.to_dict()
# create an instance of ApiV1SecretRotationsGet200ResponseSecretRotationsInner from a dict
api_v1_secret_rotations_get200_response_secret_rotations_inner_from_dict = ApiV1SecretRotationsGet200ResponseSecretRotationsInner.from_dict(api_v1_secret_rotations_get200_response_secret_rotations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


