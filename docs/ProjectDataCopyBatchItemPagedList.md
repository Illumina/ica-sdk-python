# ProjectDataCopyBatchItemPagedList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectDataCopyBatchItem]**](ProjectDataCopyBatchItem.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from icasdk.models.project_data_copy_batch_item_paged_list import ProjectDataCopyBatchItemPagedList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataCopyBatchItemPagedList from a JSON string
project_data_copy_batch_item_paged_list_instance = ProjectDataCopyBatchItemPagedList.from_json(json)
# print the JSON string representation of the object
print ProjectDataCopyBatchItemPagedList.to_json()

# convert the object into a dict
project_data_copy_batch_item_paged_list_dict = project_data_copy_batch_item_paged_list_instance.to_dict()
# create an instance of ProjectDataCopyBatchItemPagedList from a dict
project_data_copy_batch_item_paged_list_form_dict = project_data_copy_batch_item_paged_list.from_dict(project_data_copy_batch_item_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

