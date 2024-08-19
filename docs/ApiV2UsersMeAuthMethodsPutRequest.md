# ApiV2UsersMeAuthMethodsPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_methods** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_auth_methods_put_request import ApiV2UsersMeAuthMethodsPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeAuthMethodsPutRequest from a JSON string
api_v2_users_me_auth_methods_put_request_instance = ApiV2UsersMeAuthMethodsPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeAuthMethodsPutRequest.to_json()

# convert the object into a dict
api_v2_users_me_auth_methods_put_request_dict = api_v2_users_me_auth_methods_put_request_instance.to_dict()
# create an instance of ApiV2UsersMeAuthMethodsPutRequest from a dict
api_v2_users_me_auth_methods_put_request_from_dict = ApiV2UsersMeAuthMethodsPutRequest.from_dict(api_v2_users_me_auth_methods_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


