# ApiV2WorkspaceSlugCertificatesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate]**](ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate.md) |  | 
**total_count** | **float** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_slug_certificates_get200_response import ApiV2WorkspaceSlugCertificatesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceSlugCertificatesGet200Response from a JSON string
api_v2_workspace_slug_certificates_get200_response_instance = ApiV2WorkspaceSlugCertificatesGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceSlugCertificatesGet200Response.to_json()

# convert the object into a dict
api_v2_workspace_slug_certificates_get200_response_dict = api_v2_workspace_slug_certificates_get200_response_instance.to_dict()
# create an instance of ApiV2WorkspaceSlugCertificatesGet200Response from a dict
api_v2_workspace_slug_certificates_get200_response_from_dict = ApiV2WorkspaceSlugCertificatesGet200Response.from_dict(api_v2_workspace_slug_certificates_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


