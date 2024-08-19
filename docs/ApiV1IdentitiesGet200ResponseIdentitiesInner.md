# ApiV1IdentitiesGet200ResponseIdentitiesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 
**role_id** | **str** |  | [optional] 
**org_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**identity_id** | **str** |  | 
**custom_role** | [**ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole**](ApiV1OrganizationOrganizationIdGroupsGet200ResponseGroupsInnerCustomRole.md) |  | [optional] 
**identity** | [**ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity**](ApiV1IdentitiesGet200ResponseIdentitiesInnerIdentity.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_identities_get200_response_identities_inner import ApiV1IdentitiesGet200ResponseIdentitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IdentitiesGet200ResponseIdentitiesInner from a JSON string
api_v1_identities_get200_response_identities_inner_instance = ApiV1IdentitiesGet200ResponseIdentitiesInner.from_json(json)
# print the JSON string representation of the object
print ApiV1IdentitiesGet200ResponseIdentitiesInner.to_json()

# convert the object into a dict
api_v1_identities_get200_response_identities_inner_dict = api_v1_identities_get200_response_identities_inner_instance.to_dict()
# create an instance of ApiV1IdentitiesGet200ResponseIdentitiesInner from a dict
api_v1_identities_get200_response_identities_inner_from_dict = ApiV1IdentitiesGet200ResponseIdentitiesInner.from_dict(api_v1_identities_get200_response_identities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


