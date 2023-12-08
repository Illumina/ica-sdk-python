# ProjectBundle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | [**Bundle**](Bundle.md) |  | 
**project_id** | **str** |  | 

## Example

```python
from icasdk.models.project_bundle import ProjectBundle

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBundle from a JSON string
project_bundle_instance = ProjectBundle.from_json(json)
# print the JSON string representation of the object
print ProjectBundle.to_json()

# convert the object into a dict
project_bundle_dict = project_bundle_instance.to_dict()
# create an instance of ProjectBundle from a dict
project_bundle_form_dict = project_bundle.from_dict(project_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


