# CreateSample


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the sample. | 
**description** | **str** | The description of the sample. | [optional] 
**tags** | [**OptionalSampleTags**](OptionalSampleTags.md) |  | [optional] 

## Example

```python
from icasdk.models.create_sample import CreateSample

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSample from a JSON string
create_sample_instance = CreateSample.from_json(json)
# print the JSON string representation of the object
print CreateSample.to_json()

# convert the object into a dict
create_sample_dict = create_sample_instance.to_dict()
# create an instance of CreateSample from a dict
create_sample_form_dict = create_sample.from_dict(create_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


