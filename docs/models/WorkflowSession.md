# icasdk.model.workflow_session.WorkflowSession

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**workflow** | [**Workflow**](Workflow.md) | [**Workflow**](Workflow.md) |  | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**userReference** | str,  | str,  | The user reference of the workflow session | 
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**status** | str,  | str,  | The status of the workflow session | must be one of ["REQUESTED", "AWAITINGINPUT", "INPROGRESS", "SUCCEEDED", "FAILED", "FAILEDFINAL", "ABORTED", ] 
**tags** | [**WorkflowSessionTag**](WorkflowSessionTag.md) | [**WorkflowSessionTag**](WorkflowSessionTag.md) |  | 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**startDate** | None, str, datetime,  | NoneClass, str,  | When the workflow session was started | [optional] value must conform to RFC-3339 date-time
**endDate** | None, str, datetime,  | NoneClass, str,  | When the workflow session was finished | [optional] value must conform to RFC-3339 date-time
**summary** | None, str,  | NoneClass, str,  | The summary of the workflow session | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

