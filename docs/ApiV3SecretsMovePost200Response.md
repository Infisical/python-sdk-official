# ApiV3SecretsMovePost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_source_updated** | **bool** |  | 
**is_destination_updated** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v3_secrets_move_post200_response import ApiV3SecretsMovePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SecretsMovePost200Response from a JSON string
api_v3_secrets_move_post200_response_instance = ApiV3SecretsMovePost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV3SecretsMovePost200Response.to_json()

# convert the object into a dict
api_v3_secrets_move_post200_response_dict = api_v3_secrets_move_post200_response_instance.to_dict()
# create an instance of ApiV3SecretsMovePost200Response from a dict
api_v3_secrets_move_post200_response_from_dict = ApiV3SecretsMovePost200Response.from_dict(api_v3_secrets_move_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


