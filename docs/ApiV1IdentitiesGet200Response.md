# ApiV1IdentitiesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | [**List[ApiV1IdentitiesGet200ResponseIdentitiesInner]**](ApiV1IdentitiesGet200ResponseIdentitiesInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_identities_get200_response import ApiV1IdentitiesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IdentitiesGet200Response from a JSON string
api_v1_identities_get200_response_instance = ApiV1IdentitiesGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1IdentitiesGet200Response.to_json()

# convert the object into a dict
api_v1_identities_get200_response_dict = api_v1_identities_get200_response_instance.to_dict()
# create an instance of ApiV1IdentitiesGet200Response from a dict
api_v1_identities_get200_response_from_dict = ApiV1IdentitiesGet200Response.from_dict(api_v1_identities_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


