# icasdk.ProjectSampleBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sample_creation_batch**](ProjectSampleBatchApi.md#create_sample_creation_batch) | **POST** /api/projects/{projectId}/sampleCreationBatch | Create a sample creation batch.
[**get_sample_creation_batch**](ProjectSampleBatchApi.md#get_sample_creation_batch) | **GET** /api/projects/{projectId}/sampleCreationBatch/{batchId} | Retrieve a sample creation batch.
[**get_sample_creation_batch_item**](ProjectSampleBatchApi.md#get_sample_creation_batch_item) | **GET** /api/projects/{projectId}/sampleCreationBatch/{batchId}/items/{itemId} | Retrieve a sample creation batch item.
[**get_sample_creation_batch_items**](ProjectSampleBatchApi.md#get_sample_creation_batch_items) | **GET** /api/projects/{projectId}/sampleCreationBatch/{batchId}/items | Retrieve a list of sample creation batch items.


# **create_sample_creation_batch**
> SampleCreationBatch create_sample_creation_batch(project_id, create_sample_creation_batch, idempotency_key=idempotency_key)

Create a sample creation batch.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.create_sample_creation_batch import CreateSampleCreationBatch
from icasdk.models.sample_creation_batch import SampleCreationBatch
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
    api_instance = icasdk.ProjectSampleBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    create_sample_creation_batch = icasdk.CreateSampleCreationBatch() # CreateSampleCreationBatch | 
    idempotency_key = 'idempotency_key_example' # str | The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:<br /><ul><li>the request body is the same as the previous request and an answer is stored => the stored response is returned without executing the request again.</li><li>the request body is the same as the previous request and no answer is stored because the previous request has not finished => 409 error response.</li><li>the request body is not the same as the previous request => 422 error response.</li></ul>This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn't been used in the past 7 days for that specific API and by the specific user. (optional)

    try:
        # Create a sample creation batch.
        api_response = api_instance.create_sample_creation_batch(project_id, create_sample_creation_batch, idempotency_key=idempotency_key)
        print("The response of ProjectSampleBatchApi->create_sample_creation_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleBatchApi->create_sample_creation_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **create_sample_creation_batch** | [**CreateSampleCreationBatch**](CreateSampleCreationBatch.md)|  | 
 **idempotency_key** | **str**| The Idempotency-Key header can be used to prevent duplicate requests and support retries. It is implemented according to the IETF spec and is allowed to be max 255 characters long. If the header is supplied, the response of the request will be saved for 7 days for the specific API endpoint, header value and user reference. When the same user makes a new request within 7 days to the same API endpoint with the same Idempotency-Key header value, following use cases can occur:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;the request body is the same as the previous request and an answer is stored &#x3D;&gt; the stored response is returned without executing the request again.&lt;/li&gt;&lt;li&gt;the request body is the same as the previous request and no answer is stored because the previous request has not finished &#x3D;&gt; 409 error response.&lt;/li&gt;&lt;li&gt;the request body is not the same as the previous request &#x3D;&gt; 422 error response.&lt;/li&gt;&lt;/ul&gt;This means that each time when executing an API request using the Idempotency-Key header, the request has to contain a new value that hasn&#39;t been used in the past 7 days for that specific API and by the specific user. | [optional] 

### Return type

[**SampleCreationBatch**](SampleCreationBatch.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/vnd.illumina.v3+json, application/x-www-form-urlencoded, application/json
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The sample creation batch is successfully created. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_creation_batch**
> SampleCreationBatch get_sample_creation_batch(project_id, batch_id)

Retrieve a sample creation batch.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.sample_creation_batch import SampleCreationBatch
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
    api_instance = icasdk.ProjectSampleBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | The ID of the sample creation batch

    try:
        # Retrieve a sample creation batch.
        api_response = api_instance.get_sample_creation_batch(project_id, batch_id)
        print("The response of ProjectSampleBatchApi->get_sample_creation_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**| The ID of the sample creation batch | 

### Return type

[**SampleCreationBatch**](SampleCreationBatch.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sample creation batch is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_creation_batch_item**
> SampleCreationBatchSampleItem get_sample_creation_batch_item(project_id, batch_id, item_id)

Retrieve a sample creation batch item.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.sample_creation_batch_sample_item import SampleCreationBatchSampleItem
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
    api_instance = icasdk.ProjectSampleBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | The ID of the sample creation batch
    item_id = 'item_id_example' # str | The ID of the sample creation batch item

    try:
        # Retrieve a sample creation batch item.
        api_response = api_instance.get_sample_creation_batch_item(project_id, batch_id, item_id)
        print("The response of ProjectSampleBatchApi->get_sample_creation_batch_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**| The ID of the sample creation batch | 
 **item_id** | **str**| The ID of the sample creation batch item | 

### Return type

[**SampleCreationBatchSampleItem**](SampleCreationBatchSampleItem.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sample creation batch item is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sample_creation_batch_items**
> SampleCreationBatchItemPagedList get_sample_creation_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)

Retrieve a list of sample creation batch items.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import icasdk
from icasdk.models.sample_creation_batch_item_paged_list import SampleCreationBatchItemPagedList
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
    api_instance = icasdk.ProjectSampleBatchApi(api_client)
    project_id = 'project_id_example' # str | 
    batch_id = 'batch_id_example' # str | The ID of the sample creation batch
    status = ['status_example'] # List[str] | The statuses to filter on. (optional)
    page_offset = 'page_offset_example' # str | [only use with offset-based paging]<br>The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages (optional)
    page_token = 'page_token_example' # str | [only use with cursor-based paging]<br>The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. (optional)
    page_size = 'page_size_example' # str | [can be used with both offset- and cursor-based paging]<br>The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results (optional)
    sort = 'sort_example' # str | [only use with offset-based paging]<br>Which field to order the results by. The default order is ascending, suffix with ' desc' to sort descending (suffix ' asc' also works for ascending). Multiple values should be separated with commas. An example: \"?sort=dateCreated, lastName desc\" (optional)

    try:
        # Retrieve a list of sample creation batch items.
        api_response = api_instance.get_sample_creation_batch_items(project_id, batch_id, status=status, page_offset=page_offset, page_token=page_token, page_size=page_size, sort=sort)
        print("The response of ProjectSampleBatchApi->get_sample_creation_batch_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectSampleBatchApi->get_sample_creation_batch_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **batch_id** | **str**| The ID of the sample creation batch | 
 **status** | [**List[str]**](str.md)| The statuses to filter on. | [optional] 
 **page_offset** | **str**| [only use with offset-based paging]&lt;br&gt;The amount of rows to skip in the result. Ideally this is a multiple of the size parameter. Offset-based pagination has a result limit of 200K rows and does not guarantee unique results across pages | [optional] 
 **page_token** | **str**| [only use with cursor-based paging]&lt;br&gt;The cursor to get subsequent results. The value to use is returned in the result when using cursor-based pagination. Cursor-based pagination guarantees complete and unique results across all pages. | [optional] 
 **page_size** | **str**| [can be used with both offset- and cursor-based paging]&lt;br&gt;The amount of rows to return. Use in combination with the offset (when using offset-based pagination) or cursor (when using cursor-based pagination) parameter to get subsequent results | [optional] 
 **sort** | **str**| [only use with offset-based paging]&lt;br&gt;Which field to order the results by. The default order is ascending, suffix with &#39; desc&#39; to sort descending (suffix &#39; asc&#39; also works for ascending). Multiple values should be separated with commas. An example: \&quot;?sort&#x3D;dateCreated, lastName desc\&quot; | [optional] 

### Return type

[**SampleCreationBatchItemPagedList**](SampleCreationBatchItemPagedList.md)

### Authorization

[JwtAuth](../README.md#JwtAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/vnd.illumina.v3+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of sample creation batch items is successfully retrieved. |  -  |
**0** | A problem occurred. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
