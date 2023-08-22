# icasdk.model.create_connector.CreateConnector

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mode** | str,  | str,  | The mode the connector runs in. | must be one of ["DOWNLOAD", "UPLOAD", "BOTH", "NONE", ] 
**code** | str,  | str,  |  | 
**os** | str,  | str,  | The target OS of the original connector installer. | must be one of ["WINDOWS", "LINUX", "OSX", ] 
**active** | bool,  | BoolClass,  |  | 
**description** | None, str,  | NoneClass, str,  | The general description of the connector instance including its purpose. | [optional] 
**maxBandwidth** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | The maximum bandwidth defined in MB per second. | [optional] 
**maxConcurrentTransfers** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum amount of concurrent transfers that this connector can execute. | [optional] if omitted the server will use the default value of 2value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

