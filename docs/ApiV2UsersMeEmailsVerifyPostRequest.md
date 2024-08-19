# ApiV2UsersMeEmailsVerifyPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v2_users_me_emails_verify_post_request import ApiV2UsersMeEmailsVerifyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UsersMeEmailsVerifyPostRequest from a JSON string
api_v2_users_me_emails_verify_post_request_instance = ApiV2UsersMeEmailsVerifyPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV2UsersMeEmailsVerifyPostRequest.to_json()

# convert the object into a dict
api_v2_users_me_emails_verify_post_request_dict = api_v2_users_me_emails_verify_post_request_instance.to_dict()
# create an instance of ApiV2UsersMeEmailsVerifyPostRequest from a dict
api_v2_users_me_emails_verify_post_request_from_dict = ApiV2UsersMeEmailsVerifyPostRequest.from_dict(api_v2_users_me_emails_verify_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


