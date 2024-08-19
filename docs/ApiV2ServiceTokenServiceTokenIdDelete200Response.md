# ApiV2ServiceTokenServiceTokenIdDelete200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token_data** | [**ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner**](ApiV1WorkspaceWorkspaceIdServiceTokenDataGet200ResponseServiceTokenDataInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v2_service_token_service_token_id_delete200_response import ApiV2ServiceTokenServiceTokenIdDelete200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ServiceTokenServiceTokenIdDelete200Response from a JSON string
api_v2_service_token_service_token_id_delete200_response_instance = ApiV2ServiceTokenServiceTokenIdDelete200Response.from_json(json)
# print the JSON string representation of the object
print ApiV2ServiceTokenServiceTokenIdDelete200Response.to_json()

# convert the object into a dict
api_v2_service_token_service_token_id_delete200_response_dict = api_v2_service_token_service_token_id_delete200_response_instance.to_dict()
# create an instance of ApiV2ServiceTokenServiceTokenIdDelete200Response from a dict
api_v2_service_token_service_token_id_delete200_response_from_dict = ApiV2ServiceTokenServiceTokenIdDelete200Response.from_dict(api_v2_service_token_service_token_id_delete200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


