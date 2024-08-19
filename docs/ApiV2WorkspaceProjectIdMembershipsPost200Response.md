# ApiV2WorkspaceProjectIdMembershipsPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memberships** | [**List[ApiV1OrganizationAdminProjectsProjectIdGrantAdminAccessPost200ResponseMembership]**](ApiV1OrganizationAdminProjectsProjectIdGrantAdminAccessPost200ResponseMembership.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_memberships_post200_response import ApiV2WorkspaceProjectIdMembershipsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdMembershipsPost200Response from a JSON string
api_v2_workspace_project_id_memberships_post200_response_instance = ApiV2WorkspaceProjectIdMembershipsPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdMembershipsPost200Response.to_json()

# convert the object into a dict
api_v2_workspace_project_id_memberships_post200_response_dict = api_v2_workspace_project_id_memberships_post200_response_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdMembershipsPost200Response from a dict
api_v2_workspace_project_id_memberships_post200_response_from_dict = ApiV2WorkspaceProjectIdMembershipsPost200Response.from_dict(api_v2_workspace_project_id_memberships_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


