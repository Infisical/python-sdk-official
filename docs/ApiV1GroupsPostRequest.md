# ApiV1GroupsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the group to create. | 
**slug** | **str** | The slug of the group to create. | [optional] 
**role** | **str** | The role of the group to create. | [optional] [default to 'no-access']

## Example

```python
from infisicalapi_client.models.api_v1_groups_post_request import ApiV1GroupsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1GroupsPostRequest from a JSON string
api_v1_groups_post_request_instance = ApiV1GroupsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1GroupsPostRequest.to_json()

# convert the object into a dict
api_v1_groups_post_request_dict = api_v1_groups_post_request_instance.to_dict()
# create an instance of ApiV1GroupsPostRequest from a dict
api_v1_groups_post_request_from_dict = ApiV1GroupsPostRequest.from_dict(api_v1_groups_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


