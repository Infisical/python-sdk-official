# ApiV1PkiCaPost200ResponseCa


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**parent_ca_id** | **str** |  | [optional] 
**project_id** | **str** |  | 
**type** | **str** |  | 
**status** | **str** |  | 
**friendly_name** | **str** |  | 
**organization** | **str** |  | 
**ou** | **str** |  | 
**country** | **str** |  | 
**province** | **str** |  | 
**locality** | **str** |  | 
**common_name** | **str** |  | 
**dn** | **str** |  | 
**serial_number** | **str** |  | [optional] 
**max_path_length** | **float** |  | [optional] 
**key_algorithm** | **str** |  | 
**not_before** | **datetime** |  | [optional] 
**not_after** | **datetime** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_pki_ca_post200_response_ca import ApiV1PkiCaPost200ResponseCa

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PkiCaPost200ResponseCa from a JSON string
api_v1_pki_ca_post200_response_ca_instance = ApiV1PkiCaPost200ResponseCa.from_json(json)
# print the JSON string representation of the object
print ApiV1PkiCaPost200ResponseCa.to_json()

# convert the object into a dict
api_v1_pki_ca_post200_response_ca_dict = api_v1_pki_ca_post200_response_ca_instance.to_dict()
# create an instance of ApiV1PkiCaPost200ResponseCa from a dict
api_v1_pki_ca_post200_response_ca_from_dict = ApiV1PkiCaPost200ResponseCa.from_dict(api_v1_pki_ca_post200_response_ca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


