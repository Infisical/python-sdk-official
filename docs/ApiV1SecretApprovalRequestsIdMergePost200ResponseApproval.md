# ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**policy_id** | **str** |  | 
**has_merged** | **bool** |  | [optional] [default to False]
**status** | **str** |  | [optional] [default to 'open']
**conflicts** | **object** |  | [optional] 
**slug** | **str** |  | 
**folder_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**is_replicated** | **bool** |  | [optional] 
**committer_user_id** | **str** |  | 
**status_changed_by_user_id** | **str** |  | [optional] 
**bypass_reason** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_id_merge_post200_response_approval import ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval from a JSON string
api_v1_secret_approval_requests_id_merge_post200_response_approval_instance = ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_id_merge_post200_response_approval_dict = api_v1_secret_approval_requests_id_merge_post200_response_approval_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval from a dict
api_v1_secret_approval_requests_id_merge_post200_response_approval_from_dict = ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval.from_dict(api_v1_secret_approval_requests_id_merge_post200_response_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


