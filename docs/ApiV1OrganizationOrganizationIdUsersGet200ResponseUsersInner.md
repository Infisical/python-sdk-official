# ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | [optional] [default to 'invited']
**invite_email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**org_id** | **str** |  | 
**role_id** | **str** |  | [optional] 
**project_favorites** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**user** | [**ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser**](ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_users_get200_response_users_inner import ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner from a JSON string
api_v1_organization_organization_id_users_get200_response_users_inner_instance = ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner.to_json()

# convert the object into a dict
api_v1_organization_organization_id_users_get200_response_users_inner_dict = api_v1_organization_organization_id_users_get200_response_users_inner_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner from a dict
api_v1_organization_organization_id_users_get200_response_users_inner_from_dict = ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInner.from_dict(api_v1_organization_organization_id_users_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


