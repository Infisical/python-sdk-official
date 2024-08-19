# ApiV1OrganizationOrganizationIdPermissionsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership** | [**ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership**](ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership.md) |  | 
**permissions** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_permissions_get200_response import ApiV1OrganizationOrganizationIdPermissionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdPermissionsGet200Response from a JSON string
api_v1_organization_organization_id_permissions_get200_response_instance = ApiV1OrganizationOrganizationIdPermissionsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdPermissionsGet200Response.to_json()

# convert the object into a dict
api_v1_organization_organization_id_permissions_get200_response_dict = api_v1_organization_organization_id_permissions_get200_response_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdPermissionsGet200Response from a dict
api_v1_organization_organization_id_permissions_get200_response_from_dict = ApiV1OrganizationOrganizationIdPermissionsGet200Response.from_dict(api_v1_organization_organization_id_permissions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


