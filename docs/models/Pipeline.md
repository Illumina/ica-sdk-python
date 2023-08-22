# icasdk.model.pipeline.Pipeline

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**analysisStorage** | [**AnalysisStorage**](AnalysisStorage.md) | [**AnalysisStorage**](AnalysisStorage.md) |  | 
**code** | str,  | str,  | The code of the pipeline | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**description** | str,  | str,  | The description of the pipeline | 
**language** | str,  | str,  | The language that is used by the pipeline | must be one of ["CWL", "NEXTFLOW", "UNKNOWN", ] 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**pipelineTags** | [**PipelineTag**](PipelineTag.md) | [**PipelineTag**](PipelineTag.md) |  | 
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**urn** | None, str,  | NoneClass, str,  | The URN of the pipeline. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**languageVersion** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

