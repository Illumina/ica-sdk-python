<a name="__pageTop"></a>
# icasdk.apis.tags.entitlement_detail_api.EntitlementDetailApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_all_matching_activation_codes_for_cwl**](#find_all_matching_activation_codes_for_cwl) | **post** /api/activationCodes:findAllMatchingForCwl | Search all matching activation code details for a Cwl pipeline.
[**find_all_matching_activation_codes_for_nextflow**](#find_all_matching_activation_codes_for_nextflow) | **post** /api/activationCodes:findAllMatchingForNextflow | Search all matching activation code details for a Nextflow pipeline.
[**find_best_matching_activation_code_for_cwl**](#find_best_matching_activation_code_for_cwl) | **post** /api/activationCodes:findBestMatchingForCwl | Search the best matching activation code detail for Cwl pipeline.
[**find_best_matching_activation_codes_for_nextflow**](#find_best_matching_activation_codes_for_nextflow) | **post** /api/activationCodes:findBestMatchingForNextflow | Search the best matching activation code details for Nextflow pipeline.

# **find_all_matching_activation_codes_for_cwl**
<a name="find_all_matching_activation_codes_for_cwl"></a>
> ActivationCodeDetailList find_all_matching_activation_codes_for_cwl(search_matching_activation_codes_for_cwl_analysis)

Search all matching activation code details for a Cwl pipeline.

Endpoint for searching all matching activation code details for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import entitlement_detail_api
from icasdk.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
from icasdk.model.activation_code_detail_list import ActivationCodeDetailList
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)

    # example passing only required values which don't have defaults set
    body = SearchMatchingActivationCodesForCwlAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=CwlAnalysisInput(
            object_type="CwlAnalysisJsonInput",
            input_json="input_json_example",
            data_ids=[
                "data_ids_example"
            ],
            mounts=[
                AnalysisInputDataMount(
                    data_id="data_id_example",
                    mount_path="mount_path_example",
                )
            ],
            external_data=[
                AnalysisInputExternalData(
                    url="url_example",
                    type="http",
                    mount_path="mount_path_example",
                    s3_details=AnalysisS3DataDetails(
                        storage_credentials_id="storage_credentials_id_example",
                    ),
                )
            ],
        ),
    )
    try:
        # Search all matching activation code details for a Cwl pipeline.
        api_response = api_instance.find_all_matching_activation_codes_for_cwl(
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_all_matching_activation_codes_for_cwl: %s\n" % e)
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
[**SearchMatchingActivationCodesForCwlAnalysis**](../../models/SearchMatchingActivationCodesForCwlAnalysis.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchMatchingActivationCodesForCwlAnalysis**](../../models/SearchMatchingActivationCodesForCwlAnalysis.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_all_matching_activation_codes_for_cwl.ApiResponseFor200) | The matching activation code details are successfully searched.
default | [ApiResponseForDefault](#find_all_matching_activation_codes_for_cwl.ApiResponseForDefault) | A problem occurred.

#### find_all_matching_activation_codes_for_cwl.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ActivationCodeDetailList**](../../models/ActivationCodeDetailList.md) |  | 


#### find_all_matching_activation_codes_for_cwl.ApiResponseForDefault
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

# **find_all_matching_activation_codes_for_nextflow**
<a name="find_all_matching_activation_codes_for_nextflow"></a>
> ActivationCodeDetailList find_all_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis)

Search all matching activation code details for a Nextflow pipeline.

Endpoint for searching all matching activation code details for a project and an analysis from a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import entitlement_detail_api
from icasdk.model.activation_code_detail_list import ActivationCodeDetailList
from icasdk.model.problem import Problem
from icasdk.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)

    # example passing only required values which don't have defaults set
    body = SearchMatchingActivationCodesForNextflowAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=NextflowAnalysisInput(
            inputs=[
                AnalysisDataInput(
                    parameter_code="parameter_code_example",
                    data_ids=[
                        "data_ids_example"
                    ],
                    mounts=[
                        AnalysisInputDataMount(
                            data_id="data_id_example",
                            mount_path="mount_path_example",
                        )
                    ],
                    external_data=[
                        AnalysisInputExternalData(
                            url="url_example",
                            type="http",
                            mount_path="mount_path_example",
                            s3_details=AnalysisS3DataDetails(
                                storage_credentials_id="storage_credentials_id_example",
                            ),
                        )
                    ],
                )
            ],
            parameters=[
                AnalysisParameterInput(
                    code="code_example",
                    value="value_example",
                    multi_value=[
                        "multi_value_example"
                    ],
                )
            ],
            reference_data_parameters=[
                AnalysisReferenceDataParameter(
                    parameter_code="parameter_code_example",
                    reference_data_id="reference_data_id_example",
                )
            ],
        ),
    )
    try:
        # Search all matching activation code details for a Nextflow pipeline.
        api_response = api_instance.find_all_matching_activation_codes_for_nextflow(
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_all_matching_activation_codes_for_nextflow: %s\n" % e)
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
[**SearchMatchingActivationCodesForNextflowAnalysis**](../../models/SearchMatchingActivationCodesForNextflowAnalysis.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchMatchingActivationCodesForNextflowAnalysis**](../../models/SearchMatchingActivationCodesForNextflowAnalysis.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_all_matching_activation_codes_for_nextflow.ApiResponseFor200) | The matching activation code details are successfully searched.
default | [ApiResponseForDefault](#find_all_matching_activation_codes_for_nextflow.ApiResponseForDefault) | A problem occurred.

#### find_all_matching_activation_codes_for_nextflow.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ActivationCodeDetailList**](../../models/ActivationCodeDetailList.md) |  | 


#### find_all_matching_activation_codes_for_nextflow.ApiResponseForDefault
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

# **find_best_matching_activation_code_for_cwl**
<a name="find_best_matching_activation_code_for_cwl"></a>
> ActivationCodeDetail find_best_matching_activation_code_for_cwl(search_matching_activation_codes_for_cwl_analysis)

Search the best matching activation code detail for Cwl pipeline.

Endpoint for searching the best activation code detail for a project and an analysis from a Cwl pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import entitlement_detail_api
from icasdk.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
from icasdk.model.activation_code_detail import ActivationCodeDetail
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)

    # example passing only required values which don't have defaults set
    body = SearchMatchingActivationCodesForCwlAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=CwlAnalysisInput(
            object_type="CwlAnalysisJsonInput",
            input_json="input_json_example",
            data_ids=[
                "data_ids_example"
            ],
            mounts=[
                AnalysisInputDataMount(
                    data_id="data_id_example",
                    mount_path="mount_path_example",
                )
            ],
            external_data=[
                AnalysisInputExternalData(
                    url="url_example",
                    type="http",
                    mount_path="mount_path_example",
                    s3_details=AnalysisS3DataDetails(
                        storage_credentials_id="storage_credentials_id_example",
                    ),
                )
            ],
        ),
    )
    try:
        # Search the best matching activation code detail for Cwl pipeline.
        api_response = api_instance.find_best_matching_activation_code_for_cwl(
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_best_matching_activation_code_for_cwl: %s\n" % e)
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
[**SearchMatchingActivationCodesForCwlAnalysis**](../../models/SearchMatchingActivationCodesForCwlAnalysis.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchMatchingActivationCodesForCwlAnalysis**](../../models/SearchMatchingActivationCodesForCwlAnalysis.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_best_matching_activation_code_for_cwl.ApiResponseFor200) | The best matching activation code details are successfully searched.
default | [ApiResponseForDefault](#find_best_matching_activation_code_for_cwl.ApiResponseForDefault) | A problem occurred.

#### find_best_matching_activation_code_for_cwl.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ActivationCodeDetail**](../../models/ActivationCodeDetail.md) |  | 


#### find_best_matching_activation_code_for_cwl.ApiResponseForDefault
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

# **find_best_matching_activation_codes_for_nextflow**
<a name="find_best_matching_activation_codes_for_nextflow"></a>
> ActivationCodeDetail find_best_matching_activation_codes_for_nextflow(search_matching_activation_codes_for_nextflow_analysis)

Search the best matching activation code details for Nextflow pipeline.

Endpoint for searching the best activation code details for a project and an analysis for a Nextflow pipeline.This is a non-RESTful endpoint, as the path of this endpoint is not representing a REST resource.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (JwtAuth):
```python
import icasdk
from icasdk.apis.tags import entitlement_detail_api
from icasdk.model.activation_code_detail import ActivationCodeDetail
from icasdk.model.problem import Problem
from icasdk.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
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
    api_instance = entitlement_detail_api.EntitlementDetailApi(api_client)

    # example passing only required values which don't have defaults set
    body = SearchMatchingActivationCodesForNextflowAnalysis(
        project_id="project_id_example",
        pipeline_id="pipeline_id_example",
        analysis_input=NextflowAnalysisInput(
            inputs=[
                AnalysisDataInput(
                    parameter_code="parameter_code_example",
                    data_ids=[
                        "data_ids_example"
                    ],
                    mounts=[
                        AnalysisInputDataMount(
                            data_id="data_id_example",
                            mount_path="mount_path_example",
                        )
                    ],
                    external_data=[
                        AnalysisInputExternalData(
                            url="url_example",
                            type="http",
                            mount_path="mount_path_example",
                            s3_details=AnalysisS3DataDetails(
                                storage_credentials_id="storage_credentials_id_example",
                            ),
                        )
                    ],
                )
            ],
            parameters=[
                AnalysisParameterInput(
                    code="code_example",
                    value="value_example",
                    multi_value=[
                        "multi_value_example"
                    ],
                )
            ],
            reference_data_parameters=[
                AnalysisReferenceDataParameter(
                    parameter_code="parameter_code_example",
                    reference_data_id="reference_data_id_example",
                )
            ],
        ),
    )
    try:
        # Search the best matching activation code details for Nextflow pipeline.
        api_response = api_instance.find_best_matching_activation_codes_for_nextflow(
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling EntitlementDetailApi->find_best_matching_activation_codes_for_nextflow: %s\n" % e)
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
[**SearchMatchingActivationCodesForNextflowAnalysis**](../../models/SearchMatchingActivationCodesForNextflowAnalysis.md) |  | 


# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchMatchingActivationCodesForNextflowAnalysis**](../../models/SearchMatchingActivationCodesForNextflowAnalysis.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_best_matching_activation_codes_for_nextflow.ApiResponseFor200) | The best matching activation code details are successfully searched.
default | [ApiResponseForDefault](#find_best_matching_activation_codes_for_nextflow.ApiResponseForDefault) | A problem occurred.

#### find_best_matching_activation_codes_for_nextflow.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ActivationCodeDetail**](../../models/ActivationCodeDetail.md) |  | 


#### find_best_matching_activation_codes_for_nextflow.ApiResponseForDefault
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

