# icasdk.model.create_data.CreateData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataType** | str,  | str,  |  | must be one of ["FILE", "FOLDER", ] 
**name** | str,  | str,  | The name of the file/folder as how it will be created. | 
**folderId** | None, str,  | NoneClass, str,  | The id of the folder you want to create this new data in. Alternatively, the folderPath attribute could be used as well for this. | [optional] 
**folderPath** | None, str,  | NoneClass, str,  | The absolute path of the folder you want to create this new data in which must end with &#x27;/&#x27;. Alternatively, the folderId attribute could be used as well for this. In case the folder path does not yet exist, it will be automatically created. | [optional] 
**formatCode** | None, str,  | NoneClass, str,  | The code of the format you would like to assign at creation time. This is only allowed for file data. If not specified, auto format assignment will be done. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

