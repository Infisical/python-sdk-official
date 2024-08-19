# ApiV1PkiCaCaIdSignCertificatePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | The pem-encoded CSR to sign with the CA to be used for certificate issuance | 
**friendly_name** | **str** | A friendly name for the certificate | [optional] 
**common_name** | **str** | The common name (CN) for the certificate | [optional] 
**alt_names** | **str** | A comma-delimited list of Subject Alternative Names (SANs) for the certificate; these can be host names or email addresses. | [optional] [default to '']
**ttl** | **str** | The time to live for the certificate such as 1m, 1h, 1d, 1y, ... | 
**not_before** | **str** | The date and time when the certificate becomes valid in YYYY-MM-DDTHH:mm:ss.sssZ format | [optional] 
**not_after** | **str** | The date and time when the certificate expires in YYYY-MM-DDTHH:mm:ss.sssZ format | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_ca_id_sign_certificate_post_request import ApiV1PkiCaCaIdSignCertificatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaCaIdSignCertificatePostRequest from a JSON string
api_v1_pki_ca_ca_id_sign_certificate_post_request_instance = ApiV1PkiCaCaIdSignCertificatePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaCaIdSignCertificatePostRequest.to_json()

# convert the object into a dict
api_v1_pki_ca_ca_id_sign_certificate_post_request_dict = api_v1_pki_ca_ca_id_sign_certificate_post_request_instance.to_dict()
# create an instance of ApiV1PkiCaCaIdSignCertificatePostRequest from a dict
api_v1_pki_ca_ca_id_sign_certificate_post_request_from_dict = ApiV1PkiCaCaIdSignCertificatePostRequest.from_dict(api_v1_pki_ca_ca_id_sign_certificate_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


