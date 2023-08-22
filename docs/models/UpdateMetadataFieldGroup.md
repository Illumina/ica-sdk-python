# icasdk.model.update_metadata_field_group.UpdateMetadataFieldGroup

List of metadata field groups to be updated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | List of metadata field groups to be updated | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**index** | decimal.Decimal, int,  | decimal.Decimal,  | Which metadata row index to update | value must be a 32 bit integer
**[updateSingleMetadataFields](#updateSingleMetadataFields)** | list, tuple,  | tuple,  | List of metadata fields to be updated | 
**fieldId** | [**FieldId**](FieldId.md) | [**FieldId**](FieldId.md) |  | [optional] 
**fieldName** | None, str,  | NoneClass, str,  | The field name to be updated. Either the field ID or field name is required. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# updateSingleMetadataFields

List of metadata fields to be updated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of metadata fields to be updated | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UpdateSingleMetadataField**](UpdateSingleMetadataField.md) | [**UpdateSingleMetadataField**](UpdateSingleMetadataField.md) | [**UpdateSingleMetadataField**](UpdateSingleMetadataField.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

