# icasdk.model.sample_history.SampleHistory

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**occurredAt** | str, datetime,  | str,  | When the change was made | value must conform to RFC-3339 date-time
**source** | str,  | str,  | In which context the change was made | 
**text** | str,  | str,  | What was changed | 
**user** | None, str, uuid.UUID,  | NoneClass, str,  | The user that made the change | [optional] value must be a uuid
**run** | None, str, uuid.UUID,  | NoneClass, str,  | In which execution context the change was made | [optional] value must be a uuid
**project** | None, str, uuid.UUID,  | NoneClass, str,  | In which project context the change was made | [optional] value must be a uuid
**model** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | In which model context the change was made | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

