# CreateNotificationChannel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Should this channel be enabled or not? | 
**type** | **str** | The type of delivery target (MAIL, SQS, SNS, HTTP, ...) | 
**address** | **str** | The address where to send a notification to (email address, url, ...) | 

## Example

```python
from icasdk.models.create_notification_channel import CreateNotificationChannel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationChannel from a JSON string
create_notification_channel_instance = CreateNotificationChannel.from_json(json)
# print the JSON string representation of the object
print CreateNotificationChannel.to_json()

# convert the object into a dict
create_notification_channel_dict = create_notification_channel_instance.to_dict()
# create an instance of CreateNotificationChannel from a dict
create_notification_channel_form_dict = create_notification_channel.from_dict(create_notification_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


