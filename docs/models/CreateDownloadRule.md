# icasdk.model.create_download_rule.CreateDownloadRule

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
**active** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**formatCode** | None, str,  | NoneClass, str,  | Regular expression to filter which format this rule applies to. | [optional] 
**projectName** | None, str,  | NoneClass, str,  | Regular expression to filter which project this rule applies to. | [optional] 
**fileNameExpression** | None, str,  | NoneClass, str,  | Will allow the filename to be modified including a set of variables | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

