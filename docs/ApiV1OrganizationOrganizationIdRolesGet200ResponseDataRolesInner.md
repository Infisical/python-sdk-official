# ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**slug** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**org_id** | **str** |  | 
**permissions** | **object** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_roles_get200_response_data_roles_inner import ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner from a JSON string
api_v1_organization_organization_id_roles_get200_response_data_roles_inner_instance = ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner.to_json()

# convert the object into a dict
api_v1_organization_organization_id_roles_get200_response_data_roles_inner_dict = api_v1_organization_organization_id_roles_get200_response_data_roles_inner_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner from a dict
api_v1_organization_organization_id_roles_get200_response_data_roles_inner_from_dict = ApiV1OrganizationOrganizationIdRolesGet200ResponseDataRolesInner.from_dict(api_v1_organization_organization_id_roles_get200_response_data_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


