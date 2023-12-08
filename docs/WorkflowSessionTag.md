# WorkflowSessionTag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** | Technical tags | [optional] 
**user_tags** | **List[str]** | User tags | [optional] 

## Example

```python
from icasdk.models.workflow_session_tag import WorkflowSessionTag

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowSessionTag from a JSON string
workflow_session_tag_instance = WorkflowSessionTag.from_json(json)
# print the JSON string representation of the object
print WorkflowSessionTag.to_json()

# convert the object into a dict
workflow_session_tag_dict = workflow_session_tag_instance.to_dict()
# create an instance of WorkflowSessionTag from a dict
workflow_session_tag_form_dict = workflow_session_tag.from_dict(workflow_session_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


