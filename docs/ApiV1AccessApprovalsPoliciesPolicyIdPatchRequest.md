# ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**secret_path** | **str** |  | [optional] 
**approvers** | **List[str]** |  | 
**approvals** | **float** |  | [optional] [default to 1]
**enforcement_level** | **str** |  | [optional] [default to 'hard']

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_policies_policy_id_patch_request import ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest from a JSON string
api_v1_access_approvals_policies_policy_id_patch_request_instance = ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest.to_json()

# convert the object into a dict
api_v1_access_approvals_policies_policy_id_patch_request_dict = api_v1_access_approvals_policies_policy_id_patch_request_instance.to_dict()
# create an instance of ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest from a dict
api_v1_access_approvals_policies_policy_id_patch_request_from_dict = ApiV1AccessApprovalsPoliciesPolicyIdPatchRequest.from_dict(api_v1_access_approvals_policies_policy_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


