# icasdk.model.storage_configuration_with_details.StorageConfigurationWithDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**isDefault** | bool,  | BoolClass,  | An indication if this is the default in region for new projects | 
**storageConfigurationDetails** | [**StorageConfigurationDetails**](StorageConfigurationDetails.md) | [**StorageConfigurationDetails**](StorageConfigurationDetails.md) |  | 
**name** | str,  | str,  | The name of the storage configuration | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**region** | [**Region**](Region.md) | [**Region**](Region.md) |  | 
**type** | str,  | str,  |  | must be one of ["AWS_S3", ] 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | must be one of ["INITIALIZING", "OK", "ERROR", ] 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  | An optional description | [optional] 
**errorMessage** | None, str,  | NoneClass, str,  | An optional error message when something went wrong with the configuration | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

