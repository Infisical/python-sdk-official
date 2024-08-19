# ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**headers** | [**List[ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner]**](ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_audit_log_streams_id_get200_response_audit_log_stream import ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream from a JSON string
api_v1_audit_log_streams_id_get200_response_audit_log_stream_instance = ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream.from_json(json)
# print the JSON string representation of the object
print ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream.to_json()

# convert the object into a dict
api_v1_audit_log_streams_id_get200_response_audit_log_stream_dict = api_v1_audit_log_streams_id_get200_response_audit_log_stream_instance.to_dict()
# create an instance of ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream from a dict
api_v1_audit_log_streams_id_get200_response_audit_log_stream_from_dict = ApiV1AuditLogStreamsIdGet200ResponseAuditLogStream.from_dict(api_v1_audit_log_streams_id_get200_response_audit_log_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


