# icasdk.model.workflow.Workflow

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**urn** | str,  | str,  | The URN of the workflow. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | 
**analysisStorage** | [**AnalysisStorage**](AnalysisStorage.md) | [**AnalysisStorage**](AnalysisStorage.md) |  | 
**code** | str,  | str,  | The code of the workflow | 
**description** | str,  | str,  | The description of the workflow | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**languageVersion** | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) | [**PipelineLanguageVersion**](PipelineLanguageVersion.md) |  | [optional] 
**workflowTags** | [**PipelineTag**](PipelineTag.md) | [**PipelineTag**](PipelineTag.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

