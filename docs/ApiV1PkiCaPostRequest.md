# ApiV1PkiCaPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** | Slug of the project to create the CA in. | 
**type** | **str** | The type of CA to create | 
**friendly_name** | **str** | A friendly name for the CA | [optional] 
**common_name** | **str** | The common name (CN) for the CA | 
**organization** | **str** | The organization (O) for the CA | 
**ou** | **str** | The organization unit (OU) for the CA | 
**country** | **str** | The country name (C) for the CA | 
**province** | **str** | The state of province name for the CA | 
**locality** | **str** | The locality name for the CA | 
**not_before** | **str** | The date and time when the CA becomes valid in YYYY-MM-DDTHH:mm:ss.sssZ format | [optional] 
**not_after** | **str** | The date and time when the CA expires in YYYY-MM-DDTHH:mm:ss.sssZ format | [optional] 
**max_path_length** | **float** | The maximum number of intermediate CAs that may follow this CA in the certificate / CA chain. A maxPathLength of -1 implies no path limit on the chain. | [optional] [default to -1]
**key_algorithm** | **str** | The type of public key algorithm and size, in bits, of the key pair for the CA; when you create an intermediate CA, you must use a key algorithm supported by the parent CA. | [optional] [default to 'RSA_2048']

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_post_request import ApiV1PkiCaPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaPostRequest from a JSON string
api_v1_pki_ca_post_request_instance = ApiV1PkiCaPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaPostRequest.to_json()

# convert the object into a dict
api_v1_pki_ca_post_request_dict = api_v1_pki_ca_post_request_instance.to_dict()
# create an instance of ApiV1PkiCaPostRequest from a dict
api_v1_pki_ca_post_request_from_dict = ApiV1PkiCaPostRequest.from_dict(api_v1_pki_ca_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


