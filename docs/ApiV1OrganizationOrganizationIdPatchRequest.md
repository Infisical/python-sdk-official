# ApiV1OrganizationOrganizationIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**auth_enforced** | **bool** |  | [optional] 
**scim_enabled** | **bool** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organization_organization_id_patch_request import ApiV1OrganizationOrganizationIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationOrganizationIdPatchRequest from a JSON string
api_v1_organization_organization_id_patch_request_instance = ApiV1OrganizationOrganizationIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationOrganizationIdPatchRequest.to_json()

# convert the object into a dict
api_v1_organization_organization_id_patch_request_dict = api_v1_organization_organization_id_patch_request_instance.to_dict()
# create an instance of ApiV1OrganizationOrganizationIdPatchRequest from a dict
api_v1_organization_organization_id_patch_request_from_dict = ApiV1OrganizationOrganizationIdPatchRequest.from_dict(api_v1_organization_organization_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


