# ApiV1InviteOrgSignupPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitee_email** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_invite_org_signup_post_request import ApiV1InviteOrgSignupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1InviteOrgSignupPostRequest from a JSON string
api_v1_invite_org_signup_post_request_instance = ApiV1InviteOrgSignupPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1InviteOrgSignupPostRequest.to_json()

# convert the object into a dict
api_v1_invite_org_signup_post_request_dict = api_v1_invite_org_signup_post_request_instance.to_dict()
# create an instance of ApiV1InviteOrgSignupPostRequest from a dict
api_v1_invite_org_signup_post_request_from_dict = ApiV1InviteOrgSignupPostRequest.from_dict(api_v1_invite_org_signup_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


