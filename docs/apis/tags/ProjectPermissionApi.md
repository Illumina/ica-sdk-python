<a name="__pageTop"></a>
# icasdk.apis.tags.project_permission_api.ProjectPermissionApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_permission**](#create_project_permission) | **post** /api/projects/{projectId}/permissions | Create a project permission.
[**get_project_permission**](#get_project_permission) | **get** /api/projects/{projectId}/permissions/{permissionId} | Retrieve a project permission.
[**get_project_permissions**](#get_project_permissions) | **get** /api/projects/{projectId}/permissions | Retrieve a list of project permissions.
[**update_project_permission**](#update_project_permission) | **put** /api/projects/{projectId}/permissions/{permissionId} | Update a project permission.

# **create_project_permission**
<a name="create_project_permission"></a>
> ProjectPermissionV4 create_project_permission(project_idcreate_project_permission_v4)

Create a project permission.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3] Initial version ## [V4] Added 'Administrator' role for Bench. The role attributes are strings instead of enums to support future additions in a backward compatible manner. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_permission_api
from icasdk.model.project_permission_v4 import ProjectPermissionV4
from icasdk.model.create_project_permission import CreateProjectPermission
from icasdk.model.create_project_permission_v4 import CreateProjectPermissionV4
from icasdk.model.problem import Problem
from icasdk.model.project_permission import ProjectPermission
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    body = CreateProjectPermissionV4(
        role_project="NONE",
        role_flow="CONTRIBUTOR",
        role_base="CONTRIBUTOR",
        role_bench="ADMINISTRATOR",
        membership_type="USER",
        user_id="user_id_example",
        email_address="email_address_example",
        workgroup_id="workgroup_id_example",
        upload_allowed=True,
        download_allowed=True,
    )
    try:
        # Create a project permission.
        api_response = api_instance.create_project_permission(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPermissionApi->create_project_permission: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndIlluminaV4json, SchemaForRequestBodyApplicationVndIlluminaV3json, SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.illumina.v4+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v4+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndIlluminaV4json
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateProjectPermissionV4**](../../models/CreateProjectPermissionV4.md) |  | 


# SchemaForRequestBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateProjectPermission**](../../models/CreateProjectPermission.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateProjectPermission**](../../models/CreateProjectPermission.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_project_permission.ApiResponseFor201) | The project permission is successfully created.
default | [ApiResponseForDefault](#create_project_permission.ApiResponseForDefault) | A problem occurred.

#### create_project_permission.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndIlluminaV4json, SchemaFor201ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationVndIlluminaV4json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermissionV4**](../../models/ProjectPermissionV4.md) |  | 


# SchemaFor201ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermission**](../../models/ProjectPermission.md) |  | 

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


#### create_project_permission.ApiResponseForDefault
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

# **get_project_permission**
<a name="get_project_permission"></a>
> ProjectPermissionV4 get_project_permission(project_idpermission_id)

Retrieve a project permission.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3] Initial version ## [V4] Added 'Administrator' role for Bench. The role attributes are strings instead of enums to support future additions in a backward compatible manner. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_permission_api
from icasdk.model.project_permission_v4 import ProjectPermissionV4
from icasdk.model.problem import Problem
from icasdk.model.project_permission import ProjectPermission
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'permissionId': "permissionId_example",
    }
    try:
        # Retrieve a project permission.
        api_response = api_instance.get_project_permission(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPermissionApi->get_project_permission: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v4+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
permissionId | PermissionIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PermissionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_permission.ApiResponseFor200) | The project permission is successfully retrieved.
default | [ApiResponseForDefault](#get_project_permission.ApiResponseForDefault) | A problem occurred.

#### get_project_permission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV4json, SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationVndIlluminaV4json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermissionV4**](../../models/ProjectPermissionV4.md) |  | 


# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermission**](../../models/ProjectPermission.md) |  | 

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


#### get_project_permission.ApiResponseForDefault
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

# **get_project_permissions**
<a name="get_project_permissions"></a>
> ProjectPermissionListV4 get_project_permissions(project_id)

Retrieve a list of project permissions.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3] Initial version ## [V4] Added 'Administrator' role for Bench. The role attributes are strings instead of enums to support future additions in a backward compatible manner. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_permission_api
from icasdk.model.project_permission_list_v4 import ProjectPermissionListV4
from icasdk.model.problem import Problem
from icasdk.model.project_permission_list import ProjectPermissionList
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    try:
        # Retrieve a list of project permissions.
        api_response = api_instance.get_project_permissions(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPermissionApi->get_project_permissions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v4+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_permissions.ApiResponseFor200) | The list of project permissions is successfully retrieved.
default | [ApiResponseForDefault](#get_project_permissions.ApiResponseForDefault) | A problem occurred.

#### get_project_permissions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV4json, SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV4json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermissionListV4**](../../models/ProjectPermissionListV4.md) |  | 


# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermissionList**](../../models/ProjectPermissionList.md) |  | 


#### get_project_permissions.ApiResponseForDefault
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

# **update_project_permission**
<a name="update_project_permission"></a>
> ProjectPermissionV4 update_project_permission(project_idpermission_idproject_permission_v4)

Update a project permission.

# Changelog For this endpoint multiple versions exist. Note that the values for request headers 'Content-Type' and 'Accept' must contain a matching version.  ## [V3] Initial version ## [V4] Added 'Administrator' role for Bench. The role attributes are strings instead of enums to support future additions in a backward compatible manner. Fields which can be updated: - uploadAllowed - downloadAllowed - roleProject - roleFlow - roleBase - roleBench

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import project_permission_api
from icasdk.model.project_permission_v4 import ProjectPermissionV4
from icasdk.model.problem import Problem
from icasdk.model.project_permission import ProjectPermission
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
    api_instance = project_permission_api.ProjectPermissionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'permissionId': "permissionId_example",
    }
    header_params = {
    }
    body = ProjectPermissionV4(
        id="id_example",
        time_created="1970-01-01T00:00:00.00Z",
        time_modified="1970-01-01T00:00:00.00Z",
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        role_project="role_project_example",
        role_flow="role_flow_example",
        role_base="role_base_example",
        role_bench="role_bench_example",
        membership_type="USER",
        user=User(
            id="id_example",
            time_created="1970-01-01T00:00:00.00Z",
            time_modified="1970-01-01T00:00:00.00Z",
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            username="username_example",
            email="email_example",
            firstname="firstname_example",
            lastname="lastname_example",
            active=True,
            tenant_administrator=True,
            job_title="job_title_example",
            greeting="MR",
            mobile_phone_number="mobile_phone_number_example",
            phone_number="phone_number_example",
            fax_number="fax_number_example",
            email_verified=True,
            two_factor_authentication=True,
            country=Country(
                id="id_example",
                time_created="1970-01-01T00:00:00.00Z",
                time_modified="1970-01-01T00:00:00.00Z",
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                code="code_example",
                name="name_example",
                region="region_example",
            ),
            address_line1="address_line1_example",
            address_line2="address_line2_example",
            address_line3="address_line3_example",
            postal_code="postal_code_example",
            city="city_example",
            state="state_example",
        ),
        email_address="email_address_example",
        workgroup=Workgroup(
            id="id_example",
            name="name_example",
            description="description_example",
        ),
        invitation_accepted=True,
        invitation_rejected=True,
        upload_allowed=True,
        download_allowed=True,
    )
    try:
        # Update a project permission.
        api_response = api_instance.update_project_permission(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPermissionApi->update_project_permission: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
        'permissionId': "permissionId_example",
    }
    header_params = {
        'If-Match': "If-Match_example",
    }
    body = ProjectPermissionV4(
        id="id_example",
        time_created="1970-01-01T00:00:00.00Z",
        time_modified="1970-01-01T00:00:00.00Z",
        owner_id="owner_id_example",
        tenant_id="tenant_id_example",
        tenant_name="tenant_name_example",
        role_project="role_project_example",
        role_flow="role_flow_example",
        role_base="role_base_example",
        role_bench="role_bench_example",
        membership_type="USER",
        user=User(
            id="id_example",
            time_created="1970-01-01T00:00:00.00Z",
            time_modified="1970-01-01T00:00:00.00Z",
            owner_id="owner_id_example",
            tenant_id="tenant_id_example",
            tenant_name="tenant_name_example",
            username="username_example",
            email="email_example",
            firstname="firstname_example",
            lastname="lastname_example",
            active=True,
            tenant_administrator=True,
            job_title="job_title_example",
            greeting="MR",
            mobile_phone_number="mobile_phone_number_example",
            phone_number="phone_number_example",
            fax_number="fax_number_example",
            email_verified=True,
            two_factor_authentication=True,
            country=Country(
                id="id_example",
                time_created="1970-01-01T00:00:00.00Z",
                time_modified="1970-01-01T00:00:00.00Z",
                owner_id="owner_id_example",
                tenant_id="tenant_id_example",
                tenant_name="tenant_name_example",
                code="code_example",
                name="name_example",
                region="region_example",
            ),
            address_line1="address_line1_example",
            address_line2="address_line2_example",
            address_line3="address_line3_example",
            postal_code="postal_code_example",
            city="city_example",
            state="state_example",
        ),
        email_address="email_address_example",
        workgroup=Workgroup(
            id="id_example",
            name="name_example",
            description="description_example",
        ),
        invitation_accepted=True,
        invitation_rejected=True,
        upload_allowed=True,
        download_allowed=True,
    )
    try:
        # Update a project permission.
        api_response = api_instance.update_project_permission(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPermissionApi->update_project_permission: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndIlluminaV4json, SchemaForRequestBodyApplicationVndIlluminaV3json, SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.illumina.v4+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v4+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndIlluminaV4json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermissionV4**](../../models/ProjectPermissionV4.md) |  | 


# SchemaForRequestBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermission**](../../models/ProjectPermission.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermission**](../../models/ProjectPermission.md) |  | 


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
projectId | ProjectIdSchema | | 
permissionId | PermissionIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PermissionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_project_permission.ApiResponseFor200) | The project permission is successfully updated.
default | [ApiResponseForDefault](#update_project_permission.ApiResponseForDefault) | A problem occurred.

#### update_project_permission.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV4json, SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationVndIlluminaV4json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermissionV4**](../../models/ProjectPermissionV4.md) |  | 


# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPermission**](../../models/ProjectPermission.md) |  | 

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


#### update_project_permission.ApiResponseForDefault
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

