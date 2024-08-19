# ApiV1AdditionalPrivilegeIdentityDeleteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privilege_slug** | **str** | The slug of the privilege to delete. | 
**identity_id** | **str** | The ID of the identity to delete. | 
**project_slug** | **str** | The slug of the project of the identity in. | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_delete_request import ApiV1AdditionalPrivilegeIdentityDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityDeleteRequest from a JSON string
api_v1_additional_privilege_identity_delete_request_instance = ApiV1AdditionalPrivilegeIdentityDeleteRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityDeleteRequest.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_delete_request_dict = api_v1_additional_privilege_identity_delete_request_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityDeleteRequest from a dict
api_v1_additional_privilege_identity_delete_request_from_dict = ApiV1AdditionalPrivilegeIdentityDeleteRequest.from_dict(api_v1_additional_privilege_identity_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


