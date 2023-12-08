# BundleToolsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BundleTool]**](BundleTool.md) |  | 

## Example

```python
from icasdk.models.bundle_tools_list import BundleToolsList

# TODO update the JSON string below
json = "{}"
# create an instance of BundleToolsList from a JSON string
bundle_tools_list_instance = BundleToolsList.from_json(json)
# print the JSON string representation of the object
print BundleToolsList.to_json()

# convert the object into a dict
bundle_tools_list_dict = bundle_tools_list_instance.to_dict()
# create an instance of BundleToolsList from a dict
bundle_tools_list_form_dict = bundle_tools_list.from_dict(bundle_tools_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


