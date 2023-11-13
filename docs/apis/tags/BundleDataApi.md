<a name="__pageTop"></a>
# icasdk.apis.tags.bundle_data_api.BundleDataApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bundle_data**](#get_bundle_data) | **get** /api/bundles/{bundleId}/data | Retrieve the list of bundle data.
[**link_data_to_bundle**](#link_data_to_bundle) | **post** /api/bundles/{bundleId}/data/{dataId} | Link data to this bundle.
[**unlink_data_from_bundle**](#unlink_data_from_bundle) | **delete** /api/bundles/{bundleId}/data/{dataId} | Unlink data from this bundle.

# **get_bundle_data**
<a name="get_bundle_data"></a>
> BundleDataPagedList get_bundle_data(bundle_id)

Retrieve the list of bundle data.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_data_api
from icasdk.model.bundle_data_paged_list import BundleDataPagedList
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
    api_instance = bundle_data_api.BundleDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
    }
    query_params = {
    }
    try:
        # Retrieve the list of bundle data.
        api_response = api_instance.get_bundle_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling BundleDataApi->get_bundle_data: %s\n" % e)

    # example passing only optional values
    path_params = {
        'bundleId': "bundleId_example",
    }
    query_params = {
        'fullText': "fullText_example",
        'id': "id_example",
        'filename': "filename_example",
        'filenameMatchMode': "EXACT",
        'filePath': "filePath_example",
        'filePathMatchMode': "STARTS_WITH_CASE_INSENSITIVE",
        'status': "PARTIAL",
        'formatId': "formatId_example",
        'formatCode': "formatCode_example",
        'type': "FILE",
        'parentFolderId': "parentFolderId_example",
        'parentFolderPath': "parentFolderPath_example",
        'creationDateAfter': "creationDateAfter_example",
        'creationDateBefore': "creationDateBefore_example",
        'statusDateAfter': "statusDateAfter_example",
        'statusDateBefore': "statusDateBefore_example",
        'userTag': "userTag_example",
        'userTagMatchMode': "EXACT",
        'runInputTag': "runInputTag_example",
        'runInputTagMatchMode': "EXACT",
        'runOutputTag': "runOutputTag_example",
        'runOutputTagMatchMode': "EXACT",
        'connectorTag': "connectorTag_example",
        'connectorTagMatchMode': "EXACT",
        'technicalTag': "technicalTag_example",
        'technicalTagMatchMode': "EXACT",
        'notInRun': "notInRun_example",
        'notLinkedToSample': "notLinkedToSample_example",
        'instrumentRunId': [
        "instrumentRunId_example"
    ],
        'pageOffset': "pageOffset_example",
        'pageToken': "pageToken_example",
        'pageSize': "pageSize_example",
        'sort': "sort_example",
    }
    try:
        # Retrieve the list of bundle data.
        api_response = api_instance.get_bundle_data(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling BundleDataApi->get_bundle_data: %s\n" % e)
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
fullText | FullTextSchema | | optional
id | IdSchema | | optional
filename | FilenameSchema | | optional
filenameMatchMode | FilenameMatchModeSchema | | optional
filePath | FilePathSchema | | optional
filePathMatchMode | FilePathMatchModeSchema | | optional
status | StatusSchema | | optional
formatId | FormatIdSchema | | optional
formatCode | FormatCodeSchema | | optional
type | TypeSchema | | optional
parentFolderId | ParentFolderIdSchema | | optional
parentFolderPath | ParentFolderPathSchema | | optional
creationDateAfter | CreationDateAfterSchema | | optional
creationDateBefore | CreationDateBeforeSchema | | optional
statusDateAfter | StatusDateAfterSchema | | optional
statusDateBefore | StatusDateBeforeSchema | | optional
userTag | UserTagSchema | | optional
userTagMatchMode | UserTagMatchModeSchema | | optional
runInputTag | RunInputTagSchema | | optional
runInputTagMatchMode | RunInputTagMatchModeSchema | | optional
runOutputTag | RunOutputTagSchema | | optional
runOutputTagMatchMode | RunOutputTagMatchModeSchema | | optional
connectorTag | ConnectorTagSchema | | optional
connectorTagMatchMode | ConnectorTagMatchModeSchema | | optional
technicalTag | TechnicalTagSchema | | optional
technicalTagMatchMode | TechnicalTagMatchModeSchema | | optional
notInRun | NotInRunSchema | | optional
notLinkedToSample | NotLinkedToSampleSchema | | optional
instrumentRunId | InstrumentRunIdSchema | | optional
pageOffset | PageOffsetSchema | | optional
pageToken | PageTokenSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional


# FullTextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilenameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilenameMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 

# FilePathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilePathMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["STARTS_WITH_CASE_INSENSITIVE", "FULL_CASE_INSENSITIVE", ] if omitted the server will use the default value of "STARTS_WITH_CASE_INSENSITIVE"

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["PARTIAL", "AVAILABLE", "ARCHIVING", "ARCHIVED", "UNARCHIVING", "DELETING", ] 

# FormatIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FormatCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["FILE", "FOLDER", ] 

# ParentFolderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ParentFolderPathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreationDateAfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CreationDateBeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusDateAfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusDateBeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserTagMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 

# RunInputTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RunInputTagMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 

# RunOutputTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RunOutputTagMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 

# ConnectorTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConnectorTagMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 

# TechnicalTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TechnicalTagMatchModeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EXACT", "EXCLUDE", "FUZZY", ] 

# NotInRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NotLinkedToSampleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# InstrumentRunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

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
bundleId | BundleIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bundle_data.ApiResponseFor200) | The list of bundle data is successfully retrieved.
default | [ApiResponseForDefault](#get_bundle_data.ApiResponseForDefault) | A problem occurred.

#### get_bundle_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**BundleDataPagedList**](../../models/BundleDataPagedList.md) |  | 


#### get_bundle_data.ApiResponseForDefault
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

# **link_data_to_bundle**
<a name="link_data_to_bundle"></a>
> link_data_to_bundle(bundle_iddata_id)

Link data to this bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_data_api
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
    api_instance = bundle_data_api.BundleDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
        'dataId': "dataId_example",
    }
    try:
        # Link data to this bundle.
        api_response = api_instance.link_data_to_bundle(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling BundleDataApi->link_data_to_bundle: %s\n" % e)
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
bundleId | BundleIdSchema | | 
dataId | DataIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DataIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#link_data_to_bundle.ApiResponseFor204) | The data is successfully linked to this bundle.
default | [ApiResponseForDefault](#link_data_to_bundle.ApiResponseForDefault) | A problem occurred.

#### link_data_to_bundle.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### link_data_to_bundle.ApiResponseForDefault
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

# **unlink_data_from_bundle**
<a name="unlink_data_from_bundle"></a>
> unlink_data_from_bundle(bundle_iddata_id)

Unlink data from this bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_data_api
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
    api_instance = bundle_data_api.BundleDataApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
        'dataId': "dataId_example",
    }
    try:
        # Unlink data from this bundle.
        api_response = api_instance.unlink_data_from_bundle(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling BundleDataApi->unlink_data_from_bundle: %s\n" % e)
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
bundleId | BundleIdSchema | | 
dataId | DataIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DataIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#unlink_data_from_bundle.ApiResponseFor204) | The data is successfully unlinked from this bundle.
default | [ApiResponseForDefault](#unlink_data_from_bundle.ApiResponseForDefault) | A problem occurred.

#### unlink_data_from_bundle.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### unlink_data_from_bundle.ApiResponseForDefault
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

