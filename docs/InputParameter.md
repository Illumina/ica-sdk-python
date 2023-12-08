# InputParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the parameter | 
**code** | **str** | The code of the parameter | 
**required** | **bool** | Indicates whether this parameter is required | 
**multi_value** | **bool** | Indicates whether multiple values are allowed for this parameter | 

## Example

```python
from icasdk.models.input_parameter import InputParameter

# TODO update the JSON string below
json = "{}"
# create an instance of InputParameter from a JSON string
input_parameter_instance = InputParameter.from_json(json)
# print the JSON string representation of the object
print InputParameter.to_json()

# convert the object into a dict
input_parameter_dict = input_parameter_instance.to_dict()
# create an instance of InputParameter from a dict
input_parameter_form_dict = input_parameter.from_dict(input_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


