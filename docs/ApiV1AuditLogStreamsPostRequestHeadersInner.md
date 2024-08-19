# ApiV1AuditLogStreamsPostRequestHeadersInner

The HTTP headers attached for the external prrovider requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The HTTP header key name. | 
**value** | **str** | The HTTP header value. | 

## Example

```python
from infisicalapi_client.models.api_v1_audit_log_streams_post_request_headers_inner import ApiV1AuditLogStreamsPostRequestHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuditLogStreamsPostRequestHeadersInner from a JSON string
api_v1_audit_log_streams_post_request_headers_inner_instance = ApiV1AuditLogStreamsPostRequestHeadersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1AuditLogStreamsPostRequestHeadersInner.to_json()

# convert the object into a dict
api_v1_audit_log_streams_post_request_headers_inner_dict = api_v1_audit_log_streams_post_request_headers_inner_instance.to_dict()
# create an instance of ApiV1AuditLogStreamsPostRequestHeadersInner from a dict
api_v1_audit_log_streams_post_request_headers_inner_from_dict = ApiV1AuditLogStreamsPostRequestHeadersInner.from_dict(api_v1_audit_log_streams_post_request_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


