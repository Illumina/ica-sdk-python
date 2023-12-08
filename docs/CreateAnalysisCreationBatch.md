# CreateAnalysisCreationBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwl_items** | [**List[CreateCwlAnalysis]**](CreateCwlAnalysis.md) |  | [optional] 
**nextflow_items** | [**List[CreateNextflowAnalysis]**](CreateNextflowAnalysis.md) |  | [optional] 

## Example

```python
from icasdk.models.create_analysis_creation_batch import CreateAnalysisCreationBatch

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnalysisCreationBatch from a JSON string
create_analysis_creation_batch_instance = CreateAnalysisCreationBatch.from_json(json)
# print the JSON string representation of the object
print CreateAnalysisCreationBatch.to_json()

# convert the object into a dict
create_analysis_creation_batch_dict = create_analysis_creation_batch_instance.to_dict()
# create an instance of CreateAnalysisCreationBatch from a dict
create_analysis_creation_batch_form_dict = create_analysis_creation_batch.from_dict(create_analysis_creation_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


