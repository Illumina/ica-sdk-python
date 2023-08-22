# icasdk.model.data_details.DataDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dataType** | str,  | str,  |  | must be one of ["FILE", "FOLDER", ] 
**name** | str,  | str,  | The name of the file/folder as it was uploaded. | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**owningProjectId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**status** | str,  | str,  |  | must be one of ["PARTIAL", "AVAILABLE", "ARCHIVING", "ARCHIVED", "UNARCHIVING", "DELETING", ] 
**tags** | [**DataTag**](DataTag.md) | [**DataTag**](DataTag.md) |  | 
**creatorId** | None, str, uuid.UUID,  | NoneClass, str,  |  | [optional] value must be a uuid
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**owningProjectName** | None, str,  | NoneClass, str,  |  | [optional] 
**path** | None, str,  | NoneClass, str,  | The user friendly path of the parent of this data. | [optional] 
**fileSizeInBytes** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The size of the file in bytes. Folders do not have a size. | [optional] value must be a 64 bit integer
**format** | [**DataFormat**](DataFormat.md) | [**DataFormat**](DataFormat.md) |  | [optional] 
**objectETag** | None, str,  | NoneClass, str,  | The file&#x27;s ETag, as received from the cloud provider. Not to be confused with the ETag reponse header of this API. | [optional] 
**storedForTheFirstTimeAt** | None, str, datetime,  | NoneClass, str,  | Specifies when the data object was stored for the first time | [optional] value must conform to RFC-3339 date-time
**region** | [**Region**](Region.md) | [**Region**](Region.md) |  | [optional] 
**willBeArchivedAt** | None, str, datetime,  | NoneClass, str,  | Specifies when the data object will be archived. | [optional] value must conform to RFC-3339 date-time
**willBeDeletedAt** | None, str, datetime,  | NoneClass, str,  | Specifies when the data object will be deleted. | [optional] value must conform to RFC-3339 date-time
**sequencingRun** | [**SequencingRun**](SequencingRun.md) | [**SequencingRun**](SequencingRun.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

