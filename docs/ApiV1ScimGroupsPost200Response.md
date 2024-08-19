# ApiV1ScimGroupsPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**id** | **str** |  | 
**display_name** | **str** |  | 
**members** | [**List[ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner]**](ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner.md) |  | [optional] 
**meta** | [**ApiV1ScimGroupsGet200ResponseResourcesInnerMeta**](ApiV1ScimGroupsGet200ResponseResourcesInnerMeta.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_groups_post200_response import ApiV1ScimGroupsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimGroupsPost200Response from a JSON string
api_v1_scim_groups_post200_response_instance = ApiV1ScimGroupsPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimGroupsPost200Response.to_json()

# convert the object into a dict
api_v1_scim_groups_post200_response_dict = api_v1_scim_groups_post200_response_instance.to_dict()
# create an instance of ApiV1ScimGroupsPost200Response from a dict
api_v1_scim_groups_post200_response_from_dict = ApiV1ScimGroupsPost200Response.from_dict(api_v1_scim_groups_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


