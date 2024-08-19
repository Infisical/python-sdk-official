# ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**ca_id** | **str** |  | 
**status** | **str** |  | 
**serial_number** | **str** |  | 
**friendly_name** | **str** |  | 
**common_name** | **str** |  | 
**not_before** | **datetime** |  | 
**not_after** | **datetime** |  | 
**revoked_at** | **datetime** |  | [optional] 
**revocation_reason** | **float** |  | [optional] 
**alt_names** | **str** |  | [optional] [default to '']

## Example

```python
from infisicalapi_client.models.api_v1_pki_certificates_serial_number_get200_response_certificate import ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate from a JSON string
api_v1_pki_certificates_serial_number_get200_response_certificate_instance = ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate.to_json()

# convert the object into a dict
api_v1_pki_certificates_serial_number_get200_response_certificate_dict = api_v1_pki_certificates_serial_number_get200_response_certificate_instance.to_dict()
# create an instance of ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate from a dict
api_v1_pki_certificates_serial_number_get200_response_certificate_from_dict = ApiV1PkiCertificatesSerialNumberGet200ResponseCertificate.from_dict(api_v1_pki_certificates_serial_number_get200_response_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


