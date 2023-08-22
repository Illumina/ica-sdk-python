# icasdk.model.analysis_parameter_input.AnalysisParameterInput

Supports multi-value parameters, only one of attributes 'value' or 'multiValue' must be provided

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Supports multi-value parameters, only one of attributes &#x27;value&#x27; or &#x27;multiValue&#x27; must be provided | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**value** | None, str,  | NoneClass, str,  | The value for single-value parameters. | [optional] 
**[multiValue](#multiValue)** | list, tuple, None,  | tuple, NoneClass,  | The values for multi-value parameters. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# multiValue

The values for multi-value parameters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The values for multi-value parameters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The values for multi-value parameters. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

