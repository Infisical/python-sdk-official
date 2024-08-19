# ApiV1ScimGroupsGroupIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**operations** | [**List[ApiV1ScimGroupsGroupIdPatchRequestOperationsInner]**](ApiV1ScimGroupsGroupIdPatchRequestOperationsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_groups_group_id_patch_request import ApiV1ScimGroupsGroupIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimGroupsGroupIdPatchRequest from a JSON string
api_v1_scim_groups_group_id_patch_request_instance = ApiV1ScimGroupsGroupIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimGroupsGroupIdPatchRequest.to_json()

# convert the object into a dict
api_v1_scim_groups_group_id_patch_request_dict = api_v1_scim_groups_group_id_patch_request_instance.to_dict()
# create an instance of ApiV1ScimGroupsGroupIdPatchRequest from a dict
api_v1_scim_groups_group_id_patch_request_from_dict = ApiV1ScimGroupsGroupIdPatchRequest.from_dict(api_v1_scim_groups_group_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


