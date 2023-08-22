# icasdk.model.project_base_table.ProjectBaseTable

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the table which should be used in writing queries | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**type** | str,  | str,  | The type of the table | must be one of ["TABLE", "VIEW", ] 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  | The status of the table | must be one of ["AVAILABLE", "DELETED", "PENDING", ] 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the table | [optional] 
**numberOfRecords** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of record in the table | [optional] value must be a 64 bit integer
**dataSize** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The amount of Data contained in this table in bytes | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

