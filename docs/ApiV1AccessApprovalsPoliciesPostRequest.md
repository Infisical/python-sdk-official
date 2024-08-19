# ApiV1AccessApprovalsPoliciesPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_slug** | **str** |  | 
**name** | **str** |  | [optional] 
**secret_path** | **str** |  | [optional] [default to '/']
**environment** | **str** |  | 
**approvers** | **List[str]** |  | 
**approvals** | **float** |  | [optional] [default to 1]
**enforcement_level** | **str** |  | [optional] [default to 'hard']

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_policies_post_request import ApiV1AccessApprovalsPoliciesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsPoliciesPostRequest from a JSON string
api_v1_access_approvals_policies_post_request_instance = ApiV1AccessApprovalsPoliciesPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsPoliciesPostRequest.to_json()

# convert the object into a dict
api_v1_access_approvals_policies_post_request_dict = api_v1_access_approvals_policies_post_request_instance.to_dict()
# create an instance of ApiV1AccessApprovalsPoliciesPostRequest from a dict
api_v1_access_approvals_policies_post_request_from_dict = ApiV1AccessApprovalsPoliciesPostRequest.from_dict(api_v1_access_approvals_policies_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


