# ApiV1IntegrationAuthAccessTokenPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | The ID of the project to create the integration auth for. | 
**integration** | **str** | The slug of integration for the auth object. | 
**access_id** | **str** | The unique authorized access id of the external integration provider. | [optional] 
**access_token** | **str** | The unique authorized access token of the external integration provider. | [optional] 
**aws_assume_iam_role_arn** | **str** | The AWS IAM Role to be assumed by Infisical | [optional] 
**url** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**refresh_token** | **str** | The refresh token for integration authorization. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_integration_auth_access_token_post_request import ApiV1IntegrationAuthAccessTokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IntegrationAuthAccessTokenPostRequest from a JSON string
api_v1_integration_auth_access_token_post_request_instance = ApiV1IntegrationAuthAccessTokenPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1IntegrationAuthAccessTokenPostRequest.to_json()

# convert the object into a dict
api_v1_integration_auth_access_token_post_request_dict = api_v1_integration_auth_access_token_post_request_instance.to_dict()
# create an instance of ApiV1IntegrationAuthAccessTokenPostRequest from a dict
api_v1_integration_auth_access_token_post_request_from_dict = ApiV1IntegrationAuthAccessTokenPostRequest.from_dict(api_v1_integration_auth_access_token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


