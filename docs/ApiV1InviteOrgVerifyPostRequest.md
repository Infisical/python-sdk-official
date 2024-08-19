# ApiV1InviteOrgVerifyPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**organization_id** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_invite_org_verify_post_request import ApiV1InviteOrgVerifyPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1InviteOrgVerifyPostRequest from a JSON string
api_v1_invite_org_verify_post_request_instance = ApiV1InviteOrgVerifyPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1InviteOrgVerifyPostRequest.to_json()

# convert the object into a dict
api_v1_invite_org_verify_post_request_dict = api_v1_invite_org_verify_post_request_instance.to_dict()
# create an instance of ApiV1InviteOrgVerifyPostRequest from a dict
api_v1_invite_org_verify_post_request_from_dict = ApiV1InviteOrgVerifyPostRequest.from_dict(api_v1_invite_org_verify_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


