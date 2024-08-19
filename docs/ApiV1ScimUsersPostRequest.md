# ApiV1ScimUsersPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**user_name** | **str** |  | 
**name** | [**ApiV1ScimUsersGet200ResponseResourcesInnerName**](ApiV1ScimUsersGet200ResponseResourcesInnerName.md) |  | 
**emails** | [**List[ApiV1ScimUsersPostRequestEmailsInner]**](ApiV1ScimUsersPostRequestEmailsInner.md) |  | [optional] 
**active** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_users_post_request import ApiV1ScimUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimUsersPostRequest from a JSON string
api_v1_scim_users_post_request_instance = ApiV1ScimUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimUsersPostRequest.to_json()

# convert the object into a dict
api_v1_scim_users_post_request_dict = api_v1_scim_users_post_request_instance.to_dict()
# create an instance of ApiV1ScimUsersPostRequest from a dict
api_v1_scim_users_post_request_from_dict = ApiV1ScimUsersPostRequest.from_dict(api_v1_scim_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


