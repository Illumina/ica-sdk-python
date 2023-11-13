<a name="__pageTop"></a>
# icasdk.apis.tags.project_workflow_session_api.ProjectWorkflowSessionApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_session_configurations**](#get_workflow_session_configurations) | **get** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/configurations | Retrieve the configurations of a workflow session.
[**get_workflow_session_inputs**](#get_workflow_session_inputs) | **get** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/inputs | Retrieve the inputs of a workflow session.
[**get_workflow_sessions**](#get_workflow_sessions) | **get** /api/projects/{projectId}/workflowSessions | Retrieve the list of workflow sessions.

# **get_workflow_session_configurations**
<a name="get_workflow_session_configurations"></a>
> WorkflowSessionConfigurationList get_workflow_session_configurations(project_idworkflow_session_id)

Retrieve the configurations of a workflow session.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_workflow_session_api
from icasdk.model.problem import Problem
from icasdk.model.workflow_session_configuration_list import WorkflowSessionConfigurationList
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
    api_instance = project_workflow_session_api.ProjectWorkflowSessionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'workflowSessionId': "workflowSessionId_example",
    }
    try:
        # Retrieve the configurations of a workflow session.
        api_response = api_instance.get_workflow_session_configurations(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_session_configurations: %s\n" % e)
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
workflowSessionId | WorkflowSessionIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WorkflowSessionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_workflow_session_configurations.ApiResponseFor200) | The configurations of the workflow session are successfully retrieved.
default | [ApiResponseForDefault](#get_workflow_session_configurations.ApiResponseForDefault) | A problem occurred.

#### get_workflow_session_configurations.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkflowSessionConfigurationList**](../../models/WorkflowSessionConfigurationList.md) |  | 


#### get_workflow_session_configurations.ApiResponseForDefault
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

# **get_workflow_session_inputs**
<a name="get_workflow_session_inputs"></a>
> WorkflowSessionInputList get_workflow_session_inputs(project_idworkflow_session_id)

Retrieve the inputs of a workflow session.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_workflow_session_api
from icasdk.model.workflow_session_input_list import WorkflowSessionInputList
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
    api_instance = project_workflow_session_api.ProjectWorkflowSessionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'workflowSessionId': "workflowSessionId_example",
    }
    try:
        # Retrieve the inputs of a workflow session.
        api_response = api_instance.get_workflow_session_inputs(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_session_inputs: %s\n" % e)
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
workflowSessionId | WorkflowSessionIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# WorkflowSessionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_workflow_session_inputs.ApiResponseFor200) | The inputs of the workflow session are successfully retrieved.
default | [ApiResponseForDefault](#get_workflow_session_inputs.ApiResponseForDefault) | A problem occurred.

#### get_workflow_session_inputs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkflowSessionInputList**](../../models/WorkflowSessionInputList.md) |  | 


#### get_workflow_session_inputs.ApiResponseForDefault
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

# **get_workflow_sessions**
<a name="get_workflow_sessions"></a>
> WorkflowSessionPagedList get_workflow_sessions(project_id)

Retrieve the list of workflow sessions.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_workflow_session_api
from icasdk.model.problem import Problem
from icasdk.model.workflow_session_paged_list import WorkflowSessionPagedList
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
    api_instance = project_workflow_session_api.ProjectWorkflowSessionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    query_params = {
    }
    try:
        # Retrieve the list of workflow sessions.
        api_response = api_instance.get_workflow_sessions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_sessions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
    }
    query_params = {
        'reference': "reference_example",
        'userreference': "userreference_example",
        'status': "status_example",
        'usertag': "usertag_example",
        'technicaltag': "technicaltag_example",
        'pageOffset': "pageOffset_example",
        'pageToken': "pageToken_example",
        'pageSize': "pageSize_example",
        'sort': "sort_example",
    }
    try:
        # Retrieve the list of workflow sessions.
        api_response = api_instance.get_workflow_sessions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_sessions: %s\n" % e)
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
reference | ReferenceSchema | | optional
userreference | UserreferenceSchema | | optional
status | StatusSchema | | optional
usertag | UsertagSchema | | optional
technicaltag | TechnicaltagSchema | | optional
pageOffset | PageOffsetSchema | | optional
pageToken | PageTokenSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional


# ReferenceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserreferenceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UsertagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TechnicaltagSchema

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
200 | [ApiResponseFor200](#get_workflow_sessions.ApiResponseFor200) | The list of project workflow sessions is successfully retrieved.
default | [ApiResponseForDefault](#get_workflow_sessions.ApiResponseForDefault) | A problem occurred.

#### get_workflow_sessions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkflowSessionPagedList**](../../models/WorkflowSessionPagedList.md) |  | 


#### get_workflow_sessions.ApiResponseForDefault
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

