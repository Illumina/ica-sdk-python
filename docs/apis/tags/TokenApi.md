<a name="__pageTop"></a>
# icasdk.apis.tags.token_api.TokenApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jwt_token**](#create_jwt_token) | **post** /api/tokens | Generate a JWT using an API-key, Basic Authentication or a psToken.
[**refresh_jwt_token**](#refresh_jwt_token) | **post** /api/tokens:refresh | Refresh a JWT using a not yet expired, still valid JWT.

# **create_jwt_token**
<a name="create_jwt_token"></a>
> Token create_jwt_token()

Generate a JWT using an API-key, Basic Authentication or a psToken.

Generate a JWT using an API-key, Basic Authentication or a psToken. When using Basic Authentication, and you are member of several tenants, also provide the tenant request parameter to indicate for which tenant you want to authenticate. Note that Basic Authentication will not work for SSO (Single Sign On) enabled authentication.

### Example

* Bearer (psToken) Authentication (PsTokenAuth):
* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
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

# Configure Bearer authorization (psToken): PsTokenAuth
configuration = icasdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure HTTP basic authorization: BasicAuth
configuration = icasdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = token_api.TokenApi(api_client)

    # example passing only optional values
    query_params = {
        'tenant': "tenant_example",
    }
    try:
        # Generate a JWT using an API-key, Basic Authentication or a psToken.
        api_response = api_instance.create_jwt_token(
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling TokenApi->create_jwt_token: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
tenant | TenantSchema | | optional


# TenantSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_jwt_token.ApiResponseFor200) | The JWT is successfully generated.
default | [ApiResponseForDefault](#create_jwt_token.ApiResponseForDefault) | A problem occurred.

#### create_jwt_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


#### create_jwt_token.ApiResponseForDefault
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

[PsTokenAuth](../../../README.md#PsTokenAuth), [BasicAuth](../../../README.md#BasicAuth), [ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **refresh_jwt_token**
<a name="refresh_jwt_token"></a>
> Token refresh_jwt_token()

Refresh a JWT using a not yet expired, still valid JWT.

When still having a valid JWT, this endpoint can be used to extend the validity.<br>Refreshing the JWT is not possible if it has been created using an API-key.

### Example

* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
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
# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = token_api.TokenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refresh a JWT using a not yet expired, still valid JWT.
        api_response = api_instance.refresh_jwt_token()
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling TokenApi->refresh_jwt_token: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#refresh_jwt_token.ApiResponseFor200) | The JWT is successfully refreshed.
default | [ApiResponseForDefault](#refresh_jwt_token.ApiResponseForDefault) | A problem occurred.

#### refresh_jwt_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**Token**](../../models/Token.md) |  | 


#### refresh_jwt_token.ApiResponseForDefault
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

[JwtAuth](../../../README.md#JwtAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

