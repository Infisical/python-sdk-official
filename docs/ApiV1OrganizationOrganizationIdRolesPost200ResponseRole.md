# ApiV1OrganizationOrganizationIdRolesPost200ResponseRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**slug** | **str** |  | 
**permissions** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**org_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_roles_post200_response_role import ApiV1OrganizationOrganizationIdRolesPost200ResponseRole

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdRolesPost200ResponseRole from a JSON string
api_v1_organization_organization_id_roles_post200_response_role_instance = ApiV1OrganizationOrganizationIdRolesPost200ResponseRole.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdRolesPost200ResponseRole.to_json()

# convert the object into a dict
api_v1_organization_organization_id_roles_post200_response_role_dict = api_v1_organization_organization_id_roles_post200_response_role_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdRolesPost200ResponseRole from a dict
api_v1_organization_organization_id_roles_post200_response_role_from_dict = ApiV1OrganizationOrganizationIdRolesPost200ResponseRole.from_dict(api_v1_organization_organization_id_roles_post200_response_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


