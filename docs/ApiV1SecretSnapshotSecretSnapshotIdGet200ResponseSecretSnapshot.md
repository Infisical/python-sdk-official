# ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**environment** | [**ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotEnvironment**](ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotEnvironment.md) |  | 
**secret_versions** | [**List[ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner]**](ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInner.md) |  | 
**folder_version** | [**List[ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotFolderVersionInner]**](ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotFolderVersionInner.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot import ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot from a JSON string
api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_instance = ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot.to_json()

# convert the object into a dict
api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_dict = api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_instance.to_dict()
# create an instance of ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot from a dict
api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_from_dict = ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshot.from_dict(api_v1_secret_snapshot_secret_snapshot_id_get200_response_secret_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


