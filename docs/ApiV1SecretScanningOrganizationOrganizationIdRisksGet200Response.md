# ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risks** | [**List[ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner]**](ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_scanning_organization_organization_id_risks_get200_response import ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response from a JSON string
api_v1_secret_scanning_organization_organization_id_risks_get200_response_instance = ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response.to_json()

# convert the object into a dict
api_v1_secret_scanning_organization_organization_id_risks_get200_response_dict = api_v1_secret_scanning_organization_organization_id_risks_get200_response_instance.to_dict()
# create an instance of ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response from a dict
api_v1_secret_scanning_organization_organization_id_risks_get200_response_from_dict = ApiV1SecretScanningOrganizationOrganizationIdRisksGet200Response.from_dict(api_v1_secret_scanning_organization_organization_id_risks_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


