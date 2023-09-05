# icasdk.model.project.Project

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**billingMode** | str,  | str,  | The billing mode of the project. It determines who pays for the costs linked to the project. | must be one of ["PROJECT", "TENANT", ] 
**name** | str,  | str,  |  | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**active** | bool,  | BoolClass,  | Indicates whether the project is active or hidden. | 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**region** | [**Region**](Region.md) | [**Region**](Region.md) |  | 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**tags** | [**ProjectTag**](ProjectTag.md) | [**ProjectTag**](ProjectTag.md) |  | 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**urn** | None, str,  | NoneClass, str,  | The URN of the project. The format is urn:ilmn:ica:\\&lt;type of the object\\&gt;:\\&lt;ID of the object\\&gt;#\\&lt;optional human readable hint representing the object\\&gt;. The hint can be omitted, in that case the hashtag (#) must also be omitted. | [optional] 
**baseEnabled** | None, bool,  | NoneClass, BoolClass,  | Indicates whether the project is base enabled. | [optional] 
**shortDescription** | None, str,  | NoneClass, str,  |  | [optional] 
**information** | None, str,  | NoneClass, str,  | Information about the project. Note that the value of this field can be arbitrary large. | [optional] 
**dataSharingEnabled** | None, bool,  | NoneClass, BoolClass,  | Indicates whether the Data and Samples created in this Project can be linked to other Projects. | [optional] 
**storageBundle** | [**StorageBundle**](StorageBundle.md) | [**StorageBundle**](StorageBundle.md) |  | [optional] 
**selfManagedStorageConfiguration** | [**StorageConfiguration**](StorageConfiguration.md) | [**StorageConfiguration**](StorageConfiguration.md) |  | [optional] 
**analysisPriority** | None, str,  | NoneClass, str,  | Indicates the priority given to a project and its analyses within a single tenant. Note that for a PUT call, when not providing a value for this attribute (null value or absent attribute), the persisted value will not change. | [optional] must be one of ["LOW", "MEDIUM", "HIGH", ] 
**metadataModel** | [**MetadataModel**](MetadataModel.md) | [**MetadataModel**](MetadataModel.md) |  | [optional] 
**application** | [**Application**](Application.md) | [**Application**](Application.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

