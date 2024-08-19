# ApiV1GroupsPost200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**org_id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**role** | **str** |  | 
**role_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_groups_post200_response import ApiV1GroupsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1GroupsPost200Response from a JSON string
api_v1_groups_post200_response_instance = ApiV1GroupsPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1GroupsPost200Response.to_json()

# convert the object into a dict
api_v1_groups_post200_response_dict = api_v1_groups_post200_response_instance.to_dict()
# create an instance of ApiV1GroupsPost200Response from a dict
api_v1_groups_post200_response_from_dict = ApiV1GroupsPost200Response.from_dict(api_v1_groups_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


