# AnalysisCreationBatchItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**request** | [**AnalysisCreationBatchItemRequest**](AnalysisCreationBatchItemRequest.md) |  | 
**processing** | [**AnalysisCreationBatchItemProcessing**](AnalysisCreationBatchItemProcessing.md) |  | 
**created_analysis** | [**Analysis**](Analysis.md) |  | [optional] 

## Example

```python
from icasdk.models.analysis_creation_batch_item import AnalysisCreationBatchItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItem from a JSON string
analysis_creation_batch_item_instance = AnalysisCreationBatchItem.from_json(json)
# print the JSON string representation of the object
print AnalysisCreationBatchItem.to_json()

# convert the object into a dict
analysis_creation_batch_item_dict = analysis_creation_batch_item_instance.to_dict()
# create an instance of AnalysisCreationBatchItem from a dict
analysis_creation_batch_item_form_dict = analysis_creation_batch_item.from_dict(analysis_creation_batch_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


