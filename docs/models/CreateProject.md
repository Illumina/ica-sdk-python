# icasdk.model.create_project.CreateProject

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**billingMode** | str,  | str,  | The billing mode of the project. It determines who pays for the costs linked to the project. | must be one of ["PROJECT", "TENANT", ] 
**regionId** | str, uuid.UUID,  | str,  | The region of the project. All data and pipeline executions will reside in this region. | value must be a uuid
**storageBundleId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**dataSharingEnabled** | bool,  | BoolClass,  | Indicates whether the Data and Samples created in this Project can be linked to other Projects. | 
**name** | str,  | str,  |  | 
**shortDescription** | None, str,  | NoneClass, str,  |  | [optional] 
**information** | None, str,  | NoneClass, str,  | Information about the project. Note that the value of this field can be arbitrary large. | [optional] 
**projectOwnerId** | None, str, uuid.UUID,  | NoneClass, str,  | Owner of the project. Defaults to the current user. | [optional] value must be a uuid
**tags** | [**ProjectTag**](ProjectTag.md) | [**ProjectTag**](ProjectTag.md) |  | [optional] 
**metadataModelId** | None, str, uuid.UUID,  | NoneClass, str,  |  | [optional] value must be a uuid
**storageConfigurationId** | None, str, uuid.UUID,  | NoneClass, str,  | An optional storage configuration id to have self managed storage. | [optional] value must be a uuid
**storageConfigurationSubfolder** | None, str,  | NoneClass, str,  | An optional subfolder that determines the object prefix of your self managed storage.  If not used, you will not be able to use this storage configuration for any future projects. | [optional] 
**analysisPriority** | None, str,  | NoneClass, str,  | Indicates the priority given to a project and its analyses within a single tenant, where MEDIUM is the default value. | [optional] must be one of ["LOW", "MEDIUM", "HIGH", ] if omitted the server will use the default value of "MEDIUM"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

