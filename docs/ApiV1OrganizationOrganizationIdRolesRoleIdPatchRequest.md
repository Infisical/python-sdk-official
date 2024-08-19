# ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_roles_role_id_patch_request import ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest from a JSON string
api_v1_organization_organization_id_roles_role_id_patch_request_instance = ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest.to_json()

# convert the object into a dict
api_v1_organization_organization_id_roles_role_id_patch_request_dict = api_v1_organization_organization_id_roles_role_id_patch_request_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest from a dict
api_v1_organization_organization_id_roles_role_id_patch_request_from_dict = ApiV1OrganizationOrganizationIdRolesRoleIdPatchRequest.from_dict(api_v1_organization_organization_id_roles_role_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


