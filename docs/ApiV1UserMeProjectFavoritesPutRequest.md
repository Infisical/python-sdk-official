# ApiV1UserMeProjectFavoritesPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**project_favorites** | **List[str]** |  | 

## Example

```python
from infisicalapi_client.models.api_v1_user_me_project_favorites_put_request import ApiV1UserMeProjectFavoritesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1UserMeProjectFavoritesPutRequest from a JSON string
api_v1_user_me_project_favorites_put_request_instance = ApiV1UserMeProjectFavoritesPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1UserMeProjectFavoritesPutRequest.to_json()

# convert the object into a dict
api_v1_user_me_project_favorites_put_request_dict = api_v1_user_me_project_favorites_put_request_instance.to_dict()
# create an instance of ApiV1UserMeProjectFavoritesPutRequest from a dict
api_v1_user_me_project_favorites_put_request_from_dict = ApiV1UserMeProjectFavoritesPutRequest.from_dict(api_v1_user_me_project_favorites_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


