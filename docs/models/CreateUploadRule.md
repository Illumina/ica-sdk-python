# icasdk.model.create_upload_rule.CreateUploadRule

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
**projectId** | str,  | str,  | The project to which the data will be uploaded. | 
**active** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**dataFormatId** | None, str, uuid.UUID,  | NoneClass, str,  | The format which will be assigned to the uploaded data. If not specified, an auto-detection of the format will be done. | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

