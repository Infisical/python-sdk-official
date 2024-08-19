# ApiV1UserActionPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_user_action_post_request import ApiV1UserActionPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UserActionPostRequest from a JSON string
api_v1_user_action_post_request_instance = ApiV1UserActionPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1UserActionPostRequest.to_json()

# convert the object into a dict
api_v1_user_action_post_request_dict = api_v1_user_action_post_request_instance.to_dict()
# create an instance of ApiV1UserActionPostRequest from a dict
api_v1_user_action_post_request_from_dict = ApiV1UserActionPostRequest.from_dict(api_v1_user_action_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


