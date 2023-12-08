# ProjectDataCopyBatchItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**ProjectDataCopyBatchItemRequest**](ProjectDataCopyBatchItemRequest.md) |  | 
**processing** | [**ProjectDataCopyBatchItemProcessing**](ProjectDataCopyBatchItemProcessing.md) |  | 
**created_project_data** | [**ProjectData**](ProjectData.md) |  | [optional] 

## Example

```python
from icasdk.models.project_data_copy_batch_item import ProjectDataCopyBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataCopyBatchItem from a JSON string
project_data_copy_batch_item_instance = ProjectDataCopyBatchItem.from_json(json)
# print the JSON string representation of the object
print ProjectDataCopyBatchItem.to_json()

# convert the object into a dict
project_data_copy_batch_item_dict = project_data_copy_batch_item_instance.to_dict()
# create an instance of ProjectDataCopyBatchItem from a dict
project_data_copy_batch_item_form_dict = project_data_copy_batch_item.from_dict(project_data_copy_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


