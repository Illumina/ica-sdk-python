# icasdk.ProjectWorkflowSessionApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_session_configurations**](ProjectWorkflowSessionApi.md#get_workflow_session_configurations) | **GET** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/configurations | Retrieve the configurations of a workflow session.
[**get_workflow_session_inputs**](ProjectWorkflowSessionApi.md#get_workflow_session_inputs) | **GET** /api/projects/{projectId}/workflowSessions/{workflowSessionId}/inputs | Retrieve the inputs of a workflow session.
[**get_workflow_sessions**](ProjectWorkflowSessionApi.md#get_workflow_sessions) | **GET** /api/projects/{projectId}/workflowSessions | Retrieve the list of workflow sessions.


# **get_workflow_session_configurations**
> WorkflowSessionConfigurationList get_workflow_session_configurations(project_id, workflow_session_id)

Retrieve the configurations of a workflow session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.workflow_session_configuration_list import WorkflowSessionConfigurationList
from icasdk.rest import ApiException
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

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icasdk.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    workflow_session_id = 'workflow_session_id_example' # str | The ID of the workflow session to retrieve the configuration for

    try:
        # Retrieve the configurations of a workflow session.
        api_response = api_instance.get_workflow_session_configurations(project_id, workflow_session_id)
        print("The response of ProjectWorkflowSessionApi->get_workflow_session_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_session_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workflow_session_id** | **str**| The ID of the workflow session to retrieve the configuration for | 

### Return type

[**WorkflowSessionConfigurationList**](WorkflowSessionConfigurationList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configurations of the workflow session are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_session_inputs**
> WorkflowSessionInputList get_workflow_session_inputs(project_id, workflow_session_id)

Retrieve the inputs of a workflow session.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.workflow_session_input_list import WorkflowSessionInputList
from icasdk.rest import ApiException
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

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icasdk.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    workflow_session_id = 'workflow_session_id_example' # str | The ID of the workflow session to retrieve the inputs for

    try:
        # Retrieve the inputs of a workflow session.
        api_response = api_instance.get_workflow_session_inputs(project_id, workflow_session_id)
        print("The response of ProjectWorkflowSessionApi->get_workflow_session_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_session_inputs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **workflow_session_id** | **str**| The ID of the workflow session to retrieve the inputs for | 

### Return type

[**WorkflowSessionInputList**](WorkflowSessionInputList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inputs of the workflow session are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_sessions**
> WorkflowSessionPagedList get_workflow_sessions(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve the list of workflow sessions.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.workflow_session_paged_list import WorkflowSessionPagedList
from icasdk.rest import ApiException
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

# Configure Bearer authorization (JWT): JwtAuth
configuration = icasdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = icasdk.ProjectWorkflowSessionApi(api_client)
    project_id = 'project_id_example' # str | 
    reference = 'reference_example' # str | The reference to filter on. (optional)
    userreference = 'userreference_example' # str | The user-reference to filter on. (optional)
    status = 'status_example' # str | The status to filter on. (optional)
    usertag = 'usertag_example' # str | The user-tags to filter on. (optional)
    technicaltag = 'technicaltag_example' # str | The technical-tags to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - workflow  (optional)

    try:
        # Retrieve the list of workflow sessions.
        api_response = api_instance.get_workflow_sessions(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectWorkflowSessionApi->get_workflow_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkflowSessionApi->get_workflow_sessions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **reference** | **str**| The reference to filter on. | [optional] 
 **userreference** | **str**| The user-reference to filter on. | [optional] 
 **status** | **str**| The status to filter on. | [optional] 
 **usertag** | **str**| The user-tags to filter on. | [optional] 
 **technicaltag** | **str**| The technical-tags to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - workflow  | [optional] 

### Return type

[**WorkflowSessionPagedList**](WorkflowSessionPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project workflow sessions is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
