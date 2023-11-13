# icasdk.model.workflow_session_data.WorkflowSessionData

The workflow-session-data used as input by the workflow session.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | The workflow-session-data used as input by the workflow session. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataId** | str,  | str,  | The id of the file/folder. | 
**dataType** | str,  | str,  |  | must be one of ["FILE", "FOLDER", ] 
**format** | [**DataFormat**](DataFormat.md) | [**DataFormat**](DataFormat.md) |  | 
**name** | str,  | str,  | The name of the file/folder as it was processed by the workflow session. | 
**mountPath** | str,  | str,  | The requested location where the input file was located on the machine that was running the workflow. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

