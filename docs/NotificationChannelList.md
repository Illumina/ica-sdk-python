# NotificationChannelList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NotificationChannel]**](NotificationChannel.md) |  | 

## Example

```python
from icasdk.models.notification_channel_list import NotificationChannelList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelList from a JSON string
notification_channel_list_instance = NotificationChannelList.from_json(json)
# print the JSON string representation of the object
print NotificationChannelList.to_json()

# convert the object into a dict
notification_channel_list_dict = notification_channel_list_instance.to_dict()
# create an instance of NotificationChannelList from a dict
notification_channel_list_form_dict = notification_channel_list.from_dict(notification_channel_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

