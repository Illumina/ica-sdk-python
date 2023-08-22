# icasdk.model.download_rule.DownloadRule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**targetLocalFolder** | str,  | str,  | The local folder where to write the data. | 
**sequence** | decimal.Decimal, int,  | decimal.Decimal,  | Defines the order of the rule. | value must be a 32 bit integer
**code** | str,  | str,  |  | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**active** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**formatCode** | None, str,  | NoneClass, str,  | Regular expression to select which format this rule applies to. | [optional] 
**projectName** | None, str,  | NoneClass, str,  | Regular expression to select which project this rule applies to. | [optional] 
**fileNameExpression** | None, str,  | NoneClass, str,  | Will allow the filename to be modified including a set of variables | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

