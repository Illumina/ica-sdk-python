# icasdk.model.analysis_input.AnalysisInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The name of the input-parameter. | 
**[analysisData](#analysisData)** | list, tuple, None,  | tuple, NoneClass,  | The analysis-data used as input by the analysis. | [optional] 
**[externalData](#externalData)** | list, tuple, None,  | tuple, NoneClass,  | The external data used as input by the analysis. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# analysisData

The analysis-data used as input by the analysis.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The analysis-data used as input by the analysis. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnalysisData**](AnalysisData.md) | [**AnalysisData**](AnalysisData.md) | [**AnalysisData**](AnalysisData.md) |  | 

# externalData

The external data used as input by the analysis.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The external data used as input by the analysis. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnalysisExternalData**](AnalysisExternalData.md) | [**AnalysisExternalData**](AnalysisExternalData.md) | [**AnalysisExternalData**](AnalysisExternalData.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

