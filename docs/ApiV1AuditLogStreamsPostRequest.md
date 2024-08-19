# ApiV1AuditLogStreamsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTP URL to push logs to. | 
**headers** | [**List[ApiV1AuditLogStreamsPostRequestHeadersInner]**](ApiV1AuditLogStreamsPostRequestHeadersInner.md) | The HTTP headers attached for the external prrovider requests. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_audit_log_streams_post_request import ApiV1AuditLogStreamsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuditLogStreamsPostRequest from a JSON string
api_v1_audit_log_streams_post_request_instance = ApiV1AuditLogStreamsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuditLogStreamsPostRequest.to_json()

# convert the object into a dict
api_v1_audit_log_streams_post_request_dict = api_v1_audit_log_streams_post_request_instance.to_dict()
# create an instance of ApiV1AuditLogStreamsPostRequest from a dict
api_v1_audit_log_streams_post_request_from_dict = ApiV1AuditLogStreamsPostRequest.from_dict(api_v1_audit_log_streams_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


