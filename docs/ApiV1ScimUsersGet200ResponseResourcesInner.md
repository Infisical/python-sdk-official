# ApiV1ScimUsersGet200ResponseResourcesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_name** | **str** |  | 
**name** | [**ApiV1ScimUsersGet200ResponseResourcesInnerName**](ApiV1ScimUsersGet200ResponseResourcesInnerName.md) |  | 
**emails** | [**List[ApiV1ScimUsersGet200ResponseResourcesInnerEmailsInner]**](ApiV1ScimUsersGet200ResponseResourcesInnerEmailsInner.md) |  | 
**display_name** | **str** |  | 
**active** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_users_get200_response_resources_inner import ApiV1ScimUsersGet200ResponseResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimUsersGet200ResponseResourcesInner from a JSON string
api_v1_scim_users_get200_response_resources_inner_instance = ApiV1ScimUsersGet200ResponseResourcesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimUsersGet200ResponseResourcesInner.to_json()

# convert the object into a dict
api_v1_scim_users_get200_response_resources_inner_dict = api_v1_scim_users_get200_response_resources_inner_instance.to_dict()
# create an instance of ApiV1ScimUsersGet200ResponseResourcesInner from a dict
api_v1_scim_users_get200_response_resources_inner_from_dict = ApiV1ScimUsersGet200ResponseResourcesInner.from_dict(api_v1_scim_users_get200_response_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


