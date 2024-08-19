# ApiV1SecretRotationsPost200ResponseSecretRotation


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
**outputs** | [**List[ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner]**](ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_rotations_post200_response_secret_rotation import ApiV1SecretRotationsPost200ResponseSecretRotation

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretRotationsPost200ResponseSecretRotation from a JSON string
api_v1_secret_rotations_post200_response_secret_rotation_instance = ApiV1SecretRotationsPost200ResponseSecretRotation.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretRotationsPost200ResponseSecretRotation.to_json()

# convert the object into a dict
api_v1_secret_rotations_post200_response_secret_rotation_dict = api_v1_secret_rotations_post200_response_secret_rotation_instance.to_dict()
# create an instance of ApiV1SecretRotationsPost200ResponseSecretRotation from a dict
api_v1_secret_rotations_post200_response_secret_rotation_from_dict = ApiV1SecretRotationsPost200ResponseSecretRotation.from_dict(api_v1_secret_rotations_post200_response_secret_rotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


