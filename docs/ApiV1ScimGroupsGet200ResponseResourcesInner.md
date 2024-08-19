# ApiV1ScimGroupsGet200ResponseResourcesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**id** | **str** |  | 
**display_name** | **str** |  | 
**members** | [**List[ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner]**](ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner.md) |  | 
**meta** | [**ApiV1ScimGroupsGet200ResponseResourcesInnerMeta**](ApiV1ScimGroupsGet200ResponseResourcesInnerMeta.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_groups_get200_response_resources_inner import ApiV1ScimGroupsGet200ResponseResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimGroupsGet200ResponseResourcesInner from a JSON string
api_v1_scim_groups_get200_response_resources_inner_instance = ApiV1ScimGroupsGet200ResponseResourcesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimGroupsGet200ResponseResourcesInner.to_json()

# convert the object into a dict
api_v1_scim_groups_get200_response_resources_inner_dict = api_v1_scim_groups_get200_response_resources_inner_instance.to_dict()
# create an instance of ApiV1ScimGroupsGet200ResponseResourcesInner from a dict
api_v1_scim_groups_get200_response_resources_inner_from_dict = ApiV1ScimGroupsGet200ResponseResourcesInner.from_dict(api_v1_scim_groups_get200_response_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


