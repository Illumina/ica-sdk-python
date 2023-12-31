# icasdk.model.pipeline_configuration_parameter.PipelineConfigurationParameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | The code of the parameter | 
**multiValue** | bool,  | BoolClass,  | Indicates whether multiple values are allowed for this parameter | 
**type** | str,  | str,  | The type for each parameter | 
**required** | bool,  | BoolClass,  | Indicates whether this parameter is required | 
**settings** | [**Settings**](Settings.md) | [**Settings**](Settings.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

