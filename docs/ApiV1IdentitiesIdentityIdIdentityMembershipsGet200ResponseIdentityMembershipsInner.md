# ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**identity_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**roles** | [**List[ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner]**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.md) |  | 
**identity** | [**ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity**](ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity.md) |  | 
**project** | [**ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerProject**](ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerProject.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner import ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner from a JSON string
api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner_instance = ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner.to_json()

# convert the object into a dict
api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner_dict = api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner_instance.to_dict()
# create an instance of ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner from a dict
api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner_from_dict = ApiV1IdentitiesIdentityIdIdentityMembershipsGet200ResponseIdentityMembershipsInner.from_dict(api_v1_identities_identity_id_identity_memberships_get200_response_identity_memberships_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


