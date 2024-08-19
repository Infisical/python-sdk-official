# ApiV1PkiCaCaIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the CA to update to. This can be one of active or disabled | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_ca_id_patch_request import ApiV1PkiCaCaIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaCaIdPatchRequest from a JSON string
api_v1_pki_ca_ca_id_patch_request_instance = ApiV1PkiCaCaIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaCaIdPatchRequest.to_json()

# convert the object into a dict
api_v1_pki_ca_ca_id_patch_request_dict = api_v1_pki_ca_ca_id_patch_request_instance.to_dict()
# create an instance of ApiV1PkiCaCaIdPatchRequest from a dict
api_v1_pki_ca_ca_id_patch_request_from_dict = ApiV1PkiCaCaIdPatchRequest.from_dict(api_v1_pki_ca_ca_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


