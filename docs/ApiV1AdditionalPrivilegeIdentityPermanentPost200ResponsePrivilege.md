# ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**slug** | **str** |  | 
**project_membership_id** | **str** |  | 
**is_temporary** | **bool** |  | [optional] [default to False]
**temporary_mode** | **str** |  | [optional] 
**temporary_range** | **str** |  | [optional] 
**temporary_access_start_time** | **datetime** |  | [optional] 
**temporary_access_end_time** | **datetime** |  | [optional] 
**permissions** | [**List[ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInner]**](ApiV1WorkspaceProjectSlugRolesPost200ResponseRolePermissionsInner.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_permanent_post200_response_privilege import ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege from a JSON string
api_v1_additional_privilege_identity_permanent_post200_response_privilege_instance = ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_permanent_post200_response_privilege_dict = api_v1_additional_privilege_identity_permanent_post200_response_privilege_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege from a dict
api_v1_additional_privilege_identity_permanent_post200_response_privilege_from_dict = ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege.from_dict(api_v1_additional_privilege_identity_permanent_post200_response_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


