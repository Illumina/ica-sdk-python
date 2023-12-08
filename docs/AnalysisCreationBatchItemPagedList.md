# AnalysisCreationBatchItemPagedList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AnalysisCreationBatchItem]**](AnalysisCreationBatchItem.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from icasdk.models.analysis_creation_batch_item_paged_list import AnalysisCreationBatchItemPagedList

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatchItemPagedList from a JSON string
analysis_creation_batch_item_paged_list_instance = AnalysisCreationBatchItemPagedList.from_json(json)
# print the JSON string representation of the object
print AnalysisCreationBatchItemPagedList.to_json()

# convert the object into a dict
analysis_creation_batch_item_paged_list_dict = analysis_creation_batch_item_paged_list_instance.to_dict()
# create an instance of AnalysisCreationBatchItemPagedList from a dict
analysis_creation_batch_item_paged_list_form_dict = analysis_creation_batch_item_paged_list.from_dict(analysis_creation_batch_item_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


