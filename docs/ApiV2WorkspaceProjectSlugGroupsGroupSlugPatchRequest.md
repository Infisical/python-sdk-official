# ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner]**](ApiV1WorkspaceWorkspaceIdMembershipsMembershipIdPatchRequestRolesInner.md) | A list of roles to update the group to. | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_slug_groups_group_slug_patch_request import ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest from a JSON string
api_v2_workspace_project_slug_groups_group_slug_patch_request_instance = ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest.to_json()

# convert the object into a dict
api_v2_workspace_project_slug_groups_group_slug_patch_request_dict = api_v2_workspace_project_slug_groups_group_slug_patch_request_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest from a dict
api_v2_workspace_project_slug_groups_group_slug_patch_request_from_dict = ApiV2WorkspaceProjectSlugGroupsGroupSlugPatchRequest.from_dict(api_v2_workspace_project_slug_groups_group_slug_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


