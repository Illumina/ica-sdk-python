# icasdk.model.pipeline_bundle.PipelineBundle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[regions](#regions)** | list, tuple,  | tuple,  |  | 
**[analysisStorages](#analysisStorages)** | list, tuple,  | tuple,  |  | 
**[retiredPipelines](#retiredPipelines)** | list, tuple,  | tuple,  |  | 
**[activePipelines](#activePipelines)** | list, tuple,  | tuple,  |  | 
**name** | str,  | str,  |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**[canceledPipelines](#canceledPipelines)** | list, tuple,  | tuple,  |  | 
**maxNumberOfAllowedSlots** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# activePipelines

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) |  | 

# canceledPipelines

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) |  | 

# retiredPipelines

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) | [**Pipeline**](Pipeline.md) |  | 

# regions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Region**](Region.md) | [**Region**](Region.md) | [**Region**](Region.md) |  | 

# analysisStorages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnalysisStorage**](AnalysisStorage.md) | [**AnalysisStorage**](AnalysisStorage.md) | [**AnalysisStorage**](AnalysisStorage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

