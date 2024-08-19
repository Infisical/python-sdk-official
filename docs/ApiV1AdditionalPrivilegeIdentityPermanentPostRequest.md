# ApiV1AdditionalPrivilegeIdentityPermanentPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The ID of the identity to create. | 
**project_slug** | **str** | The slug of the project of the identity in. | 
**slug** | **str** | The slug of the privilege to create. | [optional] 
**permissions** | [**List[ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner]**](ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.md) | @deprecated - use privilegePermission The permission object for the privilege. - Read secrets &#x60;&#x60;&#x60; { \&quot;permissions\&quot;: [{\&quot;action\&quot;: \&quot;read\&quot;, \&quot;subject\&quot;: \&quot;secrets\&quot;]} &#x60;&#x60;&#x60; - Read and Write secrets &#x60;&#x60;&#x60; { \&quot;permissions\&quot;: [{\&quot;action\&quot;: \&quot;read\&quot;, \&quot;subject\&quot;: \&quot;secrets\&quot;], {\&quot;action\&quot;: \&quot;write\&quot;, \&quot;subject\&quot;: \&quot;secrets\&quot;]} &#x60;&#x60;&#x60; - Read secrets scoped to an environment and secret path &#x60;&#x60;&#x60; - { \&quot;permissions\&quot;: [{\&quot;action\&quot;: \&quot;read\&quot;, \&quot;subject\&quot;: \&quot;secrets\&quot;, \&quot;conditions\&quot;: { \&quot;environment\&quot;: \&quot;dev\&quot;, \&quot;secretPath\&quot;: { \&quot;$glob\&quot;: \&quot;/\&quot; } }}] } &#x60;&#x60;&#x60;  | [optional] 
**privilege_permission** | [**ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission**](ApiV1AdditionalPrivilegeIdentityPermanentPostRequestPrivilegePermission.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_permanent_post_request import ApiV1AdditionalPrivilegeIdentityPermanentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPostRequest from a JSON string
api_v1_additional_privilege_identity_permanent_post_request_instance = ApiV1AdditionalPrivilegeIdentityPermanentPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityPermanentPostRequest.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_permanent_post_request_dict = api_v1_additional_privilege_identity_permanent_post_request_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityPermanentPostRequest from a dict
api_v1_additional_privilege_identity_permanent_post_request_from_dict = ApiV1AdditionalPrivilegeIdentityPermanentPostRequest.from_dict(api_v1_additional_privilege_identity_permanent_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


