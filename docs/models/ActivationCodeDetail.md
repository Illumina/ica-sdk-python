# icasdk.model.activation_code_detail.ActivationCodeDetail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allowedSlots** | decimal.Decimal, int,  | decimal.Decimal,  | The allowed slot within this code, -1 means unlimited | value must be a 32 bit integer
**originalSlots** | decimal.Decimal, int,  | decimal.Decimal,  | The assigned allowed slot within this code, -1 means unlimited | value must be a 32 bit integer
**pipelineBundle** | [**PipelineBundle**](PipelineBundle.md) | [**PipelineBundle**](PipelineBundle.md) |  | 
**usedSlots** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates how many slots can are used. | value must be a 32 bit integer
**movedSlots** | decimal.Decimal, int,  | decimal.Decimal,  | The slots that where moved to another activation code | value must be a 32 bit integer
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**[usages](#usages)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# usages

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ActivationCodeDetailUsage**](ActivationCodeDetailUsage.md) | [**ActivationCodeDetailUsage**](ActivationCodeDetailUsage.md) | [**ActivationCodeDetailUsage**](ActivationCodeDetailUsage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

