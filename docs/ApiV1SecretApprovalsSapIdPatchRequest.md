# ApiV1SecretApprovalsSapIdPatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**approvers** | **List[str]** |  | 
**approvals** | **float** |  | [optional] [default to 1]
**secret_path** | **str** |  | [optional] 
**enforcement_level** | **str** |  | [optional] 

## Example

```python
from infisicalapi_client.models.api_v1_secret_approvals_sap_id_patch_request import ApiV1SecretApprovalsSapIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SecretApprovalsSapIdPatchRequest from a JSON string
api_v1_secret_approvals_sap_id_patch_request_instance = ApiV1SecretApprovalsSapIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1SecretApprovalsSapIdPatchRequest.to_json()

# convert the object into a dict
api_v1_secret_approvals_sap_id_patch_request_dict = api_v1_secret_approvals_sap_id_patch_request_instance.to_dict()
# create an instance of ApiV1SecretApprovalsSapIdPatchRequest from a dict
api_v1_secret_approvals_sap_id_patch_request_from_dict = ApiV1SecretApprovalsSapIdPatchRequest.from_dict(api_v1_secret_approvals_sap_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


