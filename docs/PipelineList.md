# PipelineList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Pipeline]**](Pipeline.md) |  | 

## Example

```python
from icasdk.models.pipeline_list import PipelineList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineList from a JSON string
pipeline_list_instance = PipelineList.from_json(json)
# print the JSON string representation of the object
print PipelineList.to_json()

# convert the object into a dict
pipeline_list_dict = pipeline_list_instance.to_dict()
# create an instance of PipelineList from a dict
pipeline_list_form_dict = pipeline_list.from_dict(pipeline_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


