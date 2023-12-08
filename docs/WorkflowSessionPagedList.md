# WorkflowSessionPagedList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WorkflowSession]**](WorkflowSession.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from icasdk.models.workflow_session_paged_list import WorkflowSessionPagedList

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionPagedList from a JSON string
workflow_session_paged_list_instance = WorkflowSessionPagedList.from_json(json)
# print the JSON string representation of the object
print WorkflowSessionPagedList.to_json()

# convert the object into a dict
workflow_session_paged_list_dict = workflow_session_paged_list_instance.to_dict()
# create an instance of WorkflowSessionPagedList from a dict
workflow_session_paged_list_form_dict = workflow_session_paged_list.from_dict(workflow_session_paged_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


