# ApiV1RateLimitPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_rate_limit** | **float** |  | 
**write_rate_limit** | **float** |  | 
**secrets_rate_limit** | **float** |  | 
**auth_rate_limit** | **float** |  | 
**invite_user_rate_limit** | **float** |  | 
**mfa_rate_limit** | **float** |  | 
**public_endpoint_limit** | **float** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_rate_limit_put_request import ApiV1RateLimitPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RateLimitPutRequest from a JSON string
api_v1_rate_limit_put_request_instance = ApiV1RateLimitPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1RateLimitPutRequest.to_json()

# convert the object into a dict
api_v1_rate_limit_put_request_dict = api_v1_rate_limit_put_request_instance.to_dict()
# create an instance of ApiV1RateLimitPutRequest from a dict
api_v1_rate_limit_put_request_from_dict = ApiV1RateLimitPutRequest.from_dict(api_v1_rate_limit_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


