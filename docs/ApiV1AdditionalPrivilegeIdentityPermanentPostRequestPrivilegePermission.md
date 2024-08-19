# ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission

The permission object for the privilege.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[str]** | Describe what action an entity can take. Possible actions: create, edit, delete, and read | 
**subject** | **str** | The entity this permission pertains to. Possible options: secrets, environments | 
**conditions** | [**ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions**](ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_permanent_post_request_privilege_permission import ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission from a JSON string
api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_instance = ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_dict = api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission from a dict
api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_from_dict = ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission.from_dict(api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


