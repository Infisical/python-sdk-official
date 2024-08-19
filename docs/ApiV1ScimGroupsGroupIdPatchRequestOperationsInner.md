# ApiV1ScimGroupsGroupIdPatchRequestOperationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**value** | [**List[ApiV1ScimGroupsGroupIdPatchRequestOperationsInnerAnyOf2ValueInner]**](ApiV1ScimGroupsGroupIdPatchRequestOperationsInnerAnyOf2ValueInner.md) |  | 
**path** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_groups_group_id_patch_request_operations_inner import ApiV1ScimGroupsGroupIdPatchRequestOperationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimGroupsGroupIdPatchRequestOperationsInner from a JSON string
api_v1_scim_groups_group_id_patch_request_operations_inner_instance = ApiV1ScimGroupsGroupIdPatchRequestOperationsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimGroupsGroupIdPatchRequestOperationsInner.to_json()

# convert the object into a dict
api_v1_scim_groups_group_id_patch_request_operations_inner_dict = api_v1_scim_groups_group_id_patch_request_operations_inner_instance.to_dict()
# create an instance of ApiV1ScimGroupsGroupIdPatchRequestOperationsInner from a dict
api_v1_scim_groups_group_id_patch_request_operations_inner_from_dict = ApiV1ScimGroupsGroupIdPatchRequestOperationsInner.from_dict(api_v1_scim_groups_group_id_patch_request_operations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


