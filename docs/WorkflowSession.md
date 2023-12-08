# WorkflowSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**user_reference** | **str** | The user reference of the workflow session | 
**workflow** | [**Workflow**](Workflow.md) |  | 
**status** | **str** | The status of the workflow session | 
**start_date** | **datetime** | When the workflow session was started | [optional] 
**end_date** | **datetime** | When the workflow session was finished | [optional] 
**summary** | **str** | The summary of the workflow session | [optional] 
**tags** | [**WorkflowSessionTag**](WorkflowSessionTag.md) |  | 

## Example

```python
from icasdk.models.workflow_session import WorkflowSession

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSession from a JSON string
workflow_session_instance = WorkflowSession.from_json(json)
# print the JSON string representation of the object
print WorkflowSession.to_json()

# convert the object into a dict
workflow_session_dict = workflow_session_instance.to_dict()
# create an instance of WorkflowSession from a dict
workflow_session_form_dict = workflow_session.from_dict(workflow_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


