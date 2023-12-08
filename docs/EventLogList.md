# EventLogList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EventLog]**](EventLog.md) |  | 

## Example

```python
from icasdk.models.event_log_list import EventLogList

# TODO update the JSON string below
json = "{}"
# create an instance of EventLogList from a JSON string
event_log_list_instance = EventLogList.from_json(json)
# print the JSON string representation of the object
print EventLogList.to_json()

# convert the object into a dict
event_log_list_dict = event_log_list_instance.to_dict()
# create an instance of EventLogList from a dict
event_log_list_form_dict = event_log_list.from_dict(event_log_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


