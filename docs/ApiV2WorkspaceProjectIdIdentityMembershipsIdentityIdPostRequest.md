# ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] [default to 'no-access']
**roles** | [**List[ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInner]**](ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequestRolesInner.md) | A list of role slugs to assign to the newly created identity project membership. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_post_request import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest from a JSON string
api_v2_workspace_project_id_identity_memberships_identity_id_post_request_instance = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest.to_json()

# convert the object into a dict
api_v2_workspace_project_id_identity_memberships_identity_id_post_request_dict = api_v2_workspace_project_id_identity_memberships_identity_id_post_request_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest from a dict
api_v2_workspace_project_id_identity_memberships_identity_id_post_request_from_dict = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPostRequest.from_dict(api_v2_workspace_project_id_identity_memberships_identity_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


