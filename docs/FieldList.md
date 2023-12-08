# FieldList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Field]**](Field.md) |  | 

## Example

```python
from icasdk.models.field_list import FieldList

# TODO update the JSON string below
json = "{}"
# create an instance of FieldList from a JSON string
field_list_instance = FieldList.from_json(json)
# print the JSON string representation of the object
print FieldList.to_json()

# convert the object into a dict
field_list_dict = field_list_instance.to_dict()
# create an instance of FieldList from a dict
field_list_form_dict = field_list.from_dict(field_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


