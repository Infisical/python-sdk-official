# ApiV1OrganizationAdminProjectsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner]**](ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner.md) |  | 
**count** | **float** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_organization_admin_projects_get200_response import ApiV1OrganizationAdminProjectsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationAdminProjectsGet200Response from a JSON string
api_v1_organization_admin_projects_get200_response_instance = ApiV1OrganizationAdminProjectsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationAdminProjectsGet200Response.to_json()

# convert the object into a dict
api_v1_organization_admin_projects_get200_response_dict = api_v1_organization_admin_projects_get200_response_instance.to_dict()
# create an instance of ApiV1OrganizationAdminProjectsGet200Response from a dict
api_v1_organization_admin_projects_get200_response_from_dict = ApiV1OrganizationAdminProjectsGet200Response.from_dict(api_v1_organization_admin_projects_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


