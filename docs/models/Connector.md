# icasdk.model.connector.Connector

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | 
**os** | str,  | str,  | The target OS of the original connector installer. | must be one of ["WINDOWS", "LINUX", "OSX", ] 
**installationStatus** | str,  | str,  |  | must be one of ["PENDING_INSTALLATION", "INSTALLED", "ERROR", "UNKNOWN", "CANCELLED", ] 
**active** | bool,  | BoolClass,  |  | 
**technicalCode** | str,  | str,  | Technical code to be used for processing. | 
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**connected** | bool,  | BoolClass,  | Indicates if the connector is connected or not. This is cached so even when the connector is no longer connected, for a short time this still may return true. | 
**mode** | str,  | str,  | The mode the connector runs in. | must be one of ["DOWNLOAD", "UPLOAD", "BOTH", "NONE", ] 
**newConnectorVersionAvailable** | bool,  | BoolClass,  |  | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**initializationKey** | None, str,  | NoneClass, str,  | The key provided via other channels to initialize the installation. | [optional] 
**description** | None, str,  | NoneClass, str,  | The general description of the connector instance including its purpose. | [optional] 
**maxBandwidth** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The maximum bandwidth defined in MB per second. | [optional] 
**maxConcurrentTransfers** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum amount of concurrent transfers that this connector can execute. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

