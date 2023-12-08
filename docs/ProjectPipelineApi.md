# icasdk.ProjectPipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cwl_pipeline**](ProjectPipelineApi.md#create_cwl_pipeline) | **POST** /api/projects/{projectId}/pipelines:createCwlPipeline | Create a CWL pipeline within a project.
[**create_nextflow_pipeline**](ProjectPipelineApi.md#create_nextflow_pipeline) | **POST** /api/projects/{projectId}/pipelines:createNextflowPipeline | Create a Nextflow pipeline within a project.
[**create_pipeline_file**](ProjectPipelineApi.md#create_pipeline_file) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}/files | Create a file for a pipeline.
[**delete_pipeline_file**](ProjectPipelineApi.md#delete_pipeline_file) | **DELETE** /api/projects/{projectId}/pipelines/{pipelineId}/files/{fileId} | Delete a file for a pipeline.
[**download_pipeline_file_content1**](ProjectPipelineApi.md#download_pipeline_file_content1) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/files/{fileId}/content | Download the contents of a pipeline file.
[**get_pipeline_files1**](ProjectPipelineApi.md#get_pipeline_files1) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/files | Retrieve files for a project pipeline.
[**get_project_pipeline**](ProjectPipelineApi.md#get_project_pipeline) | **GET** /api/projects/{projectId}/pipelines/{pipelineId} | Retrieve a project pipeline.
[**get_project_pipeline_configuration_parameters**](ProjectPipelineApi.md#get_project_pipeline_configuration_parameters) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/configurationParameters | Retrieve configuration parameters for a project pipeline.
[**get_project_pipeline_html_documentation**](ProjectPipelineApi.md#get_project_pipeline_html_documentation) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/documentation/HTML | Retrieve HTML documentation for a project pipeline.
[**get_project_pipeline_input_parameters**](ProjectPipelineApi.md#get_project_pipeline_input_parameters) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/inputParameters | Retrieve input parameters for a project pipeline.
[**get_project_pipeline_reference_sets**](ProjectPipelineApi.md#get_project_pipeline_reference_sets) | **GET** /api/projects/{projectId}/pipelines/{pipelineId}/referenceSets | Retrieve the reference sets of a project pipeline.
[**get_project_pipelines**](ProjectPipelineApi.md#get_project_pipelines) | **GET** /api/projects/{projectId}/pipelines | Retrieve a list of project pipelines.
[**link_pipeline_to_project**](ProjectPipelineApi.md#link_pipeline_to_project) | **POST** /api/projects/{projectId}/pipelines/{pipelineId} | Link a pipeline to a project.
[**release_pipeline**](ProjectPipelineApi.md#release_pipeline) | **POST** /api/projects/{projectId}/pipelines/{pipelineId}:release | Release a pipeline.
[**unlink_pipeline_from_project**](ProjectPipelineApi.md#unlink_pipeline_from_project) | **DELETE** /api/projects/{projectId}/pipelines/{pipelineId} | Unlink a pipeline from a project.
[**update_pipeline_file**](ProjectPipelineApi.md#update_pipeline_file) | **PUT** /api/projects/{projectId}/pipelines/{pipelineId}/files/{fileId}/content | Update the contents of a file for a pipeline.


# **create_cwl_pipeline**
> ProjectPipeline create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation)

Create a CWL pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.links import Links
from icasdk.models.project_pipeline import ProjectPipeline
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the CWL pipeline
    description = 'description_example' # str | The description of the CWL pipeline
    workflow_cwl_file = None # bytearray | The CWL workflow file.
    parameters_xml_file = None # bytearray | 
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    tool_cwl_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = icasdk.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[str] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)

    try:
        # Create a CWL pipeline within a project.
        api_response = api_instance.create_cwl_pipeline(project_id, code, description, workflow_cwl_file, parameters_xml_file, analysis_storage_id, tool_cwl_files=tool_cwl_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation)
        print("The response of ProjectPipelineApi->create_cwl_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the CWL pipeline | 
 **description** | **str**| The description of the CWL pipeline | 
 **workflow_cwl_file** | **bytearray**| The CWL workflow file. | 
 **parameters_xml_file** | **bytearray**|  | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **tool_cwl_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[str]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The CWL pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nextflow_pipeline**
> ProjectPipeline create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation)

Create a Nextflow pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.links import Links
from icasdk.models.project_pipeline import ProjectPipeline
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    code = 'code_example' # str | The code of the pipeline
    description = 'description_example' # str | The description of the pipeline
    main_nextflow_file = None # bytearray | The main Nextflow file.
    parameters_xml_file = None # bytearray | 
    analysis_storage_id = 'analysis_storage_id_example' # str | The id of the storage to use for the pipeline.
    pipeline_language_version_id = 'pipeline_language_version_id_example' # str | The id of the Nextflow version to use for the pipeline. (optional)
    nextflow_config_file = None # bytearray | The Nextflow config file. (optional)
    other_nextflow_files = None # List[bytearray] |  (optional)
    metadata_model_file = None # bytearray | The metadata model json file(contents can be retrieved from the controlplane). (optional)
    links = icasdk.Links() # Links |  (optional)
    version_comment = 'version_comment_example' # str |  (optional)
    categories = ['categories_example'] # List[str] |  (optional)
    html_documentation = 'html_documentation_example' # str |  (optional)

    try:
        # Create a Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_pipeline(project_id, code, description, main_nextflow_file, parameters_xml_file, analysis_storage_id, pipeline_language_version_id=pipeline_language_version_id, nextflow_config_file=nextflow_config_file, other_nextflow_files=other_nextflow_files, metadata_model_file=metadata_model_file, links=links, version_comment=version_comment, categories=categories, html_documentation=html_documentation)
        print("The response of ProjectPipelineApi->create_nextflow_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **code** | **str**| The code of the pipeline | 
 **description** | **str**| The description of the pipeline | 
 **main_nextflow_file** | **bytearray**| The main Nextflow file. | 
 **parameters_xml_file** | **bytearray**|  | 
 **analysis_storage_id** | **str**| The id of the storage to use for the pipeline. | 
 **pipeline_language_version_id** | **str**| The id of the Nextflow version to use for the pipeline. | [optional] 
 **nextflow_config_file** | **bytearray**| The Nextflow config file. | [optional] 
 **other_nextflow_files** | **List[bytearray]**|  | [optional] 
 **metadata_model_file** | **bytearray**| The metadata model json file(contents can be retrieved from the controlplane). | [optional] 
 **links** | [**Links**](Links.md)|  | [optional] 
 **version_comment** | **str**|  | [optional] 
 **categories** | [**List[str]**](str.md)|  | [optional] 
 **html_documentation** | **str**|  | [optional] 

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Nextflow pipeline is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pipeline_file**
> PipelineFile create_pipeline_file(project_id, pipeline_id, content)

Create a file for a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.pipeline_file import PipelineFile
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to create a file for
    content = None # bytearray | 

    try:
        # Create a file for a pipeline.
        api_response = api_instance.create_pipeline_file(project_id, pipeline_id, content)
        print("The response of ProjectPipelineApi->create_pipeline_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->create_pipeline_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to create a file for | 
 **content** | **bytearray**|  | 

### Return type

[**PipelineFile**](PipelineFile.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pipeline file is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline_file**
> delete_pipeline_file(project_id, pipeline_id, file_id)

Delete a file for a pipeline.

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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to delete a file for
    file_id = 'file_id_example' # str | The ID of the pipeline file

    try:
        # Delete a file for a pipeline.
        api_instance.delete_pipeline_file(project_id, pipeline_id, file_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->delete_pipeline_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to delete a file for | 
 **file_id** | **str**| The ID of the pipeline file | 

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
**204** | The pipeline file is successfully deleted. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_pipeline_file_content1**
> bytearray download_pipeline_file_content1(project_id, pipeline_id, file_id)

Download the contents of a pipeline file.

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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for
    file_id = 'file_id_example' # str | The ID of the pipeline file

    try:
        # Download the contents of a pipeline file.
        api_response = api_instance.download_pipeline_file_content1(project_id, pipeline_id, file_id)
        print("The response of ProjectPipelineApi->download_pipeline_file_content1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->download_pipeline_file_content1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 
 **file_id** | **str**| The ID of the pipeline file | 

### Return type

**bytearray**

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline file is successfully downloaded. |  * Content-Disposition - Contains name of the file to be downloaded. <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_files1**
> PipelineFileList get_pipeline_files1(project_id, pipeline_id)

Retrieve files for a project pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.pipeline_file_list import PipelineFileList
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve files for

    try:
        # Retrieve files for a project pipeline.
        api_response = api_instance.get_pipeline_files1(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_pipeline_files1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_pipeline_files1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve files for | 

### Return type

[**PipelineFileList**](PipelineFileList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The files are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline**
> ProjectPipeline get_project_pipeline(project_id, pipeline_id)

Retrieve a project pipeline.

Retrieves a project pipeline. This can be a pipeline from a linked bundle or an entitled, unlinked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.project_pipeline import ProjectPipeline
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve

    try:
        # Retrieve a project pipeline.
        api_response = api_instance.get_project_pipeline(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve | 

### Return type

[**ProjectPipeline**](ProjectPipeline.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The project pipeline is successfully retrieved. |  * ETag - The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). <br>  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_configuration_parameters**
> PipelineConfigurationParameterList get_project_pipeline_configuration_parameters(project_id, pipeline_id)

Retrieve configuration parameters for a project pipeline.

The pipeline can originate from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve input parameters for

    try:
        # Retrieve configuration parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_configuration_parameters(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_configuration_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_configuration_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve input parameters for | 

### Return type

[**PipelineConfigurationParameterList**](PipelineConfigurationParameterList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration parameters are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_html_documentation**
> PipelineHtmlDocumentation get_project_pipeline_html_documentation(project_id, pipeline_id)

Retrieve HTML documentation for a project pipeline.

Retrieve HTML documentation for a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.pipeline_html_documentation import PipelineHtmlDocumentation
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve HTML documentation from

    try:
        # Retrieve HTML documentation for a project pipeline.
        api_response = api_instance.get_project_pipeline_html_documentation(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_html_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_html_documentation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve HTML documentation from | 

### Return type

[**PipelineHtmlDocumentation**](PipelineHtmlDocumentation.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTML documentation is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_input_parameters**
> InputParameterList get_project_pipeline_input_parameters(project_id, pipeline_id)

Retrieve input parameters for a project pipeline.

The pipeline can originate from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.input_parameter_list import InputParameterList
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to retrieve input parameters for

    try:
        # Retrieve input parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_input_parameters(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_input_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_input_parameters: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to retrieve input parameters for | 

### Return type

[**InputParameterList**](InputParameterList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input parameters are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipeline_reference_sets**
> ReferenceSetList get_project_pipeline_reference_sets(project_id, pipeline_id)

Retrieve the reference sets of a project pipeline.

Retrieve the reference sets of a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.reference_set_list import ReferenceSetList
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline to retrieve reference sets for

    try:
        # Retrieve the reference sets of a project pipeline.
        api_response = api_instance.get_project_pipeline_reference_sets(project_id, pipeline_id)
        print("The response of ProjectPipelineApi->get_project_pipeline_reference_sets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_reference_sets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline to retrieve reference sets for | 

### Return type

[**ReferenceSetList**](ReferenceSetList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of reference sets is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_pipelines**
> ProjectPipelineList get_project_pipelines(project_id)

Retrieve a list of project pipelines.

Lists all pipelines that are available to the project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.project_pipeline_list import ProjectPipelineList
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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project to retrieve pipelines for

    try:
        # Retrieve a list of project pipelines.
        api_response = api_instance.get_project_pipelines(project_id)
        print("The response of ProjectPipelineApi->get_project_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipelines: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project to retrieve pipelines for | 

### Return type

[**ProjectPipelineList**](ProjectPipelineList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of project pipelines is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_pipeline_to_project**
> link_pipeline_to_project(project_id, pipeline_id)

Link a pipeline to a project.

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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline

    try:
        # Link a pipeline to a project.
        api_instance.link_pipeline_to_project(project_id, pipeline_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->link_pipeline_to_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline | 

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
**204** | The pipeline is successfully linked to the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_pipeline**
> release_pipeline(project_id, pipeline_id)

Release a pipeline.

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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline

    try:
        # Release a pipeline.
        api_instance.release_pipeline(project_id, pipeline_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->release_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline | 

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
**204** | The pipeline is successfully released. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_pipeline_from_project**
> unlink_pipeline_from_project(project_id, pipeline_id)

Unlink a pipeline from a project.

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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the pipeline

    try:
        # Unlink a pipeline from a project.
        api_instance.unlink_pipeline_from_project(project_id, pipeline_id)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->unlink_pipeline_from_project: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the pipeline | 

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
**204** | The pipeline is successfully unlinked from the project. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pipeline_file**
> update_pipeline_file(project_id, pipeline_id, file_id, content)

Update the contents of a file for a pipeline.

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
    api_instance = icasdk.ProjectPipelineApi(api_client)
    project_id = 'project_id_example' # str | 
    pipeline_id = 'pipeline_id_example' # str | The ID of the project pipeline to update a file for
    file_id = 'file_id_example' # str | The ID of the pipeline file
    content = None # bytearray | 

    try:
        # Update the contents of a file for a pipeline.
        api_instance.update_pipeline_file(project_id, pipeline_id, file_id, content)
    except Exception as e:
        print("Exception when calling ProjectPipelineApi->update_pipeline_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **pipeline_id** | **str**| The ID of the project pipeline to update a file for | 
 **file_id** | **str**| The ID of the pipeline file | 
 **content** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pipeline file is successfully updated. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

