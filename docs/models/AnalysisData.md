# icasdk.model.analysis_data.AnalysisData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataId** | str,  | str,  | The id of the file/folder. | 
**dataType** | str,  | str,  |  | must be one of ["FILE", "FOLDER", ] 
**format** | [**DataFormat**](DataFormat.md) | [**DataFormat**](DataFormat.md) |  | 
**name** | str,  | str,  | The name of the file/folder as it was processed by the analysis. | 
**[children](#children)** | list, tuple,  | tuple,  |  | [optional] 
**mountPath** | str,  | str,  | The requested location where the input file was located on the machine that was running the pipeline. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# children

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnalysisData**](AnalysisData.md) | [**AnalysisData**](AnalysisData.md) | [**AnalysisData**](AnalysisData.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

