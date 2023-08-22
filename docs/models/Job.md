# icasdk.model.job.Job

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**owner** | [**User**](User.md) | [**User**](User.md) |  | 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**subjectType** | str,  | str,  | The type of the subject for which this job provides execution. | 
**subjectId** | str, uuid.UUID,  | str,  | The id of the subject for which this job provides execution. | value must be a uuid
**status** | str,  | str,  |  | must be one of ["INITIALIZED", "WAITING_FOR_RESOURCES", "RUNNING", "STOPPED", "SUCCEEDED", "PARTIALLY_SUCCEEDED", "FAILED", ] 
**additionalStatusInformation** | None, str,  | NoneClass, str,  | Additional information regarding the status of this job. | [optional] 
**timeStarted** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**timeFinished** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

