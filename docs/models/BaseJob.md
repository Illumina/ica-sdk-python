# icasdk.model.base_job.BaseJob

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**type** | str,  | str,  | The type of the job | must be one of ["COPYTABLE", "EXPORTTABLE", "CREATETABLE", "EXECUTEQUERY", "LOADDATA", "PREPAREDATA", ] 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  | The status of the job | must be one of ["CREATED", "SUCCEEDED", "FAILED", "PENDING", "INPROGRESS", "ABORTED", ] 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  | A short description of the base job | [optional] 
**table** | [**ProjectBaseTable**](ProjectBaseTable.md) | [**ProjectBaseTable**](ProjectBaseTable.md) |  | [optional] 
**overallDuration** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The duration of the job expressed in milliseconds | [optional] value must be a 64 bit integer
**details** | None, str,  | NoneClass, str,  | Detailed description of the job | [optional] 
**bytesBilled** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Bytes billed | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

