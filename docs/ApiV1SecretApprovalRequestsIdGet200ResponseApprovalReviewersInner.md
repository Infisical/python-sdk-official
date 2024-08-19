# ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**username** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner import ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner from a JSON string
api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner_instance = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner_dict = api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner from a dict
api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner_from_dict = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalReviewersInner.from_dict(api_v1_secret_approval_requests_id_get200_response_approval_reviewers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


