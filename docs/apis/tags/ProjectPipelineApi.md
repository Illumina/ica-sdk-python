<a name="__pageTop"></a>
# icasdk.apis.tags.project_pipeline_api.ProjectPipelineApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cwl_pipeline**](#create_cwl_pipeline) | **post** /api/projects/{projectId}/pipelines:createCwlPipeline | Create a CWL pipeline within a project.
[**create_nextflow_pipeline**](#create_nextflow_pipeline) | **post** /api/projects/{projectId}/pipelines:createNextflowPipeline | Create a Nextflow pipeline within a project.
[**get_project_pipeline**](#get_project_pipeline) | **get** /api/projects/{projectId}/pipelines/{pipelineId} | Retrieve a project pipeline.
[**get_project_pipeline_configuration_parameters**](#get_project_pipeline_configuration_parameters) | **get** /api/projects/{projectId}/pipelines/{pipelineId}/configurationParameters | Retrieve configuration parameters for a project pipeline.
[**get_project_pipeline_html_documentation**](#get_project_pipeline_html_documentation) | **get** /api/projects/{projectId}/pipelines/{pipelineId}/documentation/HTML | Retrieve HTML documentation for a project pipeline.
[**get_project_pipeline_input_parameters**](#get_project_pipeline_input_parameters) | **get** /api/projects/{projectId}/pipelines/{pipelineId}/inputParameters | Retrieve input parameters for a project pipeline.
[**get_project_pipeline_reference_sets**](#get_project_pipeline_reference_sets) | **get** /api/projects/{projectId}/pipelines/{pipelineId}/referenceSets | Retrieve the reference sets of a project pipeline.
[**get_project_pipelines**](#get_project_pipelines) | **get** /api/projects/{projectId}/pipelines | Retrieve a list of project pipelines.
[**link_pipeline_to_project**](#link_pipeline_to_project) | **post** /api/projects/{projectId}/pipelines/{pipelineId} | Link a pipeline to a project.
[**release_pipeline**](#release_pipeline) | **post** /api/projects/{projectId}/pipelines/{pipelineId}:release | Release a pipeline.
[**unlink_pipeline_from_project**](#unlink_pipeline_from_project) | **delete** /api/projects/{projectId}/pipelines/{pipelineId} | Unlink a pipeline from a project.

# **create_cwl_pipeline**
<a name="create_cwl_pipeline"></a>
> ProjectPipeline create_cwl_pipeline(project_id)

Create a CWL pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.project_pipeline import ProjectPipeline
from icasdk.model.problem import Problem
from icasdk.model.create_cwl_pipeline import CreateCwlPipeline
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    try:
        # Create a CWL pipeline within a project.
        api_response = api_instance.create_cwl_pipeline(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
    }
    body = dict(
        code="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
        description="description_example",
        workflow_cwl_file=open('/path/to/file', 'rb'),
        tool_cwl_files=[
            open('/path/to/file', 'rb')
        ],
        parameters_xml_file=open('/path/to/file', 'rb'),
        metadata_model_file=open('/path/to/file', 'rb'),
        links=Links(
            links=[
                Link(
                    name="name_example",
                    url="url_example",
                )
            ],
,
,
,
        ),
        version_comment="version_comment_example",
        categories=[
            "categories_example"
        ],
        html_documentation="html_documentation_example",
        analysis_storage_id="analysis_storage_id_example",
    )
    try:
        # Create a CWL pipeline within a project.
        api_response = api_instance.create_cwl_pipeline(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateCwlPipeline**](../../models/CreateCwlPipeline.md) |  | 


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
201 | [ApiResponseFor201](#create_cwl_pipeline.ApiResponseFor201) | The CWL pipeline is successfully created.
default | [ApiResponseForDefault](#create_cwl_pipeline.ApiResponseForDefault) | A problem occurred.

#### create_cwl_pipeline.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPipeline**](../../models/ProjectPipeline.md) |  | 


#### create_cwl_pipeline.ApiResponseForDefault
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

# **create_nextflow_pipeline**
<a name="create_nextflow_pipeline"></a>
> ProjectPipeline create_nextflow_pipeline(project_id)

Create a Nextflow pipeline within a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.project_pipeline import ProjectPipeline
from icasdk.model.create_nextflow_pipeline import CreateNextflowPipeline
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    try:
        # Create a Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_pipeline(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_pipeline: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
    }
    body = dict(
        code="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
        pipeline_language_version_id="pipeline_language_version_id_example",
        description="description_example",
        main_nextflow_file=open('/path/to/file', 'rb'),
        nextflow_config_file=open('/path/to/file', 'rb'),
        other_nextflow_files=[
            open('/path/to/file', 'rb')
        ],
        parameters_xml_file=open('/path/to/file', 'rb'),
        metadata_model_file=open('/path/to/file', 'rb'),
        links=Links(
            links=[
                Link(
                    name="name_example",
                    url="url_example",
                )
            ],
,
,
,
        ),
        version_comment="version_comment_example",
        categories=[
            "categories_example"
        ],
        html_documentation="html_documentation_example",
        analysis_storage_id="analysis_storage_id_example",
    )
    try:
        # Create a Nextflow pipeline within a project.
        api_response = api_instance.create_nextflow_pipeline(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->create_nextflow_pipeline: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateNextflowPipeline**](../../models/CreateNextflowPipeline.md) |  | 


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
201 | [ApiResponseFor201](#create_nextflow_pipeline.ApiResponseFor201) | The Nextflow pipeline is successfully created.
default | [ApiResponseForDefault](#create_nextflow_pipeline.ApiResponseForDefault) | A problem occurred.

#### create_nextflow_pipeline.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPipeline**](../../models/ProjectPipeline.md) |  | 


#### create_nextflow_pipeline.ApiResponseForDefault
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

# **get_project_pipeline**
<a name="get_project_pipeline"></a>
> ProjectPipeline get_project_pipeline(project_idpipeline_id)

Retrieve a project pipeline.

Retrieves a project pipeline. This can be a pipeline from a linked bundle or an entitled, unlinked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.project_pipeline import ProjectPipeline
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Retrieve a project pipeline.
        api_response = api_instance.get_project_pipeline(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_pipeline.ApiResponseFor200) | The project pipeline is successfully retrieved.
default | [ApiResponseForDefault](#get_project_pipeline.ApiResponseForDefault) | A problem occurred.

#### get_project_pipeline.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPipeline**](../../models/ProjectPipeline.md) |  | 

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


#### get_project_pipeline.ApiResponseForDefault
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

# **get_project_pipeline_configuration_parameters**
<a name="get_project_pipeline_configuration_parameters"></a>
> PipelineConfigurationParameterList get_project_pipeline_configuration_parameters(project_idpipeline_id)

Retrieve configuration parameters for a project pipeline.

The pipeline can originate from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.problem import Problem
from icasdk.model.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Retrieve configuration parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_configuration_parameters(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_configuration_parameters: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_pipeline_configuration_parameters.ApiResponseFor200) | The configuration parameters are successfully retrieved.
default | [ApiResponseForDefault](#get_project_pipeline_configuration_parameters.ApiResponseForDefault) | A problem occurred.

#### get_project_pipeline_configuration_parameters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineConfigurationParameterList**](../../models/PipelineConfigurationParameterList.md) |  | 


#### get_project_pipeline_configuration_parameters.ApiResponseForDefault
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

# **get_project_pipeline_html_documentation**
<a name="get_project_pipeline_html_documentation"></a>
> PipelineHtmlDocumentation get_project_pipeline_html_documentation(project_idpipeline_id)

Retrieve HTML documentation for a project pipeline.

Retrieve HTML documentation for a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.problem import Problem
from icasdk.model.pipeline_html_documentation import PipelineHtmlDocumentation
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Retrieve HTML documentation for a project pipeline.
        api_response = api_instance.get_project_pipeline_html_documentation(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_html_documentation: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_pipeline_html_documentation.ApiResponseFor200) | The HTML documentation is successfully retrieved.
default | [ApiResponseForDefault](#get_project_pipeline_html_documentation.ApiResponseForDefault) | A problem occurred.

#### get_project_pipeline_html_documentation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineHtmlDocumentation**](../../models/PipelineHtmlDocumentation.md) |  | 


#### get_project_pipeline_html_documentation.ApiResponseForDefault
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

# **get_project_pipeline_input_parameters**
<a name="get_project_pipeline_input_parameters"></a>
> InputParameterList get_project_pipeline_input_parameters(project_idpipeline_id)

Retrieve input parameters for a project pipeline.

The pipeline can originate from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.input_parameter_list import InputParameterList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Retrieve input parameters for a project pipeline.
        api_response = api_instance.get_project_pipeline_input_parameters(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_input_parameters: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_pipeline_input_parameters.ApiResponseFor200) | The input parameters are successfully retrieved.
default | [ApiResponseForDefault](#get_project_pipeline_input_parameters.ApiResponseForDefault) | A problem occurred.

#### get_project_pipeline_input_parameters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**InputParameterList**](../../models/InputParameterList.md) |  | 


#### get_project_pipeline_input_parameters.ApiResponseForDefault
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

# **get_project_pipeline_reference_sets**
<a name="get_project_pipeline_reference_sets"></a>
> ReferenceSetList get_project_pipeline_reference_sets(project_idpipeline_id)

Retrieve the reference sets of a project pipeline.

Retrieve the reference sets of a project pipeline. This can be a pipeline from a linked bundle.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.reference_set_list import ReferenceSetList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Retrieve the reference sets of a project pipeline.
        api_response = api_instance.get_project_pipeline_reference_sets(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipeline_reference_sets: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_pipeline_reference_sets.ApiResponseFor200) | The list of reference sets is successfully retrieved.
default | [ApiResponseForDefault](#get_project_pipeline_reference_sets.ApiResponseForDefault) | A problem occurred.

#### get_project_pipeline_reference_sets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ReferenceSetList**](../../models/ReferenceSetList.md) |  | 


#### get_project_pipeline_reference_sets.ApiResponseForDefault
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

# **get_project_pipelines**
<a name="get_project_pipelines"></a>
> ProjectPipelineList get_project_pipelines(project_id)

Retrieve a list of project pipelines.

Lists all pipelines that are available to the project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
from icasdk.model.project_pipeline_list import ProjectPipelineList
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    try:
        # Retrieve a list of project pipelines.
        api_response = api_instance.get_project_pipelines(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->get_project_pipelines: %s\n" % e)
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
200 | [ApiResponseFor200](#get_project_pipelines.ApiResponseFor200) | The list of project pipelines is successfully retrieved.
default | [ApiResponseForDefault](#get_project_pipelines.ApiResponseForDefault) | A problem occurred.

#### get_project_pipelines.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectPipelineList**](../../models/ProjectPipelineList.md) |  | 


#### get_project_pipelines.ApiResponseForDefault
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

# **link_pipeline_to_project**
<a name="link_pipeline_to_project"></a>
> link_pipeline_to_project(project_idpipeline_id)

Link a pipeline to a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Link a pipeline to a project.
        api_response = api_instance.link_pipeline_to_project(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->link_pipeline_to_project: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#link_pipeline_to_project.ApiResponseFor204) | The pipeline is successfully linked to the project.
default | [ApiResponseForDefault](#link_pipeline_to_project.ApiResponseForDefault) | A problem occurred.

#### link_pipeline_to_project.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### link_pipeline_to_project.ApiResponseForDefault
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

# **release_pipeline**
<a name="release_pipeline"></a>
> release_pipeline(project_idpipeline_id)

Release a pipeline.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Release a pipeline.
        api_response = api_instance.release_pipeline(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->release_pipeline: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#release_pipeline.ApiResponseFor204) | The pipeline is successfully released.
default | [ApiResponseForDefault](#release_pipeline.ApiResponseForDefault) | A problem occurred.

#### release_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### release_pipeline.ApiResponseForDefault
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

# **unlink_pipeline_from_project**
<a name="unlink_pipeline_from_project"></a>
> unlink_pipeline_from_project(project_idpipeline_id)

Unlink a pipeline from a project.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_pipeline_api
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
    api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'pipelineId': "pipelineId_example",
    }
    try:
        # Unlink a pipeline from a project.
        api_response = api_instance.unlink_pipeline_from_project(
            path_params=path_params,
        )
    except icasdk.ApiException as e:
        print("Exception when calling ProjectPipelineApi->unlink_pipeline_from_project: %s\n" % e)
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
projectId | ProjectIdSchema | | 
pipelineId | PipelineIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PipelineIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#unlink_pipeline_from_project.ApiResponseFor204) | The pipeline is successfully unlinked from the project.
default | [ApiResponseForDefault](#unlink_pipeline_from_project.ApiResponseForDefault) | A problem occurred.

#### unlink_pipeline_from_project.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### unlink_pipeline_from_project.ApiResponseForDefault
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

