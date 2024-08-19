# ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **str** | The renew TTL that gets added with current expiry (ensure it&#39;s below max TTL) for a total less than creation time + max TTL. | [optional] 
**project_slug** | **str** | The slug of the project of the dynamic secret in. | 
**path** | **str** | The path of the dynamic secret in. | [optional] [default to '/']
**environment_slug** | **str** | The slug of the environment of the dynamic secret in. | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_leases_lease_id_renew_post_request import ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest from a JSON string
api_v1_dynamic_secrets_leases_lease_id_renew_post_request_instance = ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_leases_lease_id_renew_post_request_dict = api_v1_dynamic_secrets_leases_lease_id_renew_post_request_instance.to_dict()
# create an instance of ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest from a dict
api_v1_dynamic_secrets_leases_lease_id_renew_post_request_from_dict = ApiV1DynamicSecretsLeasesLeaseIdRenewPostRequest.from_dict(api_v1_dynamic_secrets_leases_lease_id_renew_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


