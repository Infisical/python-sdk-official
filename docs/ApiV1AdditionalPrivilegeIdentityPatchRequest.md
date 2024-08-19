# ApiV1AdditionalPrivilegeIdentityPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege_slug** | **str** | The slug of the privilege to update. | 
**identity_id** | **str** | The ID of the identity to update. | 
**project_slug** | **str** | The slug of the project of the identity in. | 
**privilege_details** | [**ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails**](ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_patch_request import ApiV1AdditionalPrivilegeIdentityPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityPatchRequest from a JSON string
api_v1_additional_privilege_identity_patch_request_instance = ApiV1AdditionalPrivilegeIdentityPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityPatchRequest.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_patch_request_dict = api_v1_additional_privilege_identity_patch_request_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityPatchRequest from a dict
api_v1_additional_privilege_identity_patch_request_from_dict = ApiV1AdditionalPrivilegeIdentityPatchRequest.from_dict(api_v1_additional_privilege_identity_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


