# ApiV1AuthAwsAuthLoginPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **str** | The ID of the identity to login. | 
**iam_http_request_method** | **str** | The HTTP request method used in the signed request. | [optional] [default to 'POST']
**iam_request_body** | **str** | The base64-encoded body of the signed request. Most likely, the base64-encoding of Action&#x3D;GetCallerIdentity&amp;Version&#x3D;2011-06-15. | 
**iam_request_headers** | **str** | The base64-encoded headers of the sts:GetCallerIdentity signed request. | 

## Example

```python
from infisicalapi_client.models.api_v1_auth_aws_auth_login_post_request import ApiV1AuthAwsAuthLoginPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthAwsAuthLoginPostRequest from a JSON string
api_v1_auth_aws_auth_login_post_request_instance = ApiV1AuthAwsAuthLoginPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthAwsAuthLoginPostRequest.to_json()

# convert the object into a dict
api_v1_auth_aws_auth_login_post_request_dict = api_v1_auth_aws_auth_login_post_request_instance.to_dict()
# create an instance of ApiV1AuthAwsAuthLoginPostRequest from a dict
api_v1_auth_aws_auth_login_post_request_from_dict = ApiV1AuthAwsAuthLoginPostRequest.from_dict(api_v1_auth_aws_auth_login_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


