# DataTag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technical_tags** | **List[str]** |  | [optional] 
**user_tags** | **List[str]** |  | [optional] 
**connector_tags** | **List[str]** |  | [optional] 
**run_in_tags** | **List[str]** |  | [optional] 
**run_out_tags** | **List[str]** |  | [optional] 
**reference_tags** | **List[str]** |  | [optional] 

## Example

```python
from icasdk.models.data_tag import DataTag

# TODO update the JSON string below
json = "{}"
# create an instance of DataTag from a JSON string
data_tag_instance = DataTag.from_json(json)
# print the JSON string representation of the object
print DataTag.to_json()

# convert the object into a dict
data_tag_dict = data_tag_instance.to_dict()
# create an instance of DataTag from a dict
data_tag_form_dict = data_tag.from_dict(data_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


