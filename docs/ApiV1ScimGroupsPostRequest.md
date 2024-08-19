# ApiV1ScimGroupsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**display_name** | **str** |  | 
**members** | [**List[ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner]**](ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_scim_groups_post_request import ApiV1ScimGroupsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimGroupsPostRequest from a JSON string
api_v1_scim_groups_post_request_instance = ApiV1ScimGroupsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimGroupsPostRequest.to_json()

# convert the object into a dict
api_v1_scim_groups_post_request_dict = api_v1_scim_groups_post_request_instance.to_dict()
# create an instance of ApiV1ScimGroupsPostRequest from a dict
api_v1_scim_groups_post_request_from_dict = ApiV1ScimGroupsPostRequest.from_dict(api_v1_scim_groups_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


