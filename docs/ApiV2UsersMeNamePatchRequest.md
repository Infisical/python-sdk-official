# ApiV2UsersMeNamePatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_name_patch_request import ApiV2UsersMeNamePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeNamePatchRequest from a JSON string
api_v2_users_me_name_patch_request_instance = ApiV2UsersMeNamePatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeNamePatchRequest.to_json()

# convert the object into a dict
api_v2_users_me_name_patch_request_dict = api_v2_users_me_name_patch_request_instance.to_dict()
# create an instance of ApiV2UsersMeNamePatchRequest from a dict
api_v2_users_me_name_patch_request_from_dict = ApiV2UsersMeNamePatchRequest.from_dict(api_v2_users_me_name_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


