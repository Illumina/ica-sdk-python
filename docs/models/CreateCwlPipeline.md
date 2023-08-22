# icasdk.model.create_cwl_pipeline.CreateCwlPipeline

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**parametersXmlFile** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 
**code** | str,  | str,  | The code of the CWL pipeline | 
**description** | str,  | str,  | The description of the CWL pipeline | 
**analysisStorageId** | str, uuid.UUID,  | str,  | The id of the storage to use for the pipeline. | value must be a uuid
**workflowCwlFile** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The CWL workflow file. | 
**[toolCwlFiles](#toolCwlFiles)** | list, tuple,  | tuple,  |  | [optional] 
**metadataModelFile** | None, bytes, io.FileIO, io.BufferedReader,  | NoneClass, bytes, FileIO,  | The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
**links** | [**Links**](Links.md) | [**Links**](Links.md) |  | [optional] 
**versionComment** | None, str,  | NoneClass, str,  |  | [optional] 
**[categories](#categories)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**htmlDocumentation** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# toolCwlFiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The CWL tool files referenced from the workflow file. | 

# categories

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

