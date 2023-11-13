<a name="__pageTop"></a>
# icasdk.apis.tags.entitled_bundle_api.EntitledBundleApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_entitled_bundle**](#get_entitled_bundle) | **get** /api/entitledbundles/{entitledBundleId} | Retrieve an entitled bundle.
[**get_entitled_bundles**](#get_entitled_bundles) | **get** /api/entitledbundles | Retrieve a list of entitled bundles.

# **get_entitled_bundle**
<a name="get_entitled_bundle"></a>
> Bundle get_entitled_bundle(entitled_bundle_id)

Retrieve an entitled bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import entitled_bundle_api
from icasdk.model.problem import Problem
from icasdk.model.bundle import Bundle
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
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entitledBundleId': "entitledBundleId_example",
    }
    try:
        # Retrieve an entitled bundle.
        api_response = api_instance.get_entitled_bundle(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling EntitledBundleApi->get_entitled_bundle: %s\n" % e)
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
entitledBundleId | EntitledBundleIdSchema | | 

# EntitledBundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_entitled_bundle.ApiResponseFor200) | The entitled bundle is successfully retrieved.
default | [ApiResponseForDefault](#get_entitled_bundle.ApiResponseForDefault) | A problem occurred.

#### get_entitled_bundle.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**Bundle**](../../models/Bundle.md) |  | 


#### get_entitled_bundle.ApiResponseForDefault
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

# **get_entitled_bundles**
<a name="get_entitled_bundles"></a>
> BundlePagedList get_entitled_bundles()

Retrieve a list of entitled bundles.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import entitled_bundle_api
from icasdk.model.problem import Problem
from icasdk.model.bundle_paged_list import BundlePagedList
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
    api_instance = entitled_bundle_api.EntitledBundleApi(api_client)

    # example passing only optional values
    query_params = {
        'search': "search_example",
        'userTags': "userTags_example",
        'technicalTags': "technicalTags_example",
        'pageOffset': "pageOffset_example",
        'pageToken': "pageToken_example",
        'pageSize': "pageSize_example",
        'sort': "sort_example",
    }
    try:
        # Retrieve a list of entitled bundles.
        api_response = api_instance.get_entitled_bundles(
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling EntitledBundleApi->get_entitled_bundles: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
search | SearchSchema | | optional
userTags | UserTagsSchema | | optional
technicalTags | TechnicalTagsSchema | | optional
pageOffset | PageOffsetSchema | | optional
pageToken | PageTokenSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional


# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserTagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TechnicalTagsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_entitled_bundles.ApiResponseFor200) | The list of entitled bundles is successfully retrieved.
default | [ApiResponseForDefault](#get_entitled_bundles.ApiResponseForDefault) | A problem occurred.

#### get_entitled_bundles.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**BundlePagedList**](../../models/BundlePagedList.md) |  | 


#### get_entitled_bundles.ApiResponseForDefault
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

