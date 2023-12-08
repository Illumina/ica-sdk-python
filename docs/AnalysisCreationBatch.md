# AnalysisCreationBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | [optional] 

## Example

```python
from icasdk.models.analysis_creation_batch import AnalysisCreationBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCreationBatch from a JSON string
analysis_creation_batch_instance = AnalysisCreationBatch.from_json(json)
# print the JSON string representation of the object
print AnalysisCreationBatch.to_json()

# convert the object into a dict
analysis_creation_batch_dict = analysis_creation_batch_instance.to_dict()
# create an instance of AnalysisCreationBatch from a dict
analysis_creation_batch_form_dict = analysis_creation_batch.from_dict(analysis_creation_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


