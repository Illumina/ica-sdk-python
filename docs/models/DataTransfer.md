# icasdk.model.data_transfer.DataTransfer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reference** | str,  | str,  |  | 
**data** | [**Data**](Data.md) | [**Data**](Data.md) |  | 
**dataTransferred** | decimal.Decimal, int,  | decimal.Decimal,  | The data transferred so far in bytes. | value must be a 64 bit integer
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**direction** | str,  | str,  |  | must be one of ["UPLOAD", "DOWNLOAD", "IMPORT", ] 
**status** | str,  | str,  |  | must be one of ["REQUESTED", "ONGOING", "SUCCEEDED", "FAILED", "ABORTED", "ABORTREQUESTED", "SCHEDULED", ] 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**connector** | [**Connector**](Connector.md) | [**Connector**](Connector.md) |  | [optional] 
**protocol** | None, str,  | NoneClass, str,  |  | [optional] must be one of ["HTTPS", ] 
**statusMessage** | None, str,  | NoneClass, str,  | A message explaining the reason why the transfer is in the current status. | [optional] 
**duration** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The overall duration of of the transfer defined in seconds. | [optional] value must be a 64 bit integer
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

