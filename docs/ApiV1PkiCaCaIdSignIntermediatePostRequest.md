# ApiV1PkiCaCaIdSignIntermediatePostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | The pem-encoded CSR to sign with the CA | 
**not_before** | **str** | The date and time when the intermediate CA becomes valid in YYYY-MM-DDTHH:mm:ss.sssZ format | [optional] 
**not_after** | **str** | The date and time when the intermediate CA expires in YYYY-MM-DDTHH:mm:ss.sssZ format | 
**max_path_length** | **float** | The maximum number of intermediate CAs that may follow this CA in the certificate / CA chain. A maxPathLength of -1 implies no path limit on the chain. | [optional] [default to -1]

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_ca_id_sign_intermediate_post_request import ApiV1PkiCaCaIdSignIntermediatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaCaIdSignIntermediatePostRequest from a JSON string
api_v1_pki_ca_ca_id_sign_intermediate_post_request_instance = ApiV1PkiCaCaIdSignIntermediatePostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaCaIdSignIntermediatePostRequest.to_json()

# convert the object into a dict
api_v1_pki_ca_ca_id_sign_intermediate_post_request_dict = api_v1_pki_ca_ca_id_sign_intermediate_post_request_instance.to_dict()
# create an instance of ApiV1PkiCaCaIdSignIntermediatePostRequest from a dict
api_v1_pki_ca_ca_id_sign_intermediate_post_request_from_dict = ApiV1PkiCaCaIdSignIntermediatePostRequest.from_dict(api_v1_pki_ca_ca_id_sign_intermediate_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


