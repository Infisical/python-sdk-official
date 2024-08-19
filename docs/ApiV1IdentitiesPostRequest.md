# ApiV1IdentitiesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the identity to create. | 
**organization_id** | **str** | The organization ID to which the identity belongs. | 
**role** | **str** | The role of the identity. Possible values are &#39;no-access&#39;, &#39;member&#39;, and &#39;admin&#39;. | [optional] [default to 'no-access']

## Example

```python
from infisicalapi_client.models.api_v1_identities_post_request import ApiV1IdentitiesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IdentitiesPostRequest from a JSON string
api_v1_identities_post_request_instance = ApiV1IdentitiesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1IdentitiesPostRequest.to_json()

# convert the object into a dict
api_v1_identities_post_request_dict = api_v1_identities_post_request_instance.to_dict()
# create an instance of ApiV1IdentitiesPostRequest from a dict
api_v1_identities_post_request_from_dict = ApiV1IdentitiesPostRequest.from_dict(api_v1_identities_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


