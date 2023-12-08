# OptionalSampleTags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 
**connector_tags** | **List[str]** |  | [optional] 
**run_in_tags** | **List[str]** |  | [optional] 

## Example

```python
from icasdk.models.optional_sample_tags import OptionalSampleTags

# TODO update the JSON string below
json = "{}"
# create an instance of OptionalSampleTags from a JSON string
optional_sample_tags_instance = OptionalSampleTags.from_json(json)
# print the JSON string representation of the object
print OptionalSampleTags.to_json()

# convert the object into a dict
optional_sample_tags_dict = optional_sample_tags_instance.to_dict()
# create an instance of OptionalSampleTags from a dict
optional_sample_tags_form_dict = optional_sample_tags.from_dict(optional_sample_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

