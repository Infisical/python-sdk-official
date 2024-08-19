# ApiV1PkiCaCaIdImportCertificatePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The certificate body to import | 
**certificate_chain** | **str** | The certificate chain to import | 

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_ca_id_import_certificate_post_request import ApiV1PkiCaCaIdImportCertificatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaCaIdImportCertificatePostRequest from a JSON string
api_v1_pki_ca_ca_id_import_certificate_post_request_instance = ApiV1PkiCaCaIdImportCertificatePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaCaIdImportCertificatePostRequest.to_json()

# convert the object into a dict
api_v1_pki_ca_ca_id_import_certificate_post_request_dict = api_v1_pki_ca_ca_id_import_certificate_post_request_instance.to_dict()
# create an instance of ApiV1PkiCaCaIdImportCertificatePostRequest from a dict
api_v1_pki_ca_ca_id_import_certificate_post_request_from_dict = ApiV1PkiCaCaIdImportCertificatePostRequest.from_dict(api_v1_pki_ca_ca_id_import_certificate_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


