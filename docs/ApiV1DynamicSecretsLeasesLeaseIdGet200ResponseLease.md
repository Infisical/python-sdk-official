# ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **float** |  | 
**external_entity_id** | **str** |  | 
**expire_at** | **datetime** |  | 
**status** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**dynamic_secret_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**dynamic_secret** | [**ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner**](ApiV1DynamicSecretsGet200ResponseDynamicSecretsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_leases_lease_id_get200_response_lease import ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease from a JSON string
api_v1_dynamic_secrets_leases_lease_id_get200_response_lease_instance = ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_leases_lease_id_get200_response_lease_dict = api_v1_dynamic_secrets_leases_lease_id_get200_response_lease_instance.to_dict()
# create an instance of ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease from a dict
api_v1_dynamic_secrets_leases_lease_id_get200_response_lease_from_dict = ApiV1DynamicSecretsLeasesLeaseIdGet200ResponseLease.from_dict(api_v1_dynamic_secrets_leases_lease_id_get200_response_lease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


