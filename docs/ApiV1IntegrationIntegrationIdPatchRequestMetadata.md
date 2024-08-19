# ApiV1IntegrationIntegrationIdPatchRequestMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_prefix** | **str** | The prefix for the saved secret. Used by GCP. | [optional] 
**secret_suffix** | **str** | The suffix for the saved secret. Used by GCP. | [optional] 
**initial_sync_behavior** | **str** | Type of syncing behavoir with the integration. | [optional] 
**mapping_behavior** | **str** | The mapping behavior of the integration. | [optional] 
**should_auto_redeploy** | **bool** | Used by Render to trigger auto deploy. | [optional] 
**secret_gcp_label** | [**ApiV1IntegrationPostRequestMetadataSecretGCPLabel**](ApiV1IntegrationPostRequestMetadataSecretGCPLabel.md) |  | [optional] 
**secret_aws_tag** | [**List[ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner]**](ApiV1AuditLogStreamsIdGet200ResponseAuditLogStreamHeadersInner.md) | The tags for AWS secrets. | [optional] 
**kms_key_id** | **str** | The ID of the encryption key from AWS KMS. | [optional] 
**should_disable_delete** | **bool** | The flag to disable deletion of secrets in AWS Parameter Store. | [optional] 
**should_enable_delete** | **bool** | The flag to enable deletion of secrets | [optional] 
**should_mask_secrets** | **bool** | Specifies if the secrets synced from Infisical to Gitlab should be marked as &#39;Masked&#39;. | [optional] 
**should_protect_secrets** | **bool** | Specifies if the secrets synced from Infisical to Gitlab should be marked as &#39;Protected&#39;. | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_integration_integration_id_patch_request_metadata import ApiV1IntegrationIntegrationIdPatchRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1IntegrationIntegrationIdPatchRequestMetadata from a JSON string
api_v1_integration_integration_id_patch_request_metadata_instance = ApiV1IntegrationIntegrationIdPatchRequestMetadata.from_json(json)
# print the JSON string representation of the object
print ApiV1IntegrationIntegrationIdPatchRequestMetadata.to_json()

# convert the object into a dict
api_v1_integration_integration_id_patch_request_metadata_dict = api_v1_integration_integration_id_patch_request_metadata_instance.to_dict()
# create an instance of ApiV1IntegrationIntegrationIdPatchRequestMetadata from a dict
api_v1_integration_integration_id_patch_request_metadata_from_dict = ApiV1IntegrationIntegrationIdPatchRequestMetadata.from_dict(api_v1_integration_integration_id_patch_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


