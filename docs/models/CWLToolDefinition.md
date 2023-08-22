# icasdk.model.cwl_tool_definition.CWLToolDefinition

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name of the tool definition | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  | Status of the tool definition | must be one of ["DRAFT", "RELEASED", "DEPRECATED", "RELEASECANDIDATE", "BUILDING", "BUILDFAILED", ] 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  | Description of the tool definition | [optional] 
**versionComment** | None, str,  | NoneClass, str,  | version comment of the tool definition | [optional] 
**releaseVersion** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | release version of the tool definition | [optional] value must be a 32 bit integer
**links** | [**Link**](Link.md) | [**Link**](Link.md) |  | [optional] 
**[categories](#categories)** | list, tuple, None,  | tuple, NoneClass,  | category tags as string array | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

category tags as string array

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | category tags as string array | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | category tags as string array | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

