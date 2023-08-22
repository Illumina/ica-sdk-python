# icasdk.model.bundle.Bundle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**releaseVersion** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**region** | [**Region**](Region.md) | [**Region**](Region.md) |  | 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | must be one of ["DRAFT", "RELEASED", "DEPRECATED", ] 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**shortDescription** | None, str,  | NoneClass, str,  |  | [optional] 
**metadataModel** | [**MetadataModel**](MetadataModel.md) | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**versionComment** | None, str,  | NoneClass, str,  |  | [optional] 
**[categories](#categories)** | list, tuple, None,  | tuple, NoneClass,  | category tags as string array | [optional] 
**links** | [**Links**](Links.md) | [**Links**](Links.md) |  | [optional] 
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

