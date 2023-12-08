# CreateNextflowPipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the pipeline | 
**pipeline_language_version_id** | **str** | The id of the Nextflow version to use for the pipeline. | [optional] 
**description** | **str** | The description of the pipeline | 
**main_nextflow_file** | **bytearray** | The main Nextflow file. | 
**nextflow_config_file** | **bytearray** | The Nextflow config file. | [optional] 
**other_nextflow_files** | **List[bytearray]** |  | [optional] 
**parameters_xml_file** | **bytearray** |  | 
**metadata_model_file** | **bytearray** | The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**version_comment** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**html_documentation** | **str** |  | [optional] 
**analysis_storage_id** | **str** | The id of the storage to use for the pipeline. | 

## Example

```python
from icasdk.models.create_nextflow_pipeline import CreateNextflowPipeline

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNextflowPipeline from a JSON string
create_nextflow_pipeline_instance = CreateNextflowPipeline.from_json(json)
# print the JSON string representation of the object
print CreateNextflowPipeline.to_json()

# convert the object into a dict
create_nextflow_pipeline_dict = create_nextflow_pipeline_instance.to_dict()
# create an instance of CreateNextflowPipeline from a dict
create_nextflow_pipeline_form_dict = create_nextflow_pipeline.from_dict(create_nextflow_pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


