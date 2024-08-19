# ApiV1AdditionalPrivilegeUsersPermanentPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_membership_id** | **str** | Project membership id of user | 
**slug** | **str** | The slug of the privilege to create. | [optional] 
**permissions** | **List[str]** | The permission object for the privilege. Refer https://casl.js.org/v6/en/guide/define-rules#the-shape-of-raw-rule to understand the shape | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_users_permanent_post_request import ApiV1AdditionalPrivilegeUsersPermanentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeUsersPermanentPostRequest from a JSON string
api_v1_additional_privilege_users_permanent_post_request_instance = ApiV1AdditionalPrivilegeUsersPermanentPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeUsersPermanentPostRequest.to_json()

# convert the object into a dict
api_v1_additional_privilege_users_permanent_post_request_dict = api_v1_additional_privilege_users_permanent_post_request_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeUsersPermanentPostRequest from a dict
api_v1_additional_privilege_users_permanent_post_request_from_dict = ApiV1AdditionalPrivilegeUsersPermanentPostRequest.from_dict(api_v1_additional_privilege_users_permanent_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


