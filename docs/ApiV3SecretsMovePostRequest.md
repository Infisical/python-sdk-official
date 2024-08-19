# ApiV3SecretsMovePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** |  | 
**source_environment** | **str** |  | 
**source_secret_path** | **str** |  | [optional] [default to '/']
**destination_environment** | **str** |  | 
**destination_secret_path** | **str** |  | [optional] [default to '/']
**secret_ids** | **List[str]** |  | 
**should_overwrite** | **bool** |  | [optional] [default to False]

## Example

```python
from infisicalapi_client.models.api_v3_secrets_move_post_request import ApiV3SecretsMovePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsMovePostRequest from a JSON string
api_v3_secrets_move_post_request_instance = ApiV3SecretsMovePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsMovePostRequest.to_json()

# convert the object into a dict
api_v3_secrets_move_post_request_dict = api_v3_secrets_move_post_request_instance.to_dict()
# create an instance of ApiV3SecretsMovePostRequest from a dict
api_v3_secrets_move_post_request_from_dict = ApiV3SecretsMovePostRequest.from_dict(api_v3_secrets_move_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


