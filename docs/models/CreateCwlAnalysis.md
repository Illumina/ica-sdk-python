# icasdk.model.create_cwl_analysis.CreateCwlAnalysis

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**userReference** | str,  | str,  | The user-reference of the analysis. This should be something meaningful for the user. | 
**analysisInput** | [**CwlAnalysisInput**](CwlAnalysisInput.md) | [**CwlAnalysisInput**](CwlAnalysisInput.md) |  | 
**pipelineId** | str,  | str,  | The pipeline for which an analysis will be created. | 
**tags** | [**AnalysisTag**](AnalysisTag.md) | [**AnalysisTag**](AnalysisTag.md) |  | 
**activationCodeDetailId** | str, uuid.UUID,  | str,  | Indicates under which activation code the pipeline is executed. | [optional] value must be a uuid
**analysisStorageId** | None, str, uuid.UUID,  | NoneClass, str,  | The id of the storage to use for the analysis. | [optional] value must be a uuid
**outputParentFolderId** | None, str,  | NoneClass, str,  | The id or the urn of the folder in which the output folder should be created. | [optional] 
**[analysisOutput](#analysisOutput)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# analysisOutput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AnalysisOutputMapping**](AnalysisOutputMapping.md) | [**AnalysisOutputMapping**](AnalysisOutputMapping.md) | [**AnalysisOutputMapping**](AnalysisOutputMapping.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

