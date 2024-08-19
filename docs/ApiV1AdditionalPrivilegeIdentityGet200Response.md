# ApiV1AdditionalPrivilegeIdentityGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privileges** | [**List[ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege]**](ApiV1AdditionalPrivilegeIdentityPermanentPost200ResponsePrivilege.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_additional_privilege_identity_get200_response import ApiV1AdditionalPrivilegeIdentityGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AdditionalPrivilegeIdentityGet200Response from a JSON string
api_v1_additional_privilege_identity_get200_response_instance = ApiV1AdditionalPrivilegeIdentityGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1AdditionalPrivilegeIdentityGet200Response.to_json()

# convert the object into a dict
api_v1_additional_privilege_identity_get200_response_dict = api_v1_additional_privilege_identity_get200_response_instance.to_dict()
# create an instance of ApiV1AdditionalPrivilegeIdentityGet200Response from a dict
api_v1_additional_privilege_identity_get200_response_from_dict = ApiV1AdditionalPrivilegeIdentityGet200Response.from_dict(api_v1_additional_privilege_identity_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


