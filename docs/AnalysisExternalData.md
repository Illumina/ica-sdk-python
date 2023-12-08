# AnalysisExternalData

The external data used as input by the analysis.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** | Possible values are: s3, http. More types could be added in a future release. | 
**mount_path** | **str** |  | 

## Example

```python
from icasdk.models.analysis_external_data import AnalysisExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisExternalData from a JSON string
analysis_external_data_instance = AnalysisExternalData.from_json(json)
# print the JSON string representation of the object
print AnalysisExternalData.to_json()

# convert the object into a dict
analysis_external_data_dict = analysis_external_data_instance.to_dict()
# create an instance of AnalysisExternalData from a dict
analysis_external_data_form_dict = analysis_external_data.from_dict(analysis_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


