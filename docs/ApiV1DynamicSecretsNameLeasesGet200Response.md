# ApiV1DynamicSecretsNameLeasesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leases** | [**List[ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner]**](ApiV1DynamicSecretsNameLeasesGet200ResponseLeasesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_dynamic_secrets_name_leases_get200_response import ApiV1DynamicSecretsNameLeasesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DynamicSecretsNameLeasesGet200Response from a JSON string
api_v1_dynamic_secrets_name_leases_get200_response_instance = ApiV1DynamicSecretsNameLeasesGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1DynamicSecretsNameLeasesGet200Response.to_json()

# convert the object into a dict
api_v1_dynamic_secrets_name_leases_get200_response_dict = api_v1_dynamic_secrets_name_leases_get200_response_instance.to_dict()
# create an instance of ApiV1DynamicSecretsNameLeasesGet200Response from a dict
api_v1_dynamic_secrets_name_leases_get200_response_from_dict = ApiV1DynamicSecretsNameLeasesGet200Response.from_dict(api_v1_dynamic_secrets_name_leases_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


