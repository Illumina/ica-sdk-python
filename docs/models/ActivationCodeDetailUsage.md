# icasdk.model.activation_code_detail_usage.ActivationCodeDetailUsage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allowedSlots** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates how many slots can be used, -1 means unlimited | value must be a 32 bit integer
**usedSlots** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates how many slots can are used, -1 means unused | value must be a 32 bit integer
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**project** | [**Project**](Project.md) | [**Project**](Project.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

