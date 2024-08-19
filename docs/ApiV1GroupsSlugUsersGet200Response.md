# ApiV1GroupsSlugUsersGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[ApiV1GroupsSlugUsersGet200ResponseUsersInner]**](ApiV1GroupsSlugUsersGet200ResponseUsersInner.md) |  | 
**total_count** | **float** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_groups_slug_users_get200_response import ApiV1GroupsSlugUsersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1GroupsSlugUsersGet200Response from a JSON string
api_v1_groups_slug_users_get200_response_instance = ApiV1GroupsSlugUsersGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1GroupsSlugUsersGet200Response.to_json()

# convert the object into a dict
api_v1_groups_slug_users_get200_response_dict = api_v1_groups_slug_users_get200_response_instance.to_dict()
# create an instance of ApiV1GroupsSlugUsersGet200Response from a dict
api_v1_groups_slug_users_get200_response_from_dict = ApiV1GroupsSlugUsersGet200Response.from_dict(api_v1_groups_slug_users_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


