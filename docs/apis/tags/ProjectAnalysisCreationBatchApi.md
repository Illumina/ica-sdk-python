<a name="__pageTop"></a>
# icasdk.apis.tags.project_analysis_creation_batch_api.ProjectAnalysisCreationBatchApi

All URIs are relative to */ica/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_analysis_creation_batch**](#create_analysis_creation_batch) | **post** /api/projects/{projectId}/analysisCreationBatch | Create and start multiple analyses in batch.
[**get_analysis_creation_batch**](#get_analysis_creation_batch) | **get** /api/projects/{projectId}/analysisCreationBatch/{batchId} | Retrieve a analysis creation batch.
[**get_analysis_creation_batch_item**](#get_analysis_creation_batch_item) | **get** /api/projects/{projectId}/analysisCreationBatch/{batchId}/items | Retrieve a list of analysis creation batch items.
[**get_analysis_creation_batch_item1**](#get_analysis_creation_batch_item1) | **get** /api/projects/{projectId}/analysisCreationBatch/{batchId}/items/{itemId} | Retrieve a analysis creation batch item.

# **create_analysis_creation_batch**
<a name="create_analysis_creation_batch"></a>
> AnalysisCreationBatch create_analysis_creation_batch(project_idcreate_analysis_creation_batch)

Create and start multiple analyses in batch.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_analysis_creation_batch_api
from icasdk.model.analysis_creation_batch import AnalysisCreationBatch
from icasdk.model.create_analysis_creation_batch import CreateAnalysisCreationBatch
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
    api_instance = project_analysis_creation_batch_api.ProjectAnalysisCreationBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
    }
    header_params = {
    }
    body = CreateAnalysisCreationBatch(
        cwl_items=[
            CreateCwlAnalysis(
                user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
                pipeline_id="pipeline_id_example",
                tags=AnalysisTag(
                    technical_tags=[
                        "technical_tags_example"
                    ],
                    user_tags=[
                        "user_tags_example"
                    ],
                    reference_tags=[
                        "reference_tags_example"
                    ],
                ),
                activation_code_detail_id="activation_code_detail_id_example",
                analysis_storage_id="analysis_storage_id_example",
                output_parent_folder_id="output_parent_folder_id_example",
                analysis_output=[
                    AnalysisOutputMapping(
                        source_path="source_path_example",
                        type="FILE",
                        target_project_id="target_project_id_example",
                        target_path="target_path_example",
                        action_on_exist="action_on_exist_example",
                    )
                ],
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
                            type="s3",
                            mount_path="mount_path_example",
                            s3_details=AnalysisS3DataDetails(
                                storage_credentials_id="storage_credentials_id_example",
                            ),
                        )
                    ],
                ),
            )
        ],
        nextflow_items=[
            CreateNextflowAnalysis(
                user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
                pipeline_id="pipeline_id_example",
                tags=AnalysisTag(),
                activation_code_detail_id="activation_code_detail_id_example",
                analysis_storage_id="analysis_storage_id_example",
                output_parent_folder_id="output_parent_folder_id_example",
,
                analysis_input=NextflowAnalysisInput(
                    inputs=[
                        AnalysisDataInput(
                            parameter_code="parameter_code_example",
,
,
,
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
        ],
    )
    try:
        # Create and start multiple analyses in batch.
        api_response = api_instance.create_analysis_creation_batch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->create_analysis_creation_batch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
    }
    header_params = {
        'Idempotency-Key': "Idempotency-Key_example",
    }
    body = CreateAnalysisCreationBatch(
        cwl_items=[
            CreateCwlAnalysis(
                user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
                pipeline_id="pipeline_id_example",
                tags=AnalysisTag(
                    technical_tags=[
                        "technical_tags_example"
                    ],
                    user_tags=[
                        "user_tags_example"
                    ],
                    reference_tags=[
                        "reference_tags_example"
                    ],
                ),
                activation_code_detail_id="activation_code_detail_id_example",
                analysis_storage_id="analysis_storage_id_example",
                output_parent_folder_id="output_parent_folder_id_example",
                analysis_output=[
                    AnalysisOutputMapping(
                        source_path="source_path_example",
                        type="FILE",
                        target_project_id="target_project_id_example",
                        target_path="target_path_example",
                        action_on_exist="action_on_exist_example",
                    )
                ],
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
                            type="s3",
                            mount_path="mount_path_example",
                            s3_details=AnalysisS3DataDetails(
                                storage_credentials_id="storage_credentials_id_example",
                            ),
                        )
                    ],
                ),
            )
        ],
        nextflow_items=[
            CreateNextflowAnalysis(
                user_reference="26bUUGjjNSwg0_bs9ZayIM/dgN/b6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz-5awxoFZxHzs6ED-kjUSnTINkYPUndNl8pmPg5K897Fu1JEFj9R1_dz/rEoBi0LnU8SsOWJ7wYrczi/Qdt8mVLxbg4bCLrLBcmXxWQK6MzKSg5jphei0IfRRwpnT_Z-qKa_YppZepezJ0-VmLSUTLYyW- e_jxxzpBvw-y P/SI-13 AOsiPRVvnXrDhh58EJzzOxprDzE3pjHRAkK7vI7/jcoPqzNk YKJOXJ2zkgYnmU-hV4pJhQ7dhTAGxjARc6SZKg2qV/ hA054g00j8CXRM4JZgexx5/BmiUdb8V-5tS7Ce-8OP8jM6Q/ap ieHoJL0cOHxhIz6IzRjPiSbv46JLcKaA-xTwLJcAkoNQxJsCUIkorO-2KAnnTOE8M6xmSejA6BGR RDxxWc493QsJ JFt/rxtNb3BtpHGNB33FSli/EaSDC3Jwlo9Aq-OZySuGXBwuNL5ICjOL uxZFN7oEXv3Rjr7mZXbY7cFU6HPiDV aM8XFtx5ef7XxGahEx5as4igHCaW/gfGuN6Yogo9e2fmFQ_q_V0iz1l6lakAtMD7gXmnBhySbG7coPhWOlWnLvrLZaxa78JI_LGepDuQ3z-LtIx RE8z6ZbHjz/3coUV uT/EXw3Z8KLTvaqhteQpbwYU8rf85eyxCXQ02l2UfQbP/Hwb TbI1I6mS 9V-ofBBak wevR6F 37RS4Mqp-z9OYCpSjEqZEdbOOqMNkk0MEG4PgSZp-tY7nzp2V09rLuCvfKd3/B7Nke4pyLFXi20uVuBIVQWxeziEmPj4-KIZ4EBDYGMeHwlQHgxMV_coQzDZPhSAcDWSu58NayafWzmTt-P7RTuj3iloSmvq6ptM/paqws8RfvaYMfrqa8yWUb/aew8fGzxL8UBpf4IYjQxCBv0aEqODMs6 __HvAARQCZ_HKqroXyt6-Y8imaC5It9ZEZjIoZP9V1EjbA-tFQv/KOFpHUcVNnqDdEconiUhJ/_OYqv01dQetO3oDTHSQdhLouT7merxKTcqNMpXfpU5ktnd4BBULIW0N/GhiW92gAEui/l WoiEW-tzti/9q3K407VNjp2Rdt_M_wxbjDN svNTMlZscMPUeqTE205sTZIkhsadNbiDH3R9hn/97bNktDzITop4y58kMdi7sEjYIZXQNI/G2UN7cFEvraG_8ul060s0W5myfNUsZOAfyRSKwumr7vrmbObYZ5LLOTkAJpJ6yD/EyKvzp oyT1iV44YK Q7W9XH_ nC87n1lMXx/cpcof84rc bTU20M2sFqt4zswj63S37gymcb35PFmFooUEItJ/WXmmb6rN-PG7CfVVrIXdUuyma63xZJQfyqFaad9jaJKwsaFZawt9CZCsgO_EkphsT/YD6 2t z_dodcIO0StQgTXeyp0Q-9qUn4jz1sIzDHdZi5DAKyeNjBARo-Dde72ZQ7rgUiF6NuAm_ZXdh 6NvD08O/uXF_iMcrZ0AkcxL21NwNNfADepMfPI jxbyGRU9VFh-_a9Mbcva1MSFLSU/GAcLlmJPzj1b/En KXp2ZJ1qP6EIAQRw6KWw-PSWFS0LzB0tz6JsM zfsuuNyQ1F qNTmvGd/34AbRwr1Mi1qq8Bv/7r73NXsLH6lkp_YwgeBZkfv7aEST19XJTe9 4t GIqXuFdD/054gT-SQFzTGrV3v TunXGLysUh_by7pmMGuKPyyeSFxct6Ze7099nRsM3R50i8YYD7uU6_-V/RO7VbVfLxqbCc-GimutTgMtTfBOiI07gLv8fxp8Rrvb2oVixDwL_5GL/dkyb0ofYJLarfJrS4gkeTAfK5NMnpgtwWLpKWVb8A/uQa TKwyJvJPBgILfXHpRfA79W9rCcVEcc1VmOZvW3--sp_E2t2terN4_2lcppBwgjIIFpE/9wjR SU K0GOwW4T/aO1NV6_Hx-5jhuPYUigmskjs38qptZPjGbQcMS6bq4jio6/n_hxYgCm- Z/K_7Ms5LyP8NoYNVF5v/C_I7qzU/pSP39e4y_L 2jAgjSpNK_48uV-MZ7CZL92Y/TDLRif4BX0k_kxk-VTaov2mlM18SfVTJ/mcMNVIO85230RBh-y9g8MNnnvGKT10t-mI5XH9biew58zTl0rQVIApvKA eQe3wv SD86JI2WO4rz8dSltvVqfei/m5FrnEpLvFqwhHFvdn0kEWtwPAhULVh_u/c  m 15yE3/jO3gKaP YHCaCFHZkWsh-mLTR_p_ZhJXuOoIsNHZsK m5ntCxGzmy4lVW_PKmo 4vtEAhOm289Yqnh43gtmE0DcSlXRhP/iRTQHkAPGO AROE GYzP3aIBvIz2Du0PJgDeBXnU3IgkF7V-jBW/R9V8PHmR5UHiFYWfIRAHRUzlaQ_5fkL16fmprt8wmIyj95MZALC3mmE-9-9QIQ_TxYHnPGd129xGytHvWDBO-HWa9uog_gy/B_Lcv_NbdKzBHV0mHJ0otqw-2cVo74hoJwmXoaUvId-qA0zLPa/yNACHAPKtKgQ-wkE FxSQB6am1_36v_4sO/L0 obeH_A5Q g0U8nnM/tLSIw h_9TVGO7HSAcUt2jm2mJ6jxIaRYSQHPbXmRPRzaWrmwaKy4EMWPwbc-aU2Q37XoigypCN/O vMz_s2eIdV-ysI6yTso6oV4n2icY_UqIX3aXe8/fjQVrmDXiXxxvBTvfg06jgn9-ScpKH8N5C4XWGVGRk3j37rxQmI4kwvKHhIKCAUvIkWH6jwZxFRo eIKF/u9HDcrUBkJ7XvQAc-6hPCiLNyumZW bZ1Z1lFtnk615uonsVXHfF05q0NRqj15TZJbNNeHStQMOuYC_jqdm9E9SG W_klzb/D/EIYyIete7WHGdGvaz8OlgB8y7yFT3urhGfXNdaf9LPJpeol/Hsm_twH5CZ0hw5E79TYBg5mTcvHosbmds0/lnttAjUMBqupVLK3x4 0AG976YmWGXzKcfMwo/AJe6AqMxeiI54JCwm88akvPHFEeT/B2_DFbeoWsodas1SE0ZbMSAutkOh5Xxm5JinIE-HSc3Uum5CXQM8IAqgV7Pt7UP7R-a-gxq3pkrhbyaL /g06Y18ROfY0YdRY3jzlcCRRc0YCrW8XRt5tBgOBd9I6/WfODawxODTr6XaLBZ4N4HcKJ0/9/176mYQK5G5Zg_-QRvAnzbzYh01qrNB/0OPLkLvQwJMAZYcIIuHLVBKQgB0tiFZAgCaX_xRaJdoCvlRQ2NFmqxndmXhZUKursXMGxzxNhAE-TRB8qkmv3x3zsY/hWxhBU-WrXobNN/UrgSnP/Hqo0hrfoM/2nH G5cT7PUzahLIwtoU8svwt-H5quoR L8lSHdFBrWE3qxdnl3KF6G9CqDK1MEEUL/z_3v2OEgVjFWE0PvPA tgxkNhx5gRDEgjBNW",
                pipeline_id="pipeline_id_example",
                tags=AnalysisTag(),
                activation_code_detail_id="activation_code_detail_id_example",
                analysis_storage_id="analysis_storage_id_example",
                output_parent_folder_id="output_parent_folder_id_example",
,
                analysis_input=NextflowAnalysisInput(
                    inputs=[
                        AnalysisDataInput(
                            parameter_code="parameter_code_example",
,
,
,
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
        ],
    )
    try:
        # Create and start multiple analyses in batch.
        api_response = api_instance.create_analysis_creation_batch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->create_analysis_creation_batch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndIlluminaV3json] | required |
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
[**CreateAnalysisCreationBatch**](../../models/CreateAnalysisCreationBatch.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Idempotency-Key | IdempotencyKeySchema | | optional

# IdempotencyKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
201 | [ApiResponseFor201](#create_analysis_creation_batch.ApiResponseFor201) | The analyses are scheduled for creation.
default | [ApiResponseForDefault](#create_analysis_creation_batch.ApiResponseForDefault) | A problem occurred.

#### create_analysis_creation_batch.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalysisCreationBatch**](../../models/AnalysisCreationBatch.md) |  | 


#### create_analysis_creation_batch.ApiResponseForDefault
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

# **get_analysis_creation_batch**
<a name="get_analysis_creation_batch"></a>
> AnalysisCreationBatch get_analysis_creation_batch(project_idbatch_id)

Retrieve a analysis creation batch.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_analysis_creation_batch_api
from icasdk.model.analysis_creation_batch import AnalysisCreationBatch
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
    api_instance = project_analysis_creation_batch_api.ProjectAnalysisCreationBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
    }
    try:
        # Retrieve a analysis creation batch.
        api_response = api_instance.get_analysis_creation_batch(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch: %s\n" % e)
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
batchId | BatchIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analysis_creation_batch.ApiResponseFor200) | The analysis creation batch is successfully retrieved.
default | [ApiResponseForDefault](#get_analysis_creation_batch.ApiResponseForDefault) | A problem occurred.

#### get_analysis_creation_batch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalysisCreationBatch**](../../models/AnalysisCreationBatch.md) |  | 


#### get_analysis_creation_batch.ApiResponseForDefault
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

# **get_analysis_creation_batch_item**
<a name="get_analysis_creation_batch_item"></a>
> AnalysisCreationBatchItemPagedList get_analysis_creation_batch_item(project_idbatch_id)

Retrieve a list of analysis creation batch items.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_analysis_creation_batch_api
from icasdk.model.analysis_creation_batch_item_paged_list import AnalysisCreationBatchItemPagedList
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
    api_instance = project_analysis_creation_batch_api.ProjectAnalysisCreationBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
    }
    query_params = {
    }
    try:
        # Retrieve a list of analysis creation batch items.
        api_response = api_instance.get_analysis_creation_batch_item(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_item: %s\n" % e)

    # example passing only optional values
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
    }
    query_params = {
        'status': [
        "RUNNING"
    ],
        'pageOffset': "pageOffset_example",
        'pageToken': "pageToken_example",
        'pageSize': "pageSize_example",
        'sort': "sort_example",
    }
    try:
        # Retrieve a list of analysis creation batch items.
        api_response = api_instance.get_analysis_creation_batch_item(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_item: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/problem+json', 'application/vnd.illumina.v3+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
status | StatusSchema | | optional
pageOffset | PageOffsetSchema | | optional
pageToken | PageTokenSchema | | optional
pageSize | PageSizeSchema | | optional
sort | SortSchema | | optional


# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["RUNNING", "WAITING_RESOURCES", "SUCCEEDED", "FAILED", ] 

# PageOffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
projectId | ProjectIdSchema | | 
batchId | BatchIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analysis_creation_batch_item.ApiResponseFor200) | The list of analysis creation batch items is successfully retrieved.
default | [ApiResponseForDefault](#get_analysis_creation_batch_item.ApiResponseForDefault) | A problem occurred.

#### get_analysis_creation_batch_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalysisCreationBatchItemPagedList**](../../models/AnalysisCreationBatchItemPagedList.md) |  | 


#### get_analysis_creation_batch_item.ApiResponseForDefault
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

# **get_analysis_creation_batch_item1**
<a name="get_analysis_creation_batch_item1"></a>
> AnalysisCreationBatchItem get_analysis_creation_batch_item1(project_idbatch_iditem_id)

Retrieve a analysis creation batch item.

### Example

* Bearer (JWT) Authentication (JwtAuth):
* Api Key Authentication (ApiKeyAuth):
```python
import icasdk
from icasdk.apis.tags import project_analysis_creation_batch_api
from icasdk.model.problem import Problem
from icasdk.model.analysis_creation_batch_item import AnalysisCreationBatchItem
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
    api_instance = project_analysis_creation_batch_api.ProjectAnalysisCreationBatchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'projectId': "projectId_example",
        'batchId': "batchId_example",
        'itemId': "itemId_example",
    }
    try:
        # Retrieve a analysis creation batch item.
        api_response = api_instance.get_analysis_creation_batch_item1(
            path_params=path_params,
        )
        pprint(api_response)
    except icasdk.ApiException as e:
        print("Exception when calling ProjectAnalysisCreationBatchApi->get_analysis_creation_batch_item1: %s\n" % e)
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
batchId | BatchIdSchema | | 
itemId | ItemIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BatchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

# ItemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_analysis_creation_batch_item1.ApiResponseFor200) | The analysis creation batch item is successfully retrieved.
default | [ApiResponseForDefault](#get_analysis_creation_batch_item1.ApiResponseForDefault) | A problem occurred.

#### get_analysis_creation_batch_item1.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndIlluminaV3json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndIlluminaV3json
Type | Description  | Notes
------------- | ------------- | -------------
[**AnalysisCreationBatchItem**](../../models/AnalysisCreationBatchItem.md) |  | 


#### get_analysis_creation_batch_item1.ApiResponseForDefault
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

