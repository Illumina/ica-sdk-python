# CreateCwlPipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the CWL pipeline | 
**description** | **str** | The description of the CWL pipeline | 
**workflow_cwl_file** | **bytearray** | The CWL workflow file. | 
**tool_cwl_files** | **List[bytearray]** |  | [optional] 
**parameters_xml_file** | **bytearray** |  | 
**metadata_model_file** | **bytearray** | The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**version_comment** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**html_documentation** | **str** |  | [optional] 
**analysis_storage_id** | **str** | The id of the storage to use for the pipeline. | 

## Example

```python
from icasdk.models.create_cwl_pipeline import CreateCwlPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCwlPipeline from a JSON string
create_cwl_pipeline_instance = CreateCwlPipeline.from_json(json)
# print the JSON string representation of the object
print CreateCwlPipeline.to_json()

# convert the object into a dict
create_cwl_pipeline_dict = create_cwl_pipeline_instance.to_dict()
# create an instance of CreateCwlPipeline from a dict
create_cwl_pipeline_form_dict = create_cwl_pipeline.from_dict(create_cwl_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


