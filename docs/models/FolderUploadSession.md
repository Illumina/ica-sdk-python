# icasdk.model.folder_upload_session.FolderUploadSession

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timeSessionExpires** | str, datetime,  | str,  | The time the folder upload session will expire as it is only temporarily valid. | value must conform to RFC-3339 date-time
**timeCreated** | str, datetime,  | str,  | The time the folder upload session was created. | value must conform to RFC-3339 date-time
**id** | str,  | str,  | The id of the folder upload session. | 
**status** | str,  | str,  | The status of the folder upload session. | must be one of ["OPEN", "CLOSED", "COMPLETED", ] 
**timeCompleted** | None, str, datetime,  | NoneClass, str,  | The time the folder upload session completed. | [optional] value must conform to RFC-3339 date-time
**timeClosed** | None, str, datetime,  | NoneClass, str,  | The time the folder upload session was closed. | [optional] value must conform to RFC-3339 date-time
**tempCredentials** | [**TempCredentials**](TempCredentials.md) | [**TempCredentials**](TempCredentials.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

