# icasdk.model.workflow_session_input.WorkflowSessionInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The name of the input-parameter. | 
**[analysisData](#analysisData)** | list, tuple, None,  | tuple, NoneClass,  | The workflow-session-data used as input by the workflow session. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# analysisData

The workflow-session-data used as input by the workflow session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The workflow-session-data used as input by the workflow session. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkflowSessionData**](WorkflowSessionData.md) | [**WorkflowSessionData**](WorkflowSessionData.md) | [**WorkflowSessionData**](WorkflowSessionData.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

