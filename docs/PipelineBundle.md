# PipelineBundle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**max_number_of_allowed_slots** | **int** |  | 
**active_pipelines** | [**List[Pipeline]**](Pipeline.md) |  | 
**canceled_pipelines** | [**List[Pipeline]**](Pipeline.md) |  | 
**retired_pipelines** | [**List[Pipeline]**](Pipeline.md) |  | 
**regions** | [**List[Region]**](Region.md) |  | 
**analysis_storages** | [**List[AnalysisStorage]**](AnalysisStorage.md) |  | 

## Example

```python
from icasdk.models.pipeline_bundle import PipelineBundle

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineBundle from a JSON string
pipeline_bundle_instance = PipelineBundle.from_json(json)
# print the JSON string representation of the object
print PipelineBundle.to_json()

# convert the object into a dict
pipeline_bundle_dict = pipeline_bundle_instance.to_dict()
# create an instance of PipelineBundle from a dict
pipeline_bundle_form_dict = pipeline_bundle.from_dict(pipeline_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


