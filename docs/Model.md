# Model


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**models** | [**List[Model]**](Model.md) |  | [optional] 
**fields** | [**List[Field]**](Field.md) |  | [optional] 

## Example

```python
from icasdk.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print Model.to_json()

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_form_dict = model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


