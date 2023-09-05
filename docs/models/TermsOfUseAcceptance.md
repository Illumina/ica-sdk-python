# icasdk.model.terms_of_use_acceptance.TermsOfUseAcceptance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accepted** | bool,  | BoolClass,  | Are the terms of use accepted | 
**firstAcceptanceDate** | str, datetime,  | str,  | Date of the first time the terms of use were accepted. | value must conform to RFC-3339 date-time
**versionTermsOfUseFirstAccept** | str,  | str,  | Version of the first accepted Terms of Use. | 
**lastAcceptanceDate** | str, datetime,  | str,  | Date of the last time the terms of use were accepted. | [optional] value must conform to RFC-3339 date-time
**versionTermsOfUseLastAccept** | str,  | str,  | Version of the last accepted Terms of Use. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

