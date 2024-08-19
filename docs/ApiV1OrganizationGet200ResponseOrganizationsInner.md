# ApiV1OrganizationGet200ResponseOrganizationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**customer_id** | **str** |  | [optional] 
**slug** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**auth_enforced** | **bool** |  | [optional] [default to False]
**scim_enabled** | **bool** |  | [optional] [default to False]
**kms_default_key_id** | **str** |  | [optional] 
**kms_encrypted_data_key** | **object** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organization_get200_response_organizations_inner import ApiV1OrganizationGet200ResponseOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationGet200ResponseOrganizationsInner from a JSON string
api_v1_organization_get200_response_organizations_inner_instance = ApiV1OrganizationGet200ResponseOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationGet200ResponseOrganizationsInner.to_json()

# convert the object into a dict
api_v1_organization_get200_response_organizations_inner_dict = api_v1_organization_get200_response_organizations_inner_instance.to_dict()
# create an instance of ApiV1OrganizationGet200ResponseOrganizationsInner from a dict
api_v1_organization_get200_response_organizations_inner_from_dict = ApiV1OrganizationGet200ResponseOrganizationsInner.from_dict(api_v1_organization_get200_response_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


