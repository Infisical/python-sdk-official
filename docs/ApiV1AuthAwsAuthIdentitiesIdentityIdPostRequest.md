# ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sts_endpoint** | **str** | The endpoint URL for the AWS STS API. | [optional] [default to 'https://sts.amazonaws.com/']
**allowed_principal_arns** | **str** | The comma-separated list of trusted IAM principal ARNs that are allowed to authenticate with Infisical. | [optional] [default to '']
**allowed_account_ids** | **str** | The comma-separated list of trusted AWS account IDs that are allowed to authenticate with Infisical. | [optional] [default to '']
**access_token_trusted_ips** | [**List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner]**](ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.md) | The IPs or CIDR ranges that access tokens can be used from. | [optional] [default to [{"ipAddress":"0.0.0.0/0"},{"ipAddress":"::/0"}]]
**access_token_ttl** | **int** | The lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_max_ttl** | **int** | The maximum lifetime for an acccess token in seconds. | [optional] [default to 2592000]
**access_token_num_uses_limit** | **int** | The maximum number of times that an access token can be used. | [optional] [default to 0]

## Example

```python
from infisicalapi_client.models.api_v1_auth_aws_auth_identities_identity_id_post_request import ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest from a JSON string
api_v1_auth_aws_auth_identities_identity_id_post_request_instance = ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest.to_json()

# convert the object into a dict
api_v1_auth_aws_auth_identities_identity_id_post_request_dict = api_v1_auth_aws_auth_identities_identity_id_post_request_instance.to_dict()
# create an instance of ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest from a dict
api_v1_auth_aws_auth_identities_identity_id_post_request_from_dict = ApiV1AuthAwsAuthIdentitiesIdentityIdPostRequest.from_dict(api_v1_auth_aws_auth_identities_identity_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


