# ApiV2UsersMeMfaPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_mfa_enabled** | **bool** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_mfa_patch_request import ApiV2UsersMeMfaPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeMfaPatchRequest from a JSON string
api_v2_users_me_mfa_patch_request_instance = ApiV2UsersMeMfaPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeMfaPatchRequest.to_json()

# convert the object into a dict
api_v2_users_me_mfa_patch_request_dict = api_v2_users_me_mfa_patch_request_instance.to_dict()
# create an instance of ApiV2UsersMeMfaPatchRequest from a dict
api_v2_users_me_mfa_patch_request_from_dict = ApiV2UsersMeMfaPatchRequest.from_dict(api_v2_users_me_mfa_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


