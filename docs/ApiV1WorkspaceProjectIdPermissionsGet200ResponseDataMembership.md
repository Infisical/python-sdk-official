# ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | 
**project_id** | **str** |  | 
**roles** | [**List[ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembershipRolesInner]**](ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembershipRolesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_workspace_project_id_permissions_get200_response_data_membership import ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership from a JSON string
api_v1_workspace_project_id_permissions_get200_response_data_membership_instance = ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership.from_json(json)
# print the JSON string representation of the object
print ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership.to_json()

# convert the object into a dict
api_v1_workspace_project_id_permissions_get200_response_data_membership_dict = api_v1_workspace_project_id_permissions_get200_response_data_membership_instance.to_dict()
# create an instance of ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership from a dict
api_v1_workspace_project_id_permissions_get200_response_data_membership_from_dict = ApiV1WorkspaceProjectIdPermissionsGet200ResponseDataMembership.from_dict(api_v1_workspace_project_id_permissions_get200_response_data_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


