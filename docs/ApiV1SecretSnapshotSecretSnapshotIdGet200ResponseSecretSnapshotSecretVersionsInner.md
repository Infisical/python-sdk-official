# ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **float** |  | 
**secret_key** | **str** |  | 
**secret_value** | **str** |  | 
**secret_comment** | **str** |  | 
**secret_reminder_note** | **str** |  | [optional] 
**secret_reminder_repeat_days** | **float** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] [default to False]
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**secret_id** | **str** |  | 
**tags** | [**List[ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner]**](ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner import ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner from a JSON string
api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner_instance = ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner.to_json()

# convert the object into a dict
api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner_dict = api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner_instance.to_dict()
# create an instance of ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner from a dict
api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner_from_dict = ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner.from_dict(api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_secret_versions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


