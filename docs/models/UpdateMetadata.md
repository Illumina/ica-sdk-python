# icasdk.model.update_metadata.UpdateMetadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[updateSingleMetadataFields](#updateSingleMetadataFields)** | list, tuple, None,  | tuple, NoneClass,  | List of metadata fields to be updated | [optional] 
**[updateMetadataFieldGroups](#updateMetadataFieldGroups)** | list, tuple, None,  | tuple, NoneClass,  | List of metadata field groups to be updated | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# updateSingleMetadataFields

List of metadata fields to be updated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of metadata fields to be updated | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UpdateSingleMetadataField**](UpdateSingleMetadataField.md) | [**UpdateSingleMetadataField**](UpdateSingleMetadataField.md) | [**UpdateSingleMetadataField**](UpdateSingleMetadataField.md) |  | 

# updateMetadataFieldGroups

List of metadata field groups to be updated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of metadata field groups to be updated | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UpdateMetadataFieldGroup**](UpdateMetadataFieldGroup.md) | [**UpdateMetadataFieldGroup**](UpdateMetadataFieldGroup.md) | [**UpdateMetadataFieldGroup**](UpdateMetadataFieldGroup.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

