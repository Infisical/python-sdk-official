# ApiV1GroupsCurrentSlugPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the group to update to. | [optional] 
**slug** | **str** | The new slug of the group to update to. | [optional] 
**role** | **str** | The new role of the group to update to. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_groups_current_slug_patch_request import ApiV1GroupsCurrentSlugPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1GroupsCurrentSlugPatchRequest from a JSON string
api_v1_groups_current_slug_patch_request_instance = ApiV1GroupsCurrentSlugPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1GroupsCurrentSlugPatchRequest.to_json()

# convert the object into a dict
api_v1_groups_current_slug_patch_request_dict = api_v1_groups_current_slug_patch_request_instance.to_dict()
# create an instance of ApiV1GroupsCurrentSlugPatchRequest from a dict
api_v1_groups_current_slug_patch_request_from_dict = ApiV1GroupsCurrentSlugPatchRequest.from_dict(api_v1_groups_current_slug_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


