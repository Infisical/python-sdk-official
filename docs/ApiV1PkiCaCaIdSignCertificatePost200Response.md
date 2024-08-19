# ApiV1PkiCaCaIdSignCertificatePost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The issued certificate | 
**issuing_ca_certificate** | **str** | The certificate of the issuing CA | 
**certificate_chain** | **str** | The certificate chain of the issued certificate | 
**serial_number** | **str** | The serial number of the issued certificate | 

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_ca_id_sign_certificate_post200_response import ApiV1PkiCaCaIdSignCertificatePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaCaIdSignCertificatePost200Response from a JSON string
api_v1_pki_ca_ca_id_sign_certificate_post200_response_instance = ApiV1PkiCaCaIdSignCertificatePost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaCaIdSignCertificatePost200Response.to_json()

# convert the object into a dict
api_v1_pki_ca_ca_id_sign_certificate_post200_response_dict = api_v1_pki_ca_ca_id_sign_certificate_post200_response_instance.to_dict()
# create an instance of ApiV1PkiCaCaIdSignCertificatePost200Response from a dict
api_v1_pki_ca_ca_id_sign_certificate_post200_response_from_dict = ApiV1PkiCaCaIdSignCertificatePost200Response.from_dict(api_v1_pki_ca_ca_id_sign_certificate_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


