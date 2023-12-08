# AnalysisStorage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**name** | **str** | The name of the storage option | 
**description** | **str** | The description about the storage option | [optional] 

## Example

```python
from icasdk.models.analysis_storage import AnalysisStorage

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStorage from a JSON string
analysis_storage_instance = AnalysisStorage.from_json(json)
# print the JSON string representation of the object
print AnalysisStorage.to_json()

# convert the object into a dict
analysis_storage_dict = analysis_storage_instance.to_dict()
# create an instance of AnalysisStorage from a dict
analysis_storage_form_dict = analysis_storage.from_dict(analysis_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


