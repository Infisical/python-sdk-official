# ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_organizations_organization_id_billing_details_patch_request import ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest from a JSON string
api_v1_organizations_organization_id_billing_details_patch_request_instance = ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest.to_json()

# convert the object into a dict
api_v1_organizations_organization_id_billing_details_patch_request_dict = api_v1_organizations_organization_id_billing_details_patch_request_instance.to_dict()
# create an instance of ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest from a dict
api_v1_organizations_organization_id_billing_details_patch_request_from_dict = ApiV1OrganizationsOrganizationIdBillingDetailsPatchRequest.from_dict(api_v1_organizations_organization_id_billing_details_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


