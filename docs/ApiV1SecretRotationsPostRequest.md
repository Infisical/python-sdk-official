# ApiV1SecretRotationsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**secret_path** | **str** |  | 
**environment** | **str** |  | 
**interval** | **float** |  | 
**provider** | **str** |  | 
**custom_provider** | **str** |  | [optional] 
**inputs** | **Dict[str, object]** |  | 
**outputs** | **Dict[str, str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_rotations_post_request import ApiV1SecretRotationsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretRotationsPostRequest from a JSON string
api_v1_secret_rotations_post_request_instance = ApiV1SecretRotationsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretRotationsPostRequest.to_json()

# convert the object into a dict
api_v1_secret_rotations_post_request_dict = api_v1_secret_rotations_post_request_instance.to_dict()
# create an instance of ApiV1SecretRotationsPostRequest from a dict
api_v1_secret_rotations_post_request_from_dict = ApiV1SecretRotationsPostRequest.from_dict(api_v1_secret_rotations_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


