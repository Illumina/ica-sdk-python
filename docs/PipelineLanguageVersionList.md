# PipelineLanguageVersionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PipelineLanguageVersion]**](PipelineLanguageVersion.md) |  | 

## Example

```python
from icasdk.models.pipeline_language_version_list import PipelineLanguageVersionList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineLanguageVersionList from a JSON string
pipeline_language_version_list_instance = PipelineLanguageVersionList.from_json(json)
# print the JSON string representation of the object
print PipelineLanguageVersionList.to_json()

# convert the object into a dict
pipeline_language_version_list_dict = pipeline_language_version_list_instance.to_dict()
# create an instance of PipelineLanguageVersionList from a dict
pipeline_language_version_list_form_dict = pipeline_language_version_list.from_dict(pipeline_language_version_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


