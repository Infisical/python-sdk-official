# ApiV2WorkspaceProjectSlugGroupsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_memberships** | [**List[ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner]**](ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_slug_groups_get200_response import ApiV2WorkspaceProjectSlugGroupsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectSlugGroupsGet200Response from a JSON string
api_v2_workspace_project_slug_groups_get200_response_instance = ApiV2WorkspaceProjectSlugGroupsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectSlugGroupsGet200Response.to_json()

# convert the object into a dict
api_v2_workspace_project_slug_groups_get200_response_dict = api_v2_workspace_project_slug_groups_get200_response_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectSlugGroupsGet200Response from a dict
api_v2_workspace_project_slug_groups_get200_response_from_dict = ApiV2WorkspaceProjectSlugGroupsGet200Response.from_dict(api_v2_workspace_project_slug_groups_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


