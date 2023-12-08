# InputParameterList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[InputParameter]**](InputParameter.md) |  | 

## Example

```python
from icasdk.models.input_parameter_list import InputParameterList

# TODO update the JSON string below
json = "{}"
# create an instance of InputParameterList from a JSON string
input_parameter_list_instance = InputParameterList.from_json(json)
# print the JSON string representation of the object
print InputParameterList.to_json()

# convert the object into a dict
input_parameter_list_dict = input_parameter_list_instance.to_dict()
# create an instance of InputParameterList from a dict
input_parameter_list_form_dict = input_parameter_list.from_dict(input_parameter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


