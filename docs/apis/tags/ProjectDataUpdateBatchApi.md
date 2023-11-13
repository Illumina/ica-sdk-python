<a name="__pageTop"></a>
# icasdk.apis.tags.project_data_update_batch_api.ProjectDataUpdateBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_data_update_batch**](#create_project_data_update_batch) | **post** /api/projects/{projectId}/dataUpdateBatch | Create a project data update batch.
[**get_project_data_update_batch**](#get_project_data_update_batch) | **get** /api/projects/{projectId}/dataUpdateBatch/{batchId} | Retrieve a project data update batch.
[**get_project_data_update_batch_item**](#get_project_data_update_batch_item) | **get** /api/projects/{projectId}/dataUpdateBatch/{batchId}/items/{itemId} | Retrieve a project data update batch item.
[**get_project_data_update_batch_items**](#get_project_data_update_batch_items) | **get** /api/projects/{projectId}/dataUpdateBatch/{batchId}/items | Retrieve a list of project data update batch items.

# **create_project_data_update_batch**
<a name="create_project_data_update_batch"></a>
> ProjectDataUpdateBatch create_project_data_update_batch(project_idcreate_project_data_update_batch)

Create a project data update batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_data_update_batch_api
from icasdk.model.problem import Problem
from icasdk.model.project_data_update_batch import ProjectDataUpdateBatch
from icasdk.model.create_project_data_update_batch import CreateProjectDataUpdateBatch
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_data_update_batch_api.ProjectDataUpdateBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    body = CreateProjectDataUpdateBatch(
        data_update_groups=[
            DataUpdateGroup(
                data_ids=[
                    "data_ids_example"
                ],
                user_tags=TagUpdate(
,
,
                ),
,
            )
        ],
    )
    try:
        # Create a project data update batch.
        api_response = api_instance.create_project_data_update_batch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataUpdateBatchApi->create_project_data_update_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndIlluminaV3json, SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.illumina.v3+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateProjectDataUpdateBatch**](../../models/CreateProjectDataUpdateBatch.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateProjectDataUpdateBatch**](../../models/CreateProjectDataUpdateBatch.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_project_data_update_batch.ApiResponseFor201) | The project data update batch is successfully created.
default | [ApiResponseForDefault](#create_project_data_update_batch.ApiResponseForDefault) | A problem occurred.

#### create_project_data_update_batch.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectDataUpdateBatch**](../../models/ProjectDataUpdateBatch.md) |  | 


#### create_project_data_update_batch.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationProblemjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Problem**](../../models/Problem.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [JwtAuth](../../../README.md#JwtAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_data_update_batch**
<a name="get_project_data_update_batch"></a>
> ProjectDataUpdateBatch get_project_data_update_batch(project_idbatch_id)

Retrieve a project data update batch.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_data_update_batch_api
from icasdk.model.problem import Problem
from icasdk.model.project_data_update_batch import ProjectDataUpdateBatch
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_data_update_batch_api.ProjectDataUpdateBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
    }
    try:
        # Retrieve a project data update batch.
        api_response = api_instance.get_project_data_update_batch(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataUpdateBatchApi->get_project_data_update_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
batchId | BatchIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_data_update_batch.ApiResponseFor200) | The project data update batch is successfully retrieved.
default | [ApiResponseForDefault](#get_project_data_update_batch.ApiResponseForDefault) | A problem occurred.

#### get_project_data_update_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectDataUpdateBatch**](../../models/ProjectDataUpdateBatch.md) |  | 


#### get_project_data_update_batch.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationProblemjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Problem**](../../models/Problem.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [JwtAuth](../../../README.md#JwtAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_data_update_batch_item**
<a name="get_project_data_update_batch_item"></a>
> ProjectDataUpdateBatchItem get_project_data_update_batch_item(project_idbatch_iditem_id)

Retrieve a project data update batch item.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_data_update_batch_api
from icasdk.model.project_data_update_batch_item import ProjectDataUpdateBatchItem
from icasdk.model.problem import Problem
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_data_update_batch_api.ProjectDataUpdateBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
        'itemId': "itemId_example",
    }
    try:
        # Retrieve a project data update batch item.
        api_response = api_instance.get_project_data_update_batch_item(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataUpdateBatchApi->get_project_data_update_batch_item: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
batchId | BatchIdSchema | | 
itemId | ItemIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# ItemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_data_update_batch_item.ApiResponseFor200) | The project data update batch item is successfully retrieved.
default | [ApiResponseForDefault](#get_project_data_update_batch_item.ApiResponseForDefault) | A problem occurred.

#### get_project_data_update_batch_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectDataUpdateBatchItem**](../../models/ProjectDataUpdateBatchItem.md) |  | 


#### get_project_data_update_batch_item.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationProblemjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Problem**](../../models/Problem.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [JwtAuth](../../../README.md#JwtAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_data_update_batch_items**
<a name="get_project_data_update_batch_items"></a>
> ProjectDataUpdateBatchItemPagedList get_project_data_update_batch_items(project_idbatch_id)

Retrieve a list of project data update batch items.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_data_update_batch_api
from icasdk.model.problem import Problem
from icasdk.model.project_data_update_batch_item_paged_list import ProjectDataUpdateBatchItemPagedList
from pprint import pprint
# Defining the host is optional and defaults to /ica/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(
    host = "/ica/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_data_update_batch_api.ProjectDataUpdateBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
    }
    query_params = {
    }
    try:
        # Retrieve a list of project data update batch items.
        api_response = api_instance.get_project_data_update_batch_items(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataUpdateBatchApi->get_project_data_update_batch_items: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
    }
    query_params = {
        'status': [
        "INITIALISED"
    ],
        'pageOffset': "pageOffset_example",
        'pageToken': "pageToken_example",
        'pageSize': "pageSize_example",
        'sort': "sort_example",
    }
    try:
        # Retrieve a list of project data update batch items.
        api_response = api_instance.get_project_data_update_batch_items(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectDataUpdateBatchApi->get_project_data_update_batch_items: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
status | StatusSchema | | optional
pageOffset | PageOffsetSchema | | optional
pageToken | PageTokenSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional


# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["INITIALISED", "WAITING_RESOURCES", "UPDATING", "UPDATED", "PARTIALLY_UPDATED", "FAILED", ] 

# PageOffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
batchId | BatchIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_data_update_batch_items.ApiResponseFor200) | The list of project data update batch items is successfully retrieved.
default | [ApiResponseForDefault](#get_project_data_update_batch_items.ApiResponseForDefault) | A problem occurred.

#### get_project_data_update_batch_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectDataUpdateBatchItemPagedList**](../../models/ProjectDataUpdateBatchItemPagedList.md) |  | 


#### get_project_data_update_batch_items.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationProblemjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationProblemjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Problem**](../../models/Problem.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth), [JwtAuth](../../../README.md#JwtAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

