# ProjectPipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline** | [**Pipeline**](Pipeline.md) |  | 
**project_id** | **str** |  | 
**bundle_links** | [**BundleList**](BundleList.md) |  | 

## Example

```python
from icasdk.models.project_pipeline import ProjectPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPipeline from a JSON string
project_pipeline_instance = ProjectPipeline.from_json(json)
# print the JSON string representation of the object
print ProjectPipeline.to_json()

# convert the object into a dict
project_pipeline_dict = project_pipeline_instance.to_dict()
# create an instance of ProjectPipeline from a dict
project_pipeline_form_dict = project_pipeline.from_dict(project_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

