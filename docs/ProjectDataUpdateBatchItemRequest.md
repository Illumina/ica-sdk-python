# ProjectDataUpdateBatchItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_id** | **str** | Data to apply the update to (recursively, if it&#39;s a folder). | 
**user_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**technical_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 

## Example

```python
from icasdk.models.project_data_update_batch_item_request import ProjectDataUpdateBatchItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataUpdateBatchItemRequest from a JSON string
project_data_update_batch_item_request_instance = ProjectDataUpdateBatchItemRequest.from_json(json)
# print the JSON string representation of the object
print ProjectDataUpdateBatchItemRequest.to_json()

# convert the object into a dict
project_data_update_batch_item_request_dict = project_data_update_batch_item_request_instance.to_dict()
# create an instance of ProjectDataUpdateBatchItemRequest from a dict
project_data_update_batch_item_request_form_dict = project_data_update_batch_item_request.from_dict(project_data_update_batch_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


