# icasdk.model.upload_rule.UploadRule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**filePattern** | str,  | str,  | The regular expression to match a file name. eg: to match all files use &#x27;.*&#x27; | 
**code** | str,  | str,  |  | 
**localFolder** | str,  | str,  | The local folder to monitor. Files in this folder on your local environment will be uploaded to the specified project. Only files matching the filePattern will be uploaded. | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**active** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**dataFormat** | [**DataFormat**](DataFormat.md) | [**DataFormat**](DataFormat.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

