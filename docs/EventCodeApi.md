# icasdk.EventCodeApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_codes**](EventCodeApi.md#get_event_codes) | **GET** /api/eventCodes | Retrieve event codes


# **get_event_codes**
> EventCodeList get_event_codes()

Retrieve event codes

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.event_code_list import EventCodeList
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
    api_instance = icasdk.EventCodeApi(api_client)

    try:
        # Retrieve event codes
        api_response = api_instance.get_event_codes()
        print("The response of EventCodeApi->get_event_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventCodeApi->get_event_codes: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**EventCodeList**](EventCodeList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The event codes are successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
