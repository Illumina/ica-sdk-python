# icasdk.model.analysis.Analysis

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pipeline** | [**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) |  | 
**reference** | str,  | str,  | The unique reference of the analysis | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**userReference** | str,  | str,  | The user reference of the analysis | 
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  | The status of the analysis | must be one of ["REQUESTED", "AWAITINGINPUT", "INPROGRESS", "SUCCEEDED", "FAILED", "FAILEDFINAL", "ABORTED", ] 
**tags** | [**AnalysisTag**](AnalysisTag.md) | [**AnalysisTag**](AnalysisTag.md) |  | 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**workflowSession** | [**WorkflowSession**](WorkflowSession.md) | [**WorkflowSession**](WorkflowSession.md) |  | [optional] 
**startDate** | None, str, datetime,  | NoneClass, str,  | When the analysis was started | [optional] value must conform to RFC-3339 date-time
**endDate** | None, str, datetime,  | NoneClass, str,  | When the analysis was finished | [optional] value must conform to RFC-3339 date-time
**summary** | None, str,  | NoneClass, str,  | The summary of the analysis | [optional] 
**analysisStorage** | [**AnalysisStorage**](AnalysisStorage.md) | [**AnalysisStorage**](AnalysisStorage.md) |  | [optional] 
**analysisPriority** | None, str,  | NoneClass, str,  | The priority of the analysis | [optional] must be one of ["LOW", "MEDIUM", "HIGH", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

