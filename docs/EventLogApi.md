# icasdk.EventLogApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_logs**](EventLogApi.md#get_event_logs) | **GET** /api/eventLog | Retrieve a list of event logs.


# **get_event_logs**
> EventLogList get_event_logs(code=code, code_filter_type=code_filter_type, category=category, date_from=date_from, date_until=date_until, rows=rows)

Retrieve a list of event logs.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.event_log_list import EventLogList
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
    api_instance = icasdk.EventLogApi(api_client)
    code = 'code_example' # str | Code (optional)
    code_filter_type = 'code_filter_type_example' # str | Code filter type (optional)
    category = 'category_example' # str | Category (optional)
    date_from = 'date_from_example' # str | Date from. Format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z' eg: 2017-01-10T10:47:56.039Z (optional)
    date_until = 'date_until_example' # str | Date until. Format: yyyy-MM-dd'T'HH:mm:ss.SSS'Z' eg: 2017-01-10T10:47:56.039Z (optional)
    rows = 250 # int | Amount of rows to fetch. Maximum 250. Defaults to 250 (optional) (default to 250)

    try:
        # Retrieve a list of event logs.
        api_response = api_instance.get_event_logs(code=code, code_filter_type=code_filter_type, category=category, date_from=date_from, date_until=date_until, rows=rows)
        print("The response of EventLogApi->get_event_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventLogApi->get_event_logs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code | [optional] 
 **code_filter_type** | **str**| Code filter type | [optional] 
 **category** | **str**| Category | [optional] 
 **date_from** | **str**| Date from. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
 **date_until** | **str**| Date until. Format: yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39; eg: 2017-01-10T10:47:56.039Z | [optional] 
 **rows** | **int**| Amount of rows to fetch. Maximum 250. Defaults to 250 | [optional] [default to 250]

### Return type

[**EventLogList**](EventLogList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of event logs is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

