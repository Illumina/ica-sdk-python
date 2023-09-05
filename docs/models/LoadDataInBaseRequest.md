# icasdk.model.load_data_in_base_request.LoadDataInBaseRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataId** | str,  | str,  | ID of the data to load into the table | 
**allowQuotedNewlines** | None, bool,  | NoneClass, BoolClass,  | Enable to include newlines contained in quoted data sections in the cellâ€™s value. When disabled, newlines will signal a new row | [optional] if omitted the server will use the default value of False
**delimiter** | None, str,  | NoneClass, str,  | field delimiter | [optional] if omitted the server will use the default value of ","
**encoding** | None, str,  | NoneClass, str,  | Encoding | [optional] must be one of ["UTF8", "ISO88591", ] if omitted the server will use the default value of "UTF8"
**forceLoad** | None, bool,  | NoneClass, BoolClass,  | When false (default): the data will not be loaded if it was already previously loaded to table ; when true, the data will be loaded even if already loaded in the past | [optional] if omitted the server will use the default value of False
**headerRowsToSkip** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | number of rows to skip (usually for headers) | [optional] if omitted the server will use the default value of 1value must be a 32 bit integer
**ignoreUnknownValues** | bool,  | BoolClass,  | When enabled, rows with extra column values that do not match the schema will be ignored and will not be loaded into the table, rows with too few values will receive default value null | [optional] if omitted the server will use the default value of False
**includeReferences** | None, bool,  | NoneClass, BoolClass,  | Include references | [optional] if omitted the server will use the default value of True
**includeDataReference** | None, bool,  | NoneClass, BoolClass,  | Include Data Reference | [optional] if omitted the server will use the default value of True
**includeSampleReference** | None, bool,  | NoneClass, BoolClass,  | Include Sample Reference | [optional] if omitted the server will use the default value of True
**includePipelineReference** | None, bool,  | NoneClass, BoolClass,  | Include Pipeline Reference | [optional] if omitted the server will use the default value of True
**includePipelineExecutionReference** | None, bool,  | NoneClass, BoolClass,  | Include Pipeline Execution Reference | [optional] if omitted the server will use the default value of True
**includeTenantReference** | None, bool,  | NoneClass, BoolClass,  | Include Tenant Reference | [optional] if omitted the server will use the default value of True
**nullMarker** | None, str,  | NoneClass, str,  | Specifies a string that represents a null value in a CSV/TSV file. | [optional] 
**numberOfErrorsAllowed** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The maximum number of bad records that Base can ignore when running the job | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**quote** | None, str,  | NoneClass, str,  | The value that is used to quote data sections in a CSV/TSV file | [optional] 
**writePreference** | None, str,  | NoneClass, str,  | specifies how to write data in the table. | [optional] must be one of ["WRITEIFEMPTY", "APPENDTOTABLE", "OVERWRITETABLE", ] if omitted the server will use the default value of "APPENDTOTABLE"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

