# ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**request_id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**reviewer_user_id** | **str** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approval_requests_id_review_post200_response_review import ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview from a JSON string
api_v1_secret_approval_requests_id_review_post200_response_review_instance = ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview.to_json()

# convert the object into a dict
api_v1_secret_approval_requests_id_review_post200_response_review_dict = api_v1_secret_approval_requests_id_review_post200_response_review_instance.to_dict()
# create an instance of ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview from a dict
api_v1_secret_approval_requests_id_review_post200_response_review_from_dict = ApiV1SecretApprovalRequestsIdReviewPost200ResponseReview.from_dict(api_v1_secret_approval_requests_id_review_post200_response_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


