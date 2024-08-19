# ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**auto_capitalization** | **bool** |  | [optional] [default to True]
**org_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**version** | **float** |  | [optional] [default to 1]
**upgrade_status** | **str** |  | [optional] 
**pit_version_limit** | **float** |  | [optional] [default to 10]
**kms_certificate_key_id** | **str** |  | [optional] 
**audit_logs_retention_days** | **float** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organization_admin_projects_get200_response_projects_inner import ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner from a JSON string
api_v1_organization_admin_projects_get200_response_projects_inner_instance = ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner.to_json()

# convert the object into a dict
api_v1_organization_admin_projects_get200_response_projects_inner_dict = api_v1_organization_admin_projects_get200_response_projects_inner_instance.to_dict()
# create an instance of ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner from a dict
api_v1_organization_admin_projects_get200_response_projects_inner_from_dict = ApiV1OrganizationAdminProjectsGet200ResponseProjectsInner.from_dict(api_v1_organization_admin_projects_get200_response_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


