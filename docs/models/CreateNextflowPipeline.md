# icasdk.model.create_nextflow_pipeline.CreateNextflowPipeline

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**parametersXmlFile** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 
**code** | str,  | str,  | The code of the pipeline | 
**mainNextflowFile** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The main Nextflow file. | 
**description** | str,  | str,  | The description of the pipeline | 
**analysisStorageId** | str, uuid.UUID,  | str,  | The id of the storage to use for the pipeline. | value must be a uuid
**pipelineLanguageVersionId** | None, str, uuid.UUID,  | NoneClass, str,  | The id of the Nextflow version to use for the pipeline. | [optional] value must be a uuid
**nextflowConfigFile** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The Nextflow config file. | [optional] 
**[otherNextflowFiles](#otherNextflowFiles)** | list, tuple,  | tuple,  |  | [optional] 
**metadataModelFile** | None, bytes, io.FileIO, io.BufferedReader,  | NoneClass, bytes, FileIO,  | The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
**links** | [**Links**](Links.md) | [**Links**](Links.md) |  | [optional] 
**versionComment** | None, str,  | NoneClass, str,  |  | [optional] 
**[categories](#categories)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**htmlDocumentation** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# otherNextflowFiles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | Other Nextflow files referenced from the main Nextflow file. | 

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

