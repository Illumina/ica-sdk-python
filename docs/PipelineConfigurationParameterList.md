# PipelineConfigurationParameterList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PipelineConfigurationParameter]**](PipelineConfigurationParameter.md) |  | 

## Example

```python
from icasdk.models.pipeline_configuration_parameter_list import PipelineConfigurationParameterList

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineConfigurationParameterList from a JSON string
pipeline_configuration_parameter_list_instance = PipelineConfigurationParameterList.from_json(json)
# print the JSON string representation of the object
print PipelineConfigurationParameterList.to_json()

# convert the object into a dict
pipeline_configuration_parameter_list_dict = pipeline_configuration_parameter_list_instance.to_dict()
# create an instance of PipelineConfigurationParameterList from a dict
pipeline_configuration_parameter_list_form_dict = pipeline_configuration_parameter_list.from_dict(pipeline_configuration_parameter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


