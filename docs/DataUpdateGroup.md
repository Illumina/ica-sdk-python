# DataUpdateGroup

Updates to apply.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ids** | **List[str]** |  | 
**user_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 
**technical_tags** | [**TagUpdate**](TagUpdate.md) |  | [optional] 

## Example

```python
from icasdk.models.data_update_group import DataUpdateGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DataUpdateGroup from a JSON string
data_update_group_instance = DataUpdateGroup.from_json(json)
# print the JSON string representation of the object
print DataUpdateGroup.to_json()

# convert the object into a dict
data_update_group_dict = data_update_group_instance.to_dict()
# create an instance of DataUpdateGroup from a dict
data_update_group_form_dict = data_update_group.from_dict(data_update_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


