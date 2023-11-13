<a name="__pageTop"></a>
# icasdk.apis.tags.notification_channel_api.NotificationChannelApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_channel**](#create_notification_channel) | **post** /api/notificationChannels | Create a notification channel
[**delete_notification_channel**](#delete_notification_channel) | **delete** /api/notificationChannels/{channelId} | Delete a notification channel
[**get_notification_channel**](#get_notification_channel) | **get** /api/notificationChannels/{channelId} | Retrieve a notification channel
[**get_notification_channels**](#get_notification_channels) | **get** /api/notificationChannels | Retrieve notification channels
[**update_notification_channel**](#update_notification_channel) | **put** /api/notificationChannels/{channelId} | Update a notification channel

# **create_notification_channel**
<a name="create_notification_channel"></a>
> NotificationChannel create_notification_channel(create_notification_channel)

Create a notification channel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import notification_channel_api
from icasdk.model.create_notification_channel import CreateNotificationChannel
from icasdk.model.problem import Problem
from icasdk.model.notification_channel import NotificationChannel
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateNotificationChannel(
        enabled=True,
        type="MAIL",
        address="address_example",
    )
    try:
        # Create a notification channel
        api_response = api_instance.create_notification_channel(
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling NotificationChannelApi->create_notification_channel: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndIlluminaV3json, SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/vnd.illumina.v3+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateNotificationChannel**](../../models/CreateNotificationChannel.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateNotificationChannel**](../../models/CreateNotificationChannel.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_notification_channel.ApiResponseFor201) | The notification channel is successfully created.
default | [ApiResponseForDefault](#create_notification_channel.ApiResponseForDefault) | A problem occurred.

#### create_notification_channel.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationChannel**](../../models/NotificationChannel.md) |  | 

#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ETag | ETagSchema | | optional

# ETagSchema

The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). | 


#### create_notification_channel.ApiResponseForDefault
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

# **delete_notification_channel**
<a name="delete_notification_channel"></a>
> delete_notification_channel(channel_id)

Delete a notification channel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import notification_channel_api
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'channelId': "channelId_example",
    }
    try:
        # Delete a notification channel
        api_response = api_instance.delete_notification_channel(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling NotificationChannelApi->delete_notification_channel: %s\n" % e)
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
channelId | ChannelIdSchema | | 

# ChannelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_notification_channel.ApiResponseFor204) | The notification channel is successfully deleted
default | [ApiResponseForDefault](#delete_notification_channel.ApiResponseForDefault) | A problem occurred.

#### delete_notification_channel.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### delete_notification_channel.ApiResponseForDefault
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

# **get_notification_channel**
<a name="get_notification_channel"></a>
> NotificationChannel get_notification_channel(channel_id)

Retrieve a notification channel

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import notification_channel_api
from icasdk.model.problem import Problem
from icasdk.model.notification_channel import NotificationChannel
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'channelId': "channelId_example",
    }
    try:
        # Retrieve a notification channel
        api_response = api_instance.get_notification_channel(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling NotificationChannelApi->get_notification_channel: %s\n" % e)
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
channelId | ChannelIdSchema | | 

# ChannelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_notification_channel.ApiResponseFor200) | The notification channel is successfully retrieved.
default | [ApiResponseForDefault](#get_notification_channel.ApiResponseForDefault) | A problem occurred.

#### get_notification_channel.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationChannel**](../../models/NotificationChannel.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ETag | ETagSchema | | optional

# ETagSchema

The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). | 


#### get_notification_channel.ApiResponseForDefault
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

# **get_notification_channels**
<a name="get_notification_channels"></a>
> NotificationChannelList get_notification_channels()

Retrieve notification channels

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import notification_channel_api
from icasdk.model.problem import Problem
from icasdk.model.notification_channel_list import NotificationChannelList
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve notification channels
        api_response = api_instance.get_notification_channels()
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling NotificationChannelApi->get_notification_channels: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_notification_channels.ApiResponseFor200) | The notification channels are successfully retrieved.
default | [ApiResponseForDefault](#get_notification_channels.ApiResponseForDefault) | A problem occurred.

#### get_notification_channels.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationChannelList**](../../models/NotificationChannelList.md) |  | 


#### get_notification_channels.ApiResponseForDefault
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

# **update_notification_channel**
<a name="update_notification_channel"></a>
> NotificationChannel update_notification_channel(channel_idnotification_channel)

Update a notification channel

This will affect all subscriptions which use this address!Fields which can be updated:  - enabled  - address 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import notification_channel_api
from icasdk.model.problem import Problem
from icasdk.model.notification_channel import NotificationChannel
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
    api_instance = notification_channel_api.NotificationChannelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'channelId': "channelId_example",
    }
    header_params = {
    }
    body = NotificationChannel(
        id="id_example",
        time_created="1970-01-01T00:00:00.00Z",
        time_modified="1970-01-01T00:00:00.00Z",
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        enabled=True,
        type="MAIL",
        address="address_example",
    )
    try:
        # Update a notification channel
        api_response = api_instance.update_notification_channel(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling NotificationChannelApi->update_notification_channel: %s\n" % e)

    # example passing only optional values
    path_params = {
        'channelId': "channelId_example",
    }
    header_params = {
        'If-Match': "If-Match_example",
    }
    body = NotificationChannel(
        id="id_example",
        time_created="1970-01-01T00:00:00.00Z",
        time_modified="1970-01-01T00:00:00.00Z",
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        enabled=True,
        type="MAIL",
        address="address_example",
    )
    try:
        # Update a notification channel
        api_response = api_instance.update_notification_channel(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling NotificationChannelApi->update_notification_channel: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndIlluminaV3json, SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.illumina.v3+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationChannel**](../../models/NotificationChannel.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationChannel**](../../models/NotificationChannel.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
If-Match | IfMatchSchema | | optional

# IfMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
channelId | ChannelIdSchema | | 

# ChannelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_notification_channel.ApiResponseFor200) | The notification channel is successfully updated.
default | [ApiResponseForDefault](#update_notification_channel.ApiResponseForDefault) | A problem occurred.

#### update_notification_channel.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**NotificationChannel**](../../models/NotificationChannel.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ETag | ETagSchema | | optional

# ETagSchema

The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The current version of the resource. Can be passed to the corresponding PUT endpoint to enable conflict exposure (409 response). | 


#### update_notification_channel.ApiResponseForDefault
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

