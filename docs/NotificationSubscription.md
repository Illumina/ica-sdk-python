# NotificationSubscription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**time_created** | **datetime** |  | 
**time_modified** | **datetime** |  | 
**owner_id** | **str** |  | 
**tenant_id** | **str** |  | 
**tenant_name** | **str** |  | [optional] 
**event_code** | **str** | The event code to subscribe to | 
**filter_expression** | **str** | To be used when a notification applies to specific conditions. | [optional] 
**enabled** | **bool** | Should this subscription be enabled or not? | 
**notification_channel** | [**NotificationChannel**](NotificationChannel.md) |  | 

## Example

```python
from icasdk.models.notification_subscription import NotificationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSubscription from a JSON string
notification_subscription_instance = NotificationSubscription.from_json(json)
# print the JSON string representation of the object
print NotificationSubscription.to_json()

# convert the object into a dict
notification_subscription_dict = notification_subscription_instance.to_dict()
# create an instance of NotificationSubscription from a dict
notification_subscription_form_dict = notification_subscription.from_dict(notification_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


