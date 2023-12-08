# ProjectSamplePagedList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProjectSample]**](ProjectSample.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from icasdk.models.project_sample_paged_list import ProjectSamplePagedList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSamplePagedList from a JSON string
project_sample_paged_list_instance = ProjectSamplePagedList.from_json(json)
# print the JSON string representation of the object
print ProjectSamplePagedList.to_json()

# convert the object into a dict
project_sample_paged_list_dict = project_sample_paged_list_instance.to_dict()
# create an instance of ProjectSamplePagedList from a dict
project_sample_paged_list_form_dict = project_sample_paged_list.from_dict(project_sample_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

