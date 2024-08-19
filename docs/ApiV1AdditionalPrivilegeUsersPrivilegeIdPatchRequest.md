# ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The slug of the privilege to create. | [optional] 
**permissions** | **List[str]** | The permission object for the privilege. Refer https://casl.js.org/v6/en/guide/define-rules#the-shape-of-raw-rule to understand the shape | [optional] 
**is_temporary** | **bool** | Whether the privilege is temporary. | [optional] 
**temporary_mode** | **str** | Type of temporary access given. Types: relative | [optional] 
**temporary_range** | **str** | TTL for the temporay time. Eg: 1m, 1h, 1d | [optional] 
**temporary_access_start_time** | **datetime** | ISO time for which temporary access should begin. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_users_privilege_id_patch_request import ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest from a JSON string
api_v1_additional_privilege_users_privilege_id_patch_request_instance = ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest.to_json()

# convert the object into a dict
api_v1_additional_privilege_users_privilege_id_patch_request_dict = api_v1_additional_privilege_users_privilege_id_patch_request_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest from a dict
api_v1_additional_privilege_users_privilege_id_patch_request_from_dict = ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest.from_dict(api_v1_additional_privilege_users_privilege_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


