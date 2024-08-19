# ApiV1OrganizationOrganizationIdRolesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**permissions** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_roles_post_request import ApiV1OrganizationOrganizationIdRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdRolesPostRequest from a JSON string
api_v1_organization_organization_id_roles_post_request_instance = ApiV1OrganizationOrganizationIdRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdRolesPostRequest.to_json()

# convert the object into a dict
api_v1_organization_organization_id_roles_post_request_dict = api_v1_organization_organization_id_roles_post_request_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdRolesPostRequest from a dict
api_v1_organization_organization_id_roles_post_request_from_dict = ApiV1OrganizationOrganizationIdRolesPostRequest.from_dict(api_v1_organization_organization_id_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


