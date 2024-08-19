# ApiV1ScimUsersPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemas** | **List[str]** |  | 
**id** | **str** |  | 
**user_name** | **str** |  | 
**name** | [**ApiV1ScimUsersGet200ResponseResourcesInnerName**](ApiV1ScimUsersGet200ResponseResourcesInnerName.md) |  | 
**emails** | [**List[ApiV1ScimUsersPostRequestEmailsInner]**](ApiV1ScimUsersPostRequestEmailsInner.md) |  | 
**display_name** | **str** |  | 
**active** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_scim_users_post200_response import ApiV1ScimUsersPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ScimUsersPost200Response from a JSON string
api_v1_scim_users_post200_response_instance = ApiV1ScimUsersPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1ScimUsersPost200Response.to_json()

# convert the object into a dict
api_v1_scim_users_post200_response_dict = api_v1_scim_users_post200_response_instance.to_dict()
# create an instance of ApiV1ScimUsersPost200Response from a dict
api_v1_scim_users_post200_response_from_dict = ApiV1ScimUsersPost200Response.from_dict(api_v1_scim_users_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


