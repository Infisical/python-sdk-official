# ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions

When specified, only matching conditions will be allowed to access given resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | The environment slug this permission should allow. | 
**secret_path** | [**ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditionsSecretPath**](ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInnerConditionsSecretPath.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions import ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions from a JSON string
api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions_instance = ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions_dict = api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions from a dict
api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions_from_dict = ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermissionConditions.from_dict(api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


