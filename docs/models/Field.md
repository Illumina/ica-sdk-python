# icasdk.model.field.Field

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**fieldType** | str,  | str,  |  | [optional] must be one of ["TEXT", "NUMERIC", "BOOLEAN", "DATE", "ENUMERATION", "FIELDGROUP", "PIPELINE_REFERENCE", ] 
**required** | bool,  | BoolClass,  |  | [optional] 
**multivalued** | bool,  | BoolClass,  |  | [optional] 
**filledByPipeline** | bool,  | BoolClass,  |  | [optional] 
**[fields](#fields)** | list, tuple,  | tuple,  |  | [optional] 
**[enumerationValues](#enumerationValues)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Field**](Field.md) | [**Field**](Field.md) | [**Field**](Field.md) |  | 

# enumerationValues

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

