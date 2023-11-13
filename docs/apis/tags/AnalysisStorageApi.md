<a name="__pageTop"></a>
# icasdk.apis.tags.analysis_storage_api.AnalysisStorageApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analysis_storage_options**](#get_analysis_storage_options) | **get** /api/analysisStorages | Retrieve the list of analysis storage options.

# **get_analysis_storage_options**
<a name="get_analysis_storage_options"></a>
> AnalysisStorageList get_analysis_storage_options()

Retrieve the list of analysis storage options.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import analysis_storage_api
from icasdk.model.analysis_storage_list import AnalysisStorageList
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
    api_instance = analysis_storage_api.AnalysisStorageApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve the list of analysis storage options.
        api_response = api_instance.get_analysis_storage_options()
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling AnalysisStorageApi->get_analysis_storage_options: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analysis_storage_options.ApiResponseFor200) | The list of analysis storage options is successfully retrieved.
default | [ApiResponseForDefault](#get_analysis_storage_options.ApiResponseForDefault) | A problem occurred.

#### get_analysis_storage_options.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalysisStorageList**](../../models/AnalysisStorageList.md) |  | 


#### get_analysis_storage_options.ApiResponseForDefault
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

