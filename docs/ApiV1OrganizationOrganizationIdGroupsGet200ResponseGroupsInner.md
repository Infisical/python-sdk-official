# ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**org_id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**role** | **str** |  | 
**role_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**custom_role** | [**ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole**](ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_groups_get200_response_groups_inner import ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner from a JSON string
api_v1_organization_organization_id_groups_get200_response_groups_inner_instance = ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner.to_json()

# convert the object into a dict
api_v1_organization_organization_id_groups_get200_response_groups_inner_dict = api_v1_organization_organization_id_groups_get200_response_groups_inner_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner from a dict
api_v1_organization_organization_id_groups_get200_response_groups_inner_from_dict = ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInner.from_dict(api_v1_organization_organization_id_groups_get200_response_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


