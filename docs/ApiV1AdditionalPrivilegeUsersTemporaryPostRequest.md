# ApiV1AdditionalPrivilegeUsersTemporaryPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_membership_id** | **str** | Project membership id of user | 
**slug** | **str** | The slug of the privilege to create. | [optional] 
**permissions** | **List[str]** | The permission object for the privilege. Refer https://casl.js.org/v6/en/guide/define-rules#the-shape-of-raw-rule to understand the shape | 
**temporary_mode** | **str** | Type of temporary access given. Types: relative | 
**temporary_range** | **str** | TTL for the temporay time. Eg: 1m, 1h, 1d | 
**temporary_access_start_time** | **datetime** | ISO time for which temporary access should begin. | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_users_temporary_post_request import ApiV1AdditionalPrivilegeUsersTemporaryPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeUsersTemporaryPostRequest from a JSON string
api_v1_additional_privilege_users_temporary_post_request_instance = ApiV1AdditionalPrivilegeUsersTemporaryPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeUsersTemporaryPostRequest.to_json()

# convert the object into a dict
api_v1_additional_privilege_users_temporary_post_request_dict = api_v1_additional_privilege_users_temporary_post_request_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeUsersTemporaryPostRequest from a dict
api_v1_additional_privilege_users_temporary_post_request_from_dict = ApiV1AdditionalPrivilegeUsersTemporaryPostRequest.from_dict(api_v1_additional_privilege_users_temporary_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


