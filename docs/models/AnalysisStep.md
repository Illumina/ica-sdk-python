# icasdk.model.analysis_step.AnalysisStep

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**technical** | bool,  | BoolClass,  | Indicates which kind of step was executed | 
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**logs** | [**AnalysisStepLogs**](AnalysisStepLogs.md) | [**AnalysisStepLogs**](AnalysisStepLogs.md) |  | 
**status** | str,  | str,  | The status of the analysis step | must be one of ["FAILED", "DONE", "RUNNING", "INTERRUPTED", "ABORTED", "WAITING", ] 
**queueDate** | None, str, datetime,  | NoneClass, str,  | When the analysis step was queued | [optional] value must conform to RFC-3339 date-time
**startDate** | None, str, datetime,  | NoneClass, str,  | When the analysis step was started | [optional] value must conform to RFC-3339 date-time
**endDate** | None, str, datetime,  | NoneClass, str,  | When the analysis step was finished | [optional] value must conform to RFC-3339 date-time
**exitCode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The exit code of the analysis step | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

