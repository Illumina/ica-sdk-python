# icasdk.model.project_permission.ProjectPermission

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**uploadAllowed** | bool,  | BoolClass,  |  | 
**membershipType** | str,  | str,  |  | must be one of ["USER", "EMAIL", "WORKGROUP", ] 
**roleFlow** | str,  | str,  |  | must be one of ["NONE", "VIEWER", "CONTRIBUTOR", ] 
**roleBase** | str,  | str,  |  | must be one of ["NONE", "VIEWER", "CONTRIBUTOR", ] 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**downloadAllowed** | bool,  | BoolClass,  |  | 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**roleBench** | str,  | str,  |  | must be one of ["NONE", "CONTRIBUTOR", ] 
**roleProject** | str,  | str,  |  | must be one of ["NONE", "VIEWER", "CONTRIBUTOR", "ADMINISTRATOR", "DATA_PROVIDER", ] 
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**user** | [**User**](User.md) | [**User**](User.md) |  | [optional] 
**emailAddress** | None, str,  | NoneClass, str,  | Only present when membershipType is EMAIL | [optional] 
**workgroup** | [**Workgroup**](Workgroup.md) | [**Workgroup**](Workgroup.md) |  | [optional] 
**invitationAccepted** | None, bool,  | NoneClass, BoolClass,  | Only present when membershipType is EMAIL | [optional] 
**invitationRejected** | None, bool,  | NoneClass, BoolClass,  | Only present when user is invited by EMAIL | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

