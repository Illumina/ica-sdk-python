# Analysis


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**reference** | **str** | The unique reference of the analysis | 
**user_reference** | **str** | The user reference of the analysis | 
**pipeline** | [**Pipeline**](Pipeline.md) |  | 
**workflow_session** | [**WorkflowSession**](WorkflowSession.md) |  | [optional] 
**status** | **str** | The status of the analysis | 
**start_date** | **datetime** | When the analysis was started | [optional] 
**end_date** | **datetime** | When the analysis was finished | [optional] 
**summary** | **str** | The summary of the analysis | [optional] 
**analysis_storage** | [**AnalysisStorage**](AnalysisStorage.md) |  | [optional] 
**analysis_priority** | **str** | The priority of the analysis | [optional] 
**tags** | [**AnalysisTag**](AnalysisTag.md) |  | 

## Example

```python
from icasdk.models.analysis import Analysis

# TODO update the JSON string below
json = "{}"
# create an instance of Analysis from a JSON string
analysis_instance = Analysis.from_json(json)
# print the JSON string representation of the object
print Analysis.to_json()

# convert the object into a dict
analysis_dict = analysis_instance.to_dict()
# create an instance of Analysis from a dict
analysis_form_dict = analysis.from_dict(analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


