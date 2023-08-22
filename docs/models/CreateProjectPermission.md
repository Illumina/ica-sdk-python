# icasdk.model.create_project_permission.CreateProjectPermission

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uploadAllowed** | bool,  | BoolClass,  | Indicates if uploading data is allowed or not. | 
**membershipType** | str,  | str,  | How users are invited to the project | must be one of ["USER", "EMAIL", "WORKGROUP", ] 
**roleFlow** | str,  | str,  |  | must be one of ["NONE", "VIEWER", "CONTRIBUTOR", ] 
**roleBase** | str,  | str,  |  | must be one of ["NONE", "VIEWER", "CONTRIBUTOR", ] 
**downloadAllowed** | bool,  | BoolClass,  | Indicates if downloading data is allowed or not. | 
**roleBench** | str,  | str,  |  | must be one of ["NONE", "CONTRIBUTOR", ] 
**roleProject** | str,  | str,  |  | must be one of ["NONE", "VIEWER", "CONTRIBUTOR", "ADMINISTRATOR", "DATA_PROVIDER", ] 
**userId** | None, str, uuid.UUID,  | NoneClass, str,  | the id of the user that should be given access, required when membershipType is USER | [optional] value must be a uuid
**emailAddress** | None, str,  | NoneClass, str,  | The email to invite a user on, required when membershipType is EMAIL | [optional] 
**workgroupId** | None, str, uuid.UUID,  | NoneClass, str,  | the id of the workgroup to give access, required when membershipType is WORKGROUP | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

