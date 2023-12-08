# AnalysisRawOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_output** | **str** | The raw output of the analysis. | 

## Example

```python
from icasdk.models.analysis_raw_output import AnalysisRawOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisRawOutput from a JSON string
analysis_raw_output_instance = AnalysisRawOutput.from_json(json)
# print the JSON string representation of the object
print AnalysisRawOutput.to_json()

# convert the object into a dict
analysis_raw_output_dict = analysis_raw_output_instance.to_dict()
# create an instance of AnalysisRawOutput from a dict
analysis_raw_output_form_dict = analysis_raw_output.from_dict(analysis_raw_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


