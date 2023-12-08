# ProjectDataCopyBatchItemProcessing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**additional_status_information** | **str** | Additional information regarding the status of this batch item. | [optional] 

## Example

```python
from icasdk.models.project_data_copy_batch_item_processing import ProjectDataCopyBatchItemProcessing

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataCopyBatchItemProcessing from a JSON string
project_data_copy_batch_item_processing_instance = ProjectDataCopyBatchItemProcessing.from_json(json)
# print the JSON string representation of the object
print ProjectDataCopyBatchItemProcessing.to_json()

# convert the object into a dict
project_data_copy_batch_item_processing_dict = project_data_copy_batch_item_processing_instance.to_dict()
# create an instance of ProjectDataCopyBatchItemProcessing from a dict
project_data_copy_batch_item_processing_form_dict = project_data_copy_batch_item_processing.from_dict(project_data_copy_batch_item_processing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


