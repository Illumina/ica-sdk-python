# CustomNotificationSubscriptionList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CustomNotificationSubscription]**](CustomNotificationSubscription.md) |  | 

## Example

```python
from icasdk.models.custom_notification_subscription_list import CustomNotificationSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNotificationSubscriptionList from a JSON string
custom_notification_subscription_list_instance = CustomNotificationSubscriptionList.from_json(json)
# print the JSON string representation of the object
print CustomNotificationSubscriptionList.to_json()

# convert the object into a dict
custom_notification_subscription_list_dict = custom_notification_subscription_list_instance.to_dict()
# create an instance of CustomNotificationSubscriptionList from a dict
custom_notification_subscription_list_form_dict = custom_notification_subscription_list.from_dict(custom_notification_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


