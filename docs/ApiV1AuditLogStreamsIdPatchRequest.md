# ApiV1AuditLogStreamsIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The HTTP URL to push logs to. | [optional] 
**headers** | [**List[ApiV1AuditLogStreamsPostRequestHeadersInner]**](ApiV1AuditLogStreamsPostRequestHeadersInner.md) | The HTTP headers attached for the external prrovider requests. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_audit_log_streams_id_patch_request import ApiV1AuditLogStreamsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AuditLogStreamsIdPatchRequest from a JSON string
api_v1_audit_log_streams_id_patch_request_instance = ApiV1AuditLogStreamsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AuditLogStreamsIdPatchRequest.to_json()

# convert the object into a dict
api_v1_audit_log_streams_id_patch_request_dict = api_v1_audit_log_streams_id_patch_request_instance.to_dict()
# create an instance of ApiV1AuditLogStreamsIdPatchRequest from a dict
api_v1_audit_log_streams_id_patch_request_from_dict = ApiV1AuditLogStreamsIdPatchRequest.from_dict(api_v1_audit_log_streams_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


