# ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | [optional] [default to 'invited']
**invite_email** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | 
**role_id** | **str** |  | [optional] 
**project_favorites** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_permissions_get200_response_membership import ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership from a JSON string
api_v1_organization_organization_id_permissions_get200_response_membership_instance = ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership.to_json()

# convert the object into a dict
api_v1_organization_organization_id_permissions_get200_response_membership_dict = api_v1_organization_organization_id_permissions_get200_response_membership_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership from a dict
api_v1_organization_organization_id_permissions_get200_response_membership_from_dict = ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership.from_dict(api_v1_organization_organization_id_permissions_get200_response_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


