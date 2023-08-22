# icasdk.model.find_project_samples.FindProjectSamples

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[dateConditions](#dateConditions)** | list, tuple,  | tuple,  | Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field. | 
**[numberConditions](#numberConditions)** | list, tuple,  | tuple,  | Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field. | 
**[booleanConditions](#booleanConditions)** | list, tuple,  | tuple,  | Adds a condition on a boolean field. | 
**[conditions](#conditions)** | list, tuple,  | tuple,  | Adds a condition on a string field. | 
**fullTextSearchString** | None, str,  | NoneClass, str,  | Adds a fuzzy matching condition for the text on all string fields of the sample i.e. on both the fixed fields (name, description) as any metadata text field. | [optional] 
**includeDeleted** | None, bool,  | NoneClass, BoolClass,  | Indicates whether deleted samples should be included. | [optional] if omitted the server will use the default value of False
**[userTags](#userTags)** | list, tuple, None,  | tuple, NoneClass,  | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | [optional] 
**userTagMatchMode** | None, str,  | NoneClass, str,  | How the usertags are filtered. | [optional] must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 
**[runInputTags](#runInputTags)** | list, tuple, None,  | tuple, NoneClass,  | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | [optional] 
**runInputTagMatchMode** | None, str,  | NoneClass, str,  | How the runInputTags are filtered. | [optional] must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 
**[connectorTags](#connectorTags)** | list, tuple, None,  | tuple, NoneClass,  | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | [optional] 
**connectorTagMatchMode** | None, str,  | NoneClass, str,  | How the connectorTags are filtered. | [optional] must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 
**[techTags](#techTags)** | list, tuple, None,  | tuple, NoneClass,  | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | [optional] 
**techTagMatchMode** | None, str,  | NoneClass, str,  | How the technicalTags are filtered. | [optional] must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 
**[instrumentRunIds](#instrumentRunIds)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Adds a condition on a string field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Adds a condition on a string field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FindSampleCondition**](FindSampleCondition.md) | [**FindSampleCondition**](FindSampleCondition.md) | [**FindSampleCondition**](FindSampleCondition.md) |  | 

# dateConditions

Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FindSampleDateCondition**](FindSampleDateCondition.md) | [**FindSampleDateCondition**](FindSampleDateCondition.md) | [**FindSampleDateCondition**](FindSampleDateCondition.md) |  | 

# numberConditions

Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FindSampleNumberCondition**](FindSampleNumberCondition.md) | [**FindSampleNumberCondition**](FindSampleNumberCondition.md) | [**FindSampleNumberCondition**](FindSampleNumberCondition.md) |  | 

# booleanConditions

Adds a condition on a boolean field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Adds a condition on a boolean field. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FindSampleBooleanCondition**](FindSampleBooleanCondition.md) | [**FindSampleBooleanCondition**](FindSampleBooleanCondition.md) | [**FindSampleBooleanCondition**](FindSampleBooleanCondition.md) |  | 

# userTags

The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done. | 

# runInputTags

The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done. | 

# connectorTags

The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done. | 

# techTags

The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  | The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done. | 

# instrumentRunIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

