# ApiV1GroupsSlugUsersGet200ResponseUsersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**username** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**id** | **str** |  | 
**is_part_of_group** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_groups_slug_users_get200_response_users_inner import ApiV1GroupsSlugUsersGet200ResponseUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1GroupsSlugUsersGet200ResponseUsersInner from a JSON string
api_v1_groups_slug_users_get200_response_users_inner_instance = ApiV1GroupsSlugUsersGet200ResponseUsersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1GroupsSlugUsersGet200ResponseUsersInner.to_json()

# convert the object into a dict
api_v1_groups_slug_users_get200_response_users_inner_dict = api_v1_groups_slug_users_get200_response_users_inner_instance.to_dict()
# create an instance of ApiV1GroupsSlugUsersGet200ResponseUsersInner from a dict
api_v1_groups_slug_users_get200_response_users_inner_from_dict = ApiV1GroupsSlugUsersGet200ResponseUsersInner.from_dict(api_v1_groups_slug_users_get200_response_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


