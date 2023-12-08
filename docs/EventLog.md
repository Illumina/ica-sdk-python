# EventLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**code** | **str** | The code of the event | 
**description** | **str** | The details of the event | 
**event_type_category** | **str** | The type of the event | 
**user_id** | **str** |  | 

## Example

```python
from icasdk.models.event_log import EventLog

# TODO update the JSON string below
json = "{}"
# create an instance of EventLog from a JSON string
event_log_instance = EventLog.from_json(json)
# print the JSON string representation of the object
print EventLog.to_json()

# convert the object into a dict
event_log_dict = event_log_instance.to_dict()
# create an instance of EventLog from a dict
event_log_form_dict = event_log.from_dict(event_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


