# CreateNotificationSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_code** | **str** | The event code to subscribe to | 
**filter_expression** | **str** | To be used when a notification applies to specific conditions. | [optional] 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel_id** | **str** | The ID of the notification channel used to send on | 

## Example

```python
from icasdk.models.create_notification_subscription import CreateNotificationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationSubscription from a JSON string
create_notification_subscription_instance = CreateNotificationSubscription.from_json(json)
# print the JSON string representation of the object
print CreateNotificationSubscription.to_json()

# convert the object into a dict
create_notification_subscription_dict = create_notification_subscription_instance.to_dict()
# create an instance of CreateNotificationSubscription from a dict
create_notification_subscription_form_dict = create_notification_subscription.from_dict(create_notification_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


