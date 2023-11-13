# icasdk.model.project_data_copy_batch_item.ProjectDataCopyBatchItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request** | [**ProjectDataCopyBatchItemRequest**](ProjectDataCopyBatchItemRequest.md) | [**ProjectDataCopyBatchItemRequest**](ProjectDataCopyBatchItemRequest.md) |  | 
**processing** | [**ProjectDataCopyBatchItemProcessing**](ProjectDataCopyBatchItemProcessing.md) | [**ProjectDataCopyBatchItemProcessing**](ProjectDataCopyBatchItemProcessing.md) |  | 
**id** | str, uuid.UUID,  | str,  |  | value must be a uuid
**createdProjectData** | [**ProjectData**](ProjectData.md) | [**ProjectData**](ProjectData.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

