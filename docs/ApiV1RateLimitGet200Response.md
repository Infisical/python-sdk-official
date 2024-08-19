# ApiV1RateLimitGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_limit** | [**ApiV1RateLimitGet200ResponseRateLimit**](ApiV1RateLimitGet200ResponseRateLimit.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_rate_limit_get200_response import ApiV1RateLimitGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1RateLimitGet200Response from a JSON string
api_v1_rate_limit_get200_response_instance = ApiV1RateLimitGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1RateLimitGet200Response.to_json()

# convert the object into a dict
api_v1_rate_limit_get200_response_dict = api_v1_rate_limit_get200_response_instance.to_dict()
# create an instance of ApiV1RateLimitGet200Response from a dict
api_v1_rate_limit_get200_response_from_dict = ApiV1RateLimitGet200Response.from_dict(api_v1_rate_limit_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


