# icasdk.model.base_connection.BaseConnection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**databaseName** | str,  | str,  | Specifies the database name bound to the project specified | 
**roleName** | str,  | str,  | Specifies the role name bound to the project specified | 
**dnsName** | str,  | str,  | snowflake dns name. Usually something like &#x27;&lt;&lt;account&gt;&gt;.snowflakecomputing.com&#x27; | 
**accessToken** | str,  | str,  | Specifies the OAuth token to use for authentication | 
**schemaName** | str,  | str,  | Specifies the schema name bound to the project specified | 
**authenticator** | str,  | str,  | Specifies the supported snowflake authenticator to use. Currently &#x27;oauth&#x27; only is supported | 
**warehouseName** | str,  | str,  | Specifies the warehouse name bound to the project specified | 
**userPrincipalName** | str,  | str,  | Specifies the user principal name. This is required for some snowflake client (snowSQL for instance) | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

