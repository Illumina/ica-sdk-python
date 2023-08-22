<a name="__pageTop"></a>
# icasdk.apis.tags.storage_bundle_api.StorageBundleApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_bundles**](#get_storage_bundles) | **get** /api/storageBundles | Retrieve a list of storage bundles.

# **get_storage_bundles**
<a name="get_storage_bundles"></a>
> StorageBundleList get_storage_bundles()

Retrieve a list of storage bundles.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import storage_bundle_api
from icasdk.model.storage_bundle_list import StorageBundleList
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
    api_instance = storage_bundle_api.StorageBundleApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a list of storage bundles.
        api_response = api_instance.get_storage_bundles()
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling StorageBundleApi->get_storage_bundles: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_storage_bundles.ApiResponseFor200) | The list of storage bundles is successfully retrieved.
default | [ApiResponseForDefault](#get_storage_bundles.ApiResponseForDefault) | A problem occurred.

#### get_storage_bundles.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**StorageBundleList**](../../models/StorageBundleList.md) |  | 


#### get_storage_bundles.ApiResponseForDefault
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

