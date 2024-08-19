# ApiV1ScimGroupsGroupIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**id** | **str** |  | 
**display_name** | **str** |  | 
**members** | [**List[ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner]**](ApiV1ScimUsersOrgMembershipIdGet201ResponseGroupsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_groups_group_id_put_request import ApiV1ScimGroupsGroupIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimGroupsGroupIdPutRequest from a JSON string
api_v1_scim_groups_group_id_put_request_instance = ApiV1ScimGroupsGroupIdPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimGroupsGroupIdPutRequest.to_json()

# convert the object into a dict
api_v1_scim_groups_group_id_put_request_dict = api_v1_scim_groups_group_id_put_request_instance.to_dict()
# create an instance of ApiV1ScimGroupsGroupIdPutRequest from a dict
api_v1_scim_groups_group_id_put_request_from_dict = ApiV1ScimGroupsGroupIdPutRequest.from_dict(api_v1_scim_groups_group_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


