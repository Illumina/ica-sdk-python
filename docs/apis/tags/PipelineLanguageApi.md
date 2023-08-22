<a name="__pageTop"></a>
# icasdk.apis.tags.pipeline_language_api.PipelineLanguageApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nextflow_versions**](#get_nextflow_versions) | **get** /api/pipelineLanguages/nextflow/versions | Retrieve a list of nextflow versions.

# **get_nextflow_versions**
<a name="get_nextflow_versions"></a>
> PipelineLanguageVersionList get_nextflow_versions()

Retrieve a list of nextflow versions.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import pipeline_language_api
from icasdk.model.problem import Problem
from icasdk.model.pipeline_language_version_list import PipelineLanguageVersionList
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_language_api.PipelineLanguageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of nextflow versions.
        api_response = api_instance.get_nextflow_versions()
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling PipelineLanguageApi->get_nextflow_versions: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_nextflow_versions.ApiResponseFor200) | The list of nextflow versions is successfully retrieved.
default | [ApiResponseForDefault](#get_nextflow_versions.ApiResponseForDefault) | A problem occurred.

#### get_nextflow_versions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineLanguageVersionList**](../../models/PipelineLanguageVersionList.md) |  | 


#### get_nextflow_versions.ApiResponseForDefault
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

[JwtAuth](../../../README.md#JwtAuth), [ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

