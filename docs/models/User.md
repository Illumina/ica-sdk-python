# icasdk.model.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**emailVerified** | bool,  | BoolClass,  |  | 
**tenantId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**twoFactorAuthentication** | bool,  | BoolClass,  |  | 
**active** | bool,  | BoolClass,  |  | 
**tenantAdministrator** | bool,  | BoolClass,  |  | 
**timeCreated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**ownerId** | str, uuid.UUID,  | str,  |  | value must be a uuid
**timeModified** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**email** | str,  | str,  |  | 
**username** | str,  | str,  |  | 
**tenantName** | None, str,  | NoneClass, str,  |  | [optional] 
**firstname** | None, str,  | NoneClass, str,  |  | [optional] 
**lastname** | None, str,  | NoneClass, str,  |  | [optional] 
**jobTitle** | None, str,  | NoneClass, str,  |  | [optional] 
**greeting** | None, str,  | NoneClass, str,  |  | [optional] must be one of ["MR", "MRS", "MS", "MISS", "DR", "HR", "SR", ] 
**mobilePhoneNumber** | None, str,  | NoneClass, str,  |  | [optional] 
**phoneNumber** | None, str,  | NoneClass, str,  |  | [optional] 
**faxNumber** | None, str,  | NoneClass, str,  |  | [optional] 
**country** | [**Country**](Country.md) | [**Country**](Country.md) |  | [optional] 
**addressLine1** | None, str,  | NoneClass, str,  |  | [optional] 
**addressLine2** | None, str,  | NoneClass, str,  |  | [optional] 
**addressLine3** | None, str,  | NoneClass, str,  |  | [optional] 
**postalCode** | None, str,  | NoneClass, str,  |  | [optional] 
**city** | None, str,  | NoneClass, str,  |  | [optional] 
**state** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

