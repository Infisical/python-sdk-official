# ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**description** | **str** |  | [optional] 
**start_line** | **str** |  | [optional] 
**end_line** | **str** |  | [optional] 
**start_column** | **str** |  | [optional] 
**end_column** | **str** |  | [optional] 
**file** | **str** |  | [optional] 
**symlink_file** | **str** |  | [optional] 
**commit** | **str** |  | [optional] 
**entropy** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**finger_print_without_commit_id** | **str** |  | [optional] 
**is_false_positive** | **bool** |  | [optional] [default to False]
**is_resolved** | **bool** |  | [optional] [default to False]
**risk_owner** | **str** |  | [optional] 
**installation_id** | **str** |  | 
**repository_id** | **str** |  | [optional] 
**repository_link** | **str** |  | [optional] 
**repository_full_name** | **str** |  | [optional] 
**pusher_name** | **str** |  | [optional] 
**pusher_email** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**org_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_scanning_organization_organization_id_risks_get200_response_risks_inner import ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner from a JSON string
api_v1_secret_scanning_organization_organization_id_risks_get200_response_risks_inner_instance = ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner.to_json()

# convert the object into a dict
api_v1_secret_scanning_organization_organization_id_risks_get200_response_risks_inner_dict = api_v1_secret_scanning_organization_organization_id_risks_get200_response_risks_inner_instance.to_dict()
# create an instance of ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner from a dict
api_v1_secret_scanning_organization_organization_id_risks_get200_response_risks_inner_from_dict = ApiV1SecretScanningOrganizationOrganizationIdRisksGet200ResponseRisksInner.from_dict(api_v1_secret_scanning_organization_organization_id_risks_get200_response_risks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


