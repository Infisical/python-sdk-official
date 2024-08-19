# ApiV1PkiCertificatesSerialNumberRevokePost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**serial_number** | **str** | The serial number of the revoked certificate. | 
**revoked_at** | **datetime** | The date and time when the certificate was revoked | 

## Example

```python
from infisicalapi_client.models.api_v1_pki_certificates_serial_number_revoke_post200_response import ApiV1PkiCertificatesSerialNumberRevokePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCertificatesSerialNumberRevokePost200Response from a JSON string
api_v1_pki_certificates_serial_number_revoke_post200_response_instance = ApiV1PkiCertificatesSerialNumberRevokePost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCertificatesSerialNumberRevokePost200Response.to_json()

# convert the object into a dict
api_v1_pki_certificates_serial_number_revoke_post200_response_dict = api_v1_pki_certificates_serial_number_revoke_post200_response_instance.to_dict()
# create an instance of ApiV1PkiCertificatesSerialNumberRevokePost200Response from a dict
api_v1_pki_certificates_serial_number_revoke_post200_response_from_dict = ApiV1PkiCertificatesSerialNumberRevokePost200Response.from_dict(api_v1_pki_certificates_serial_number_revoke_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


