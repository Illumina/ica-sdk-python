# icasdk.model.create_storage_configuration.CreateStorageConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**regionId** | str, uuid.UUID,  | str,  | The id of the region where the bucket will be located | value must be a uuid
**name** | str,  | str,  | The name of the configuration | 
**storageCredentialId** | str, uuid.UUID,  | str,  | The id of the storage credential | value must be a uuid
**type** | str,  | str,  | The type of configuration | must be one of ["AWS_S3", ] 
**description** | None, str,  | NoneClass, str,  | An optional description | [optional] 
**awsDetails** | [**AWSDetails**](AWSDetails.md) | [**AWSDetails**](AWSDetails.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

