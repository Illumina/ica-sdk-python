<a name="__pageTop"></a>
# icasdk.apis.tags.bundle_tool_api.BundleToolApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bundle_tools**](#get_bundle_tools) | **get** /api/bundles/{bundleId}/tools | Retrieve a list of bundle tools.
[**get_tools_eligible_for_linking_to_bundle**](#get_tools_eligible_for_linking_to_bundle) | **get** /api/bundles/{bundleId}/tools/eligibleForLinking | Retrieve a list of tools eligible for linking to the bundle.
[**link_tool_to_bundle**](#link_tool_to_bundle) | **post** /api/bundles/{bundleId}/tools/{toolId} | Link a tool to a bundle
[**unlink_tool_from_bundle**](#unlink_tool_from_bundle) | **delete** /api/bundles/{bundleId}/tools/{toolId} | Unlink a tool from this bundle.

# **get_bundle_tools**
<a name="get_bundle_tools"></a>
> BundleToolsList get_bundle_tools(bundle_id)

Retrieve a list of bundle tools.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_tool_api
from icasdk.model.bundle_tools_list import BundleToolsList
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
    }
    try:
        # Retrieve a list of bundle tools.
        api_response = api_instance.get_bundle_tools(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling BundleToolApi->get_bundle_tools: %s\n" % e)
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

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bundle_tools.ApiResponseFor200) | The list of bundle tools is successfully retrieved.
default | [ApiResponseForDefault](#get_bundle_tools.ApiResponseForDefault) | A problem occurred.

#### get_bundle_tools.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**BundleToolsList**](../../models/BundleToolsList.md) |  | 


#### get_bundle_tools.ApiResponseForDefault
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

# **get_tools_eligible_for_linking_to_bundle**
<a name="get_tools_eligible_for_linking_to_bundle"></a>
> CwlToolDefinitionList get_tools_eligible_for_linking_to_bundle(bundle_id)

Retrieve a list of tools eligible for linking to the bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_tool_api
from icasdk.model.cwl_tool_definition_list import CwlToolDefinitionList
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
    }
    try:
        # Retrieve a list of tools eligible for linking to the bundle.
        api_response = api_instance.get_tools_eligible_for_linking_to_bundle(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling BundleToolApi->get_tools_eligible_for_linking_to_bundle: %s\n" % e)
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

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_tools_eligible_for_linking_to_bundle.ApiResponseFor200) | The list of tools is successfully retrieved.
default | [ApiResponseForDefault](#get_tools_eligible_for_linking_to_bundle.ApiResponseForDefault) | A problem occurred.

#### get_tools_eligible_for_linking_to_bundle.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**CwlToolDefinitionList**](../../models/CwlToolDefinitionList.md) |  | 


#### get_tools_eligible_for_linking_to_bundle.ApiResponseForDefault
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

# **link_tool_to_bundle**
<a name="link_tool_to_bundle"></a>
> link_tool_to_bundle(bundle_idtool_id)

Link a tool to a bundle

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_tool_api
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
        'toolId': "toolId_example",
    }
    try:
        # Link a tool to a bundle
        api_response = api_instance.link_tool_to_bundle(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling BundleToolApi->link_tool_to_bundle: %s\n" % e)
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
toolId | ToolIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#link_tool_to_bundle.ApiResponseFor204) | The tool is successfully linked to the bundle.
default | [ApiResponseForDefault](#link_tool_to_bundle.ApiResponseForDefault) | A problem occurred.

#### link_tool_to_bundle.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### link_tool_to_bundle.ApiResponseForDefault
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

# **unlink_tool_from_bundle**
<a name="unlink_tool_from_bundle"></a>
> unlink_tool_from_bundle(bundle_idtool_id)

Unlink a tool from this bundle.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import bundle_tool_api
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
    api_instance = bundle_tool_api.BundleToolApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundleId': "bundleId_example",
        'toolId': "toolId_example",
    }
    try:
        # Unlink a tool from this bundle.
        api_response = api_instance.unlink_tool_from_bundle(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling BundleToolApi->unlink_tool_from_bundle: %s\n" % e)
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
toolId | ToolIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToolIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#unlink_tool_from_bundle.ApiResponseFor204) | The tool is successfully unlinked from this bundle.
default | [ApiResponseForDefault](#unlink_tool_from_bundle.ApiResponseForDefault) | A problem occurred.

#### unlink_tool_from_bundle.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### unlink_tool_from_bundle.ApiResponseForDefault
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

