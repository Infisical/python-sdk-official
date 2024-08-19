# ApiV3AuthLogin2Post200ResponseAnyOf1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_enabled** | **bool** |  | 
**encryption_version** | **float** |  | [optional] [default to 1]
**protected_key** | **str** |  | 
**protected_key_iv** | **str** |  | 
**protected_key_tag** | **str** |  | 
**public_key** | **str** |  | 
**encrypted_private_key** | **str** |  | 
**iv** | **str** |  | 
**tag** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v3_auth_login2_post200_response_any_of1 import ApiV3AuthLogin2Post200ResponseAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3AuthLogin2Post200ResponseAnyOf1 from a JSON string
api_v3_auth_login2_post200_response_any_of1_instance = ApiV3AuthLogin2Post200ResponseAnyOf1.from_json(json)
# print the JSON string representation of the object
print ApiV3AuthLogin2Post200ResponseAnyOf1.to_json()

# convert the object into a dict
api_v3_auth_login2_post200_response_any_of1_dict = api_v3_auth_login2_post200_response_any_of1_instance.to_dict()
# create an instance of ApiV3AuthLogin2Post200ResponseAnyOf1 from a dict
api_v3_auth_login2_post200_response_any_of1_from_dict = ApiV3AuthLogin2Post200ResponseAnyOf1.from_dict(api_v3_auth_login2_post200_response_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


