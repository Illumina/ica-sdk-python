# icasdk.model.sample.Sample

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[metadata](#metadata)** | list, tuple,  | tuple,  | The metadata of the sample | 
**name** | str,  | str,  | The name of the sample | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**metadataValid** | bool,  | BoolClass,  | Whether the metadata is valid | 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**region** | [**Region**](Region.md) | [**Region**](Region.md) |  | 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | must be one of ["DELETED", "AVAILABLE", "PARTIAL", ] 
**tags** | [**SampleTag**](SampleTag.md) | [**SampleTag**](SampleTag.md) |  | 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  | The description of the sample | [optional] 
**[sequencingRuns](#sequencingRuns)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

The metadata of the sample

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The metadata of the sample | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MetadataField**](MetadataField.md) | [**MetadataField**](MetadataField.md) | [**MetadataField**](MetadataField.md) |  | 

# sequencingRuns

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SequencingRun**](SequencingRun.md) | [**SequencingRun**](SequencingRun.md) | [**SequencingRun**](SequencingRun.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

