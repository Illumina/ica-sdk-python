# BundleData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Data**](Data.md) |  | 
**bundle_id** | **str** |  | 

## Example

```python
from icasdk.models.bundle_data import BundleData

# TODO update the JSON string below
json = "{}"
# create an instance of BundleData from a JSON string
bundle_data_instance = BundleData.from_json(json)
# print the JSON string representation of the object
print BundleData.to_json()

# convert the object into a dict
bundle_data_dict = bundle_data_instance.to_dict()
# create an instance of BundleData from a dict
bundle_data_form_dict = bundle_data.from_dict(bundle_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


