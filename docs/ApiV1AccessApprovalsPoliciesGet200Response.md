# ApiV1AccessApprovalsPoliciesGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals** | [**List[ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner]**](ApiV1AccessApprovalsPoliciesGet200ResponseApprovalsInner.md) |  | 

## Example

```python
from infisicalapi_client.models.api_v1_access_approvals_policies_get200_response import ApiV1AccessApprovalsPoliciesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AccessApprovalsPoliciesGet200Response from a JSON string
api_v1_access_approvals_policies_get200_response_instance = ApiV1AccessApprovalsPoliciesGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1AccessApprovalsPoliciesGet200Response.to_json()

# convert the object into a dict
api_v1_access_approvals_policies_get200_response_dict = api_v1_access_approvals_policies_get200_response_instance.to_dict()
# create an instance of ApiV1AccessApprovalsPoliciesGet200Response from a dict
api_v1_access_approvals_policies_get200_response_from_dict = ApiV1AccessApprovalsPoliciesGet200Response.from_dict(api_v1_access_approvals_policies_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


