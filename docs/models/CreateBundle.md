# icasdk.model.create_bundle.CreateBundle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**regionId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**bundleReleaseVersion** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**[categories](#categories)** | list, tuple,  | tuple,  | category tags as string array | 
**bundleStatus** | str,  | str,  |  | must be one of ["DRAFT", "RELEASED", "DEPRECATED", ] 
**shortDescription** | None, str,  | NoneClass, str,  |  | [optional] 
**bundleVersionComment** | None, str,  | NoneClass, str,  |  | [optional] 
**metadataModelId** | None, str, uuid.UUID,  | NoneClass, str,  |  | [optional] value must be a uuid
**links** | [**Links**](Links.md) | [**Links**](Links.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# categories

category tags as string array

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | category tags as string array | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | category tags as string array | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

