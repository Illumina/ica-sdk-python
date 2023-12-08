# icasdk.ProjectAnalysisApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_analysis**](ProjectAnalysisApi.md#abort_analysis) | **POST** /api/projects/{projectId}/analyses/{analysisId}:abort | Abort an analysis.
[**create_cwl_analysis**](ProjectAnalysisApi.md#create_cwl_analysis) | **POST** /api/projects/{projectId}/analysis:cwl | Create and start an analysis for a CWL pipeline.
[**create_nextflow_analysis**](ProjectAnalysisApi.md#create_nextflow_analysis) | **POST** /api/projects/{projectId}/analysis:nextflow | Create and start an analysis for a Nextflow pipeline.
[**get_analyses**](ProjectAnalysisApi.md#get_analyses) | **GET** /api/projects/{projectId}/analyses | Retrieve the list of analyses.
[**get_analysis**](ProjectAnalysisApi.md#get_analysis) | **GET** /api/projects/{projectId}/analyses/{analysisId} | Retrieve an analysis.
[**get_analysis_configurations**](ProjectAnalysisApi.md#get_analysis_configurations) | **GET** /api/projects/{projectId}/analyses/{analysisId}/configurations | Retrieve the configurations of an analysis.
[**get_analysis_inputs**](ProjectAnalysisApi.md#get_analysis_inputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/inputs | Retrieve the inputs of an analysis.
[**get_analysis_outputs**](ProjectAnalysisApi.md#get_analysis_outputs) | **GET** /api/projects/{projectId}/analyses/{analysisId}/outputs | Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.
[**get_analysis_steps**](ProjectAnalysisApi.md#get_analysis_steps) | **GET** /api/projects/{projectId}/analyses/{analysisId}/steps | Retrieve the individual steps of an analysis.
[**get_cwl_input_json**](ProjectAnalysisApi.md#get_cwl_input_json) | **GET** /api/projects/{projectId}/analyses/{analysisId}/cwl/inputJson | Retrieve the input json of a CWL analysis.
[**get_cwl_output_json**](ProjectAnalysisApi.md#get_cwl_output_json) | **GET** /api/projects/{projectId}/analyses/{analysisId}/cwl/outputJson | Retrieve the output json of a CWL analysis.
[**get_raw_analysis_output**](ProjectAnalysisApi.md#get_raw_analysis_output) | **GET** /api/projects/{projectId}/analyses/{analysisId}/rawOutput | Retrieve the raw output of an analysis.
[**update_analysis**](ProjectAnalysisApi.md#update_analysis) | **PUT** /api/projects/{projectId}/analyses/{analysisId} | Update an analysis.


# **abort_analysis**
> abort_analysis(project_id, analysis_id)

Abort an analysis.

Endpoint for aborting an analysis. The status of the analysis is not updated immediately, only when the abortion of the analysis has actually started.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to abort

    try:
        # Abort an analysis.
        api_instance.abort_analysis(project_id, analysis_id)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->abort_analysis: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to abort | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The analysis is successfully aborted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cwl_analysis**
> Analysis create_cwl_analysis(project_id, create_cwl_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a CWL pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis import Analysis
from icasdk.models.create_cwl_analysis import CreateCwlAnalysis
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_cwl_analysis = icasdk.CreateCwlAnalysis() # CreateCwlAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user. (optional)

    try:
        # Create and start an analysis for a CWL pipeline.
        api_response = api_instance.create_cwl_analysis(project_id, create_cwl_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_cwl_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_cwl_analysis: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_cwl_analysis** | [**CreateCwlAnalysis**](CreateCwlAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn&#39;t been used in the past 7 days for that specific API and by the specific user. | [optional] 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_analysis**
> Analysis create_nextflow_analysis(project_id, create_nextflow_analysis, idempotency_key=idempotency_key)

Create and start an analysis for a Nextflow pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis import Analysis
from icasdk.models.create_nextflow_analysis import CreateNextflowAnalysis
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    create_nextflow_analysis = icasdk.CreateNextflowAnalysis() # CreateNextflowAnalysis | The following options can be used for actionOnExist:<br /><ul><li>Overwrite (default): If a file with that name already exists, it is overwritten.</li><li>Rename: If a file with that name already exists, an incremental counter is appended to the file name.</li><li>Skip: If a file with that name already exists, the new file is not saved and the data is discarded.</li></ul>
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user. (optional)

    try:
        # Create and start an analysis for a Nextflow pipeline.
        api_response = api_instance.create_nextflow_analysis(project_id, create_nextflow_analysis, idempotency_key=idempotency_key)
        print("The response of ProjectAnalysisApi->create_nextflow_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->create_nextflow_analysis: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_nextflow_analysis** | [**CreateNextflowAnalysis**](CreateNextflowAnalysis.md)| The following options can be used for actionOnExist:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Overwrite (default): If a file with that name already exists, it is overwritten.&lt;/li&gt;&lt;li&gt;Rename: If a file with that name already exists, an incremental counter is appended to the file name.&lt;/li&gt;&lt;li&gt;Skip: If a file with that name already exists, the new file is not saved and the data is discarded.&lt;/li&gt;&lt;/ul&gt; | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn&#39;t been used in the past 7 days for that specific API and by the specific user. | [optional] 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The analysis is successfully created and scheduled. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analyses**
> AnalysisPagedList get_analyses(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve the list of analyses.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis_paged_list import AnalysisPagedList
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    reference = 'reference_example' # str | The reference to filter on. (optional)
    userreference = 'userreference_example' # str | The user-reference to filter on. (optional)
    status = 'status_example' # str | The status to filter on. (optional)
    usertag = 'usertag_example' # str | The user-tags to filter on. (optional)
    technicaltag = 'technicaltag_example' # str | The technical-tags to filter on. (optional)
    referencetag = 'referencetag_example' # str | The reference-data-tags to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\"  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  (optional)

    try:
        # Retrieve the list of analyses.
        api_response = api_instance.get_analyses(project_id, reference=reference, userreference=userreference, status=status, usertag=usertag, technicaltag=technicaltag, referencetag=referencetag, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectAnalysisApi->get_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analyses: %s\n" % e)
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
 **referencetag** | **str**| The reference-data-tags to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot;  The attributes for which sorting is supported: - reference - userReference - pipeline - status - startDate - endDate - summary  | [optional] 

### Return type

[**AnalysisPagedList**](AnalysisPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project analyses is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis**
> Analysis get_analysis(project_id, analysis_id)

Retrieve an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis import Analysis
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve

    try:
        # Retrieve an analysis.
        api_response = api_instance.get_analysis(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_configurations**
> ExecutionConfigurationList get_analysis_configurations(project_id, analysis_id)

Retrieve the configurations of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.execution_configuration_list import ExecutionConfigurationList
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the configuration for

    try:
        # Retrieve the configurations of an analysis.
        api_response = api_instance.get_analysis_configurations(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_configurations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the configuration for | 

### Return type

[**ExecutionConfigurationList**](ExecutionConfigurationList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configurations of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_inputs**
> AnalysisInputList get_analysis_inputs(project_id, analysis_id)

Retrieve the inputs of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis_input_list import AnalysisInputList
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the inputs for

    try:
        # Retrieve the inputs of an analysis.
        api_response = api_instance.get_analysis_inputs(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_inputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_inputs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the inputs for | 

### Return type

[**AnalysisInputList**](AnalysisInputList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The inputs of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_outputs**
> AnalysisOutputList get_analysis_outputs(project_id, analysis_id)

Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis_output_list import AnalysisOutputList
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the outputs for

    try:
        # Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.
        api_response = api_instance.get_analysis_outputs(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_outputs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_outputs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the outputs for | 

### Return type

[**AnalysisOutputList**](AnalysisOutputList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The outputs of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_analysis_steps**
> AnalysisStepList get_analysis_steps(project_id, analysis_id)

Retrieve the individual steps of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis_step_list import AnalysisStepList
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis to retrieve the individual steps for

    try:
        # Retrieve the individual steps of an analysis.
        api_response = api_instance.get_analysis_steps(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_analysis_steps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_analysis_steps: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis to retrieve the individual steps for | 

### Return type

[**AnalysisStepList**](AnalysisStepList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The individual steps of the analysis are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwl_input_json**
> CwlAnalysisInputJson get_cwl_input_json(project_id, analysis_id)

Retrieve the input json of a CWL analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.cwl_analysis_input_json import CwlAnalysisInputJson
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the CWL analysis for which to retrieve the input json

    try:
        # Retrieve the input json of a CWL analysis.
        api_response = api_instance.get_cwl_input_json(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_cwl_input_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_cwl_input_json: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the CWL analysis for which to retrieve the input json | 

### Return type

[**CwlAnalysisInputJson**](CwlAnalysisInputJson.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input json of the CWL analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cwl_output_json**
> CwlAnalysisOutputJson get_cwl_output_json(project_id, analysis_id)

Retrieve the output json of a CWL analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.cwl_analysis_output_json import CwlAnalysisOutputJson
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the CWL analysis for which to retrieve the output json

    try:
        # Retrieve the output json of a CWL analysis.
        api_response = api_instance.get_cwl_output_json(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_cwl_output_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_cwl_output_json: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the CWL analysis for which to retrieve the output json | 

### Return type

[**CwlAnalysisOutputJson**](CwlAnalysisOutputJson.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The output json of the CWL analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_analysis_output**
> AnalysisRawOutput get_raw_analysis_output(project_id, analysis_id)

Retrieve the raw output of an analysis.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis_raw_output import AnalysisRawOutput
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | The ID of the analysis for which to retrieve the raw output

    try:
        # Retrieve the raw output of an analysis.
        api_response = api_instance.get_raw_analysis_output(project_id, analysis_id)
        print("The response of ProjectAnalysisApi->get_raw_analysis_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->get_raw_analysis_output: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**| The ID of the analysis for which to retrieve the raw output | 

### Return type

[**AnalysisRawOutput**](AnalysisRawOutput.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raw output of the analysis is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis**
> Analysis update_analysis(project_id, analysis_id, analysis, if_match=if_match)

Update an analysis.

Attributes which can be updated:    - tags

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.analysis import Analysis
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
    api_instance = icasdk.ProjectAnalysisApi(api_client)
    project_id = 'project_id_example' # str | 
    analysis_id = 'analysis_id_example' # str | 
    analysis = icasdk.Analysis() # Analysis | 
    if_match = 'if_match_example' # str | Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client's most recent value of the 'ETag' response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. (optional)

    try:
        # Update an analysis.
        api_response = api_instance.update_analysis(project_id, analysis_id, analysis, if_match=if_match)
        print("The response of ProjectAnalysisApi->update_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAnalysisApi->update_analysis: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **analysis_id** | **str**|  | 
 **analysis** | [**Analysis**](Analysis.md)|  | 
 **if_match** | **str**| Optional header parameter to enable conflict exposure. If the client provides this header, then it must contains the client&#39;s most recent value of the &#39;ETag&#39; response header, and the server will respond with a 409 code if it detects a conflict. If the client does not provide this header, then the server will not do a conflict check, which means that as a client you can override the resource even when the server has a more recent version. | [optional] 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The analysis is successfully updated. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

