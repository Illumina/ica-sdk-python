# icasdk.model.project_data_update_batch_item_paged_list.ProjectDataUpdateBatchItemPagedList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[items](#items)** | list, tuple,  | tuple,  |  | 
**nextPageToken** | None, str,  | NoneClass, str,  | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remainingRecords** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The number of records remaining (used in cursor based pagination) | [optional] value must be a 64 bit integer
**totalItemCount** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | The total number of records matching the search criteria (used in offset based pagination) | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProjectDataUpdateBatchItem**](ProjectDataUpdateBatchItem.md) | [**ProjectDataUpdateBatchItem**](ProjectDataUpdateBatchItem.md) | [**ProjectDataUpdateBatchItem**](ProjectDataUpdateBatchItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

