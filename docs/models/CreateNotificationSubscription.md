# icasdk.model.create_notification_subscription.CreateNotificationSubscription

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**eventCode** | str,  | str,  | The event code to subscribe to | 
**notificationChannelId** | str, uuid.UUID,  | str,  | The ID of the notification channel used to send on | value must be a uuid
**enabled** | bool,  | BoolClass,  | Should this subscription be enabled or not? | 
**filterExpression** | None, str,  | NoneClass, str,  | To be used when a notification applies to specific conditions. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

