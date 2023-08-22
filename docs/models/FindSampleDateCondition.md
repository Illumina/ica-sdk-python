# icasdk.model.find_sample_date_condition.FindSampleDateCondition

Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadataField** | [**FieldId**](FieldId.md) | [**FieldId**](FieldId.md) |  | [optional] 
**field** | None, str,  | NoneClass, str,  |  | [optional] 
**beforeDate** | None, str,  | NoneClass, str,  | Before date. Format: yyyy-MM-dd&#x27;T&#x27;HH:mm:ss.SSS&#x27;Z&#x27; eg: 2017-01-10T10:47:56.039Z | [optional] 
**afterDate** | None, str,  | NoneClass, str,  | After date. Format: yyyy-MM-dd&#x27;T&#x27;HH:mm:ss.SSS&#x27;Z&#x27; eg: 2017-01-10T10:47:56.039Z | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

