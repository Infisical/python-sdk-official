# ApiV1RateLimitGet200ResponseRateLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**read_rate_limit** | **float** |  | [optional] [default to 600]
**write_rate_limit** | **float** |  | [optional] [default to 200]
**secrets_rate_limit** | **float** |  | [optional] [default to 60]
**auth_rate_limit** | **float** |  | [optional] [default to 60]
**invite_user_rate_limit** | **float** |  | [optional] [default to 30]
**mfa_rate_limit** | **float** |  | [optional] [default to 20]
**public_endpoint_limit** | **float** |  | [optional] [default to 30]
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_rate_limit_get200_response_rate_limit import ApiV1RateLimitGet200ResponseRateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RateLimitGet200ResponseRateLimit from a JSON string
api_v1_rate_limit_get200_response_rate_limit_instance = ApiV1RateLimitGet200ResponseRateLimit.from_json(json)
# print the JSON string representation of the object
print ApiV1RateLimitGet200ResponseRateLimit.to_json()

# convert the object into a dict
api_v1_rate_limit_get200_response_rate_limit_dict = api_v1_rate_limit_get200_response_rate_limit_instance.to_dict()
# create an instance of ApiV1RateLimitGet200ResponseRateLimit from a dict
api_v1_rate_limit_get200_response_rate_limit_from_dict = ApiV1RateLimitGet200ResponseRateLimit.from_dict(api_v1_rate_limit_get200_response_rate_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


