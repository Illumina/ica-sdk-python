# icasdk.model.analysis_step_logs.AnalysisStepLogs

Contains references to the standard output (stdout) and standard error (stderr) log streams of an analysis step. In this object both log streams could be provided in 2 different formats: as a WebSocket stream URL or as an ICA Data reference. The status of the analysis step determines which format is provided: a WebSocket URL during step execution, a Data reference after step execution. Note however that an analysis step might not expose log streams at all, which would result in this object being empty. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains references to the standard output (stdout) and standard error (stderr) log streams of an analysis step. In this object both log streams could be provided in 2 different formats: as a WebSocket stream URL or as an ICA Data reference. The status of the analysis step determines which format is provided: a WebSocket URL during step execution, a Data reference after step execution. Note however that an analysis step might not expose log streams at all, which would result in this object being empty.  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**stdOutData** | [**Data**](Data.md) | [**Data**](Data.md) |  | [optional] 
**stdOutStream** | None, str,  | NoneClass, str,  | A WebSocket URL for reading the standard output log stream. Might be closed by ICA as soon as the analysis step execution has finished. | [optional] 
**stdErrData** | [**Data**](Data.md) | [**Data**](Data.md) |  | [optional] 
**stdErrStream** | None, str,  | NoneClass, str,  | A WebSocket URL for reading the standard error log stream. Might be closed by ICA as soon as the analysis step execution has finished. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

