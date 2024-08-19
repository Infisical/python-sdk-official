# ApiV1IdentitiesPost200ResponseIdentity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**auth_method** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_identities_post200_response_identity import ApiV1IdentitiesPost200ResponseIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IdentitiesPost200ResponseIdentity from a JSON string
api_v1_identities_post200_response_identity_instance = ApiV1IdentitiesPost200ResponseIdentity.from_json(json)
# print the JSON string representation of the object
print ApiV1IdentitiesPost200ResponseIdentity.to_json()

# convert the object into a dict
api_v1_identities_post200_response_identity_dict = api_v1_identities_post200_response_identity_instance.to_dict()
# create an instance of ApiV1IdentitiesPost200ResponseIdentity from a dict
api_v1_identities_post200_response_identity_from_dict = ApiV1IdentitiesPost200ResponseIdentity.from_dict(api_v1_identities_post200_response_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


