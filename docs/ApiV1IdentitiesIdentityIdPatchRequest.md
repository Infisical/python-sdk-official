# ApiV1IdentitiesIdentityIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the identity. | [optional] 
**role** | **str** | The new role of the identity. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_identities_identity_id_patch_request import ApiV1IdentitiesIdentityIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IdentitiesIdentityIdPatchRequest from a JSON string
api_v1_identities_identity_id_patch_request_instance = ApiV1IdentitiesIdentityIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1IdentitiesIdentityIdPatchRequest.to_json()

# convert the object into a dict
api_v1_identities_identity_id_patch_request_dict = api_v1_identities_identity_id_patch_request_instance.to_dict()
# create an instance of ApiV1IdentitiesIdentityIdPatchRequest from a dict
api_v1_identities_identity_id_patch_request_from_dict = ApiV1IdentitiesIdentityIdPatchRequest.from_dict(api_v1_identities_identity_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


