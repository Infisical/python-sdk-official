# ApiV1ScimUsersOrgMembershipIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**id** | **str** |  | 
**user_name** | **str** |  | 
**name** | [**ApiV1ScimUsersGet200ResponseResourcesInnerName**](ApiV1ScimUsersGet200ResponseResourcesInnerName.md) |  | 
**display_name** | **str** |  | 
**active** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_users_org_membership_id_put_request import ApiV1ScimUsersOrgMembershipIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimUsersOrgMembershipIdPutRequest from a JSON string
api_v1_scim_users_org_membership_id_put_request_instance = ApiV1ScimUsersOrgMembershipIdPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimUsersOrgMembershipIdPutRequest.to_json()

# convert the object into a dict
api_v1_scim_users_org_membership_id_put_request_dict = api_v1_scim_users_org_membership_id_put_request_instance.to_dict()
# create an instance of ApiV1ScimUsersOrgMembershipIdPutRequest from a dict
api_v1_scim_users_org_membership_id_put_request_from_dict = ApiV1ScimUsersOrgMembershipIdPutRequest.from_dict(api_v1_scim_users_org_membership_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


