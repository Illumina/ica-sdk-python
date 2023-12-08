# ProjectDataLinkingBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**job** | [**Job**](Job.md) |  | 

## Example

```python
from icasdk.models.project_data_linking_batch import ProjectDataLinkingBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDataLinkingBatch from a JSON string
project_data_linking_batch_instance = ProjectDataLinkingBatch.from_json(json)
# print the JSON string representation of the object
print ProjectDataLinkingBatch.to_json()

# convert the object into a dict
project_data_linking_batch_dict = project_data_linking_batch_instance.to_dict()
# create an instance of ProjectDataLinkingBatch from a dict
project_data_linking_batch_form_dict = project_data_linking_batch.from_dict(project_data_linking_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

