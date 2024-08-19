# ApiV1AdminUserManagementUsersGet200ResponseUsersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_admin_user_management_users_get200_response_users_inner import ApiV1AdminUserManagementUsersGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdminUserManagementUsersGet200ResponseUsersInner from a JSON string
api_v1_admin_user_management_users_get200_response_users_inner_instance = ApiV1AdminUserManagementUsersGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1AdminUserManagementUsersGet200ResponseUsersInner.to_json()

# convert the object into a dict
api_v1_admin_user_management_users_get200_response_users_inner_dict = api_v1_admin_user_management_users_get200_response_users_inner_instance.to_dict()
# create an instance of ApiV1AdminUserManagementUsersGet200ResponseUsersInner from a dict
api_v1_admin_user_management_users_get200_response_users_inner_from_dict = ApiV1AdminUserManagementUsersGet200ResponseUsersInner.from_dict(api_v1_admin_user_management_users_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


