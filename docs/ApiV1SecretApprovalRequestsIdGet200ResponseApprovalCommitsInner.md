# ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**secret_key** | **str** |  | 
**secret_value** | **str** |  | 
**secret_comment** | **str** |  | 
**secret_reminder_note** | **str** |  | [optional] 
**secret_reminder_repeat_days** | **float** |  | [optional] 
**skip_multiline_encoding** | **bool** |  | [optional] [default to False]
**metadata** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**op** | **str** |  | 
**tags** | [**List[ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner]**](ApiV1SecretSnapshotSecretSnapshotIdGet200ResponseSecretSnapshotSecretVersionsInnerTagsInner.md) |  | [optional] 
**secret** | [**ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret**](ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.md) |  | [optional] 
**secret_version** | [**ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecretVersion**](ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecretVersion.md) |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_commits_inner import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner from a JSON string
api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_instance = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_dict = api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner from a dict
api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_from_dict = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInner.from_dict(api_v1_secret_approval_requests_id_get200_response_approval_commits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


