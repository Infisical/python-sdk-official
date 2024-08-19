# ApiV1AuditLogStreamsGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_log_streams** | [**List[ApiV1AuditLogStreamsGet200ResponseAuditLogStreamsInner]**](ApiV1AuditLogStreamsGet200ResponseAuditLogStreamsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_audit_log_streams_get200_response import ApiV1AuditLogStreamsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuditLogStreamsGet200Response from a JSON string
api_v1_audit_log_streams_get200_response_instance = ApiV1AuditLogStreamsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1AuditLogStreamsGet200Response.to_json()

# convert the object into a dict
api_v1_audit_log_streams_get200_response_dict = api_v1_audit_log_streams_get200_response_instance.to_dict()
# create an instance of ApiV1AuditLogStreamsGet200Response from a dict
api_v1_audit_log_streams_get200_response_from_dict = ApiV1AuditLogStreamsGet200Response.from_dict(api_v1_audit_log_streams_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


