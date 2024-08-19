# ApiV1PkiCertificatesSerialNumberRevokePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revocation_reason** | **str** | The reason for revoking the certificate. | 

## Example

```python
from infisicalapi_client.models.api_v1_pki_certificates_serial_number_revoke_post_request import ApiV1PkiCertificatesSerialNumberRevokePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCertificatesSerialNumberRevokePostRequest from a JSON string
api_v1_pki_certificates_serial_number_revoke_post_request_instance = ApiV1PkiCertificatesSerialNumberRevokePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCertificatesSerialNumberRevokePostRequest.to_json()

# convert the object into a dict
api_v1_pki_certificates_serial_number_revoke_post_request_dict = api_v1_pki_certificates_serial_number_revoke_post_request_instance.to_dict()
# create an instance of ApiV1PkiCertificatesSerialNumberRevokePostRequest from a dict
api_v1_pki_certificates_serial_number_revoke_post_request_from_dict = ApiV1PkiCertificatesSerialNumberRevokePostRequest.from_dict(api_v1_pki_certificates_serial_number_revoke_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


