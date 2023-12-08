# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p> 

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from icasdk.models.cwl_analysis_input import CwlAnalysisInput

class TestCwlAnalysisInput(unittest.TestCase):
    """CwlAnalysisInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CwlAnalysisInput:
        """Test CwlAnalysisInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CwlAnalysisInput`
        """
        model = CwlAnalysisInput()
        if include_optional:
            return CwlAnalysisInput(
                object_type = 'STRUCTURED',
                inputs = [
                    icasdk.models.analysis_data_input.AnalysisDataInput(
                        parameter_code = '', 
                        data_ids = [
                            ''
                            ], 
                        mounts = [
                            icasdk.models.analysis_input_data_mount.AnalysisInputDataMount(
                                data_id = '', 
                                mount_path = '', )
                            ], 
                        external_data = [
                            icasdk.models.analysis_input_external_data.AnalysisInputExternalData(
                                url = '', 
                                type = 'http', 
                                mount_path = '', 
                                s3_details = icasdk.models.analysis_s3_data_details.AnalysisS3DataDetails(
                                    storage_credentials_id = '', ), )
                            ], )
                    ],
                parameters = [
                    icasdk.models.analysis_parameter_input.AnalysisParameterInput(
                        code = '', 
                        value = '', 
                        multi_value = [
                            ''
                            ], )
                    ],
                reference_data_parameters = [
                    icasdk.models.analysis_reference_data_parameter.AnalysisReferenceDataParameter(
                        parameter_code = '', 
                        reference_data_id = '', )
                    ],
                input_json = '',
                data_ids = [
                    ''
                    ],
                mounts = [
                    icasdk.models.analysis_input_data_mount.AnalysisInputDataMount(
                        data_id = '', 
                        mount_path = '', )
                    ],
                external_data = [
                    icasdk.models.analysis_input_external_data.AnalysisInputExternalData(
                        url = '', 
                        type = 'http', 
                        mount_path = '', 
                        s3_details = icasdk.models.analysis_s3_data_details.AnalysisS3DataDetails(
                            storage_credentials_id = '', ), )
                    ]
            )
        else:
            return CwlAnalysisInput(
                object_type = 'STRUCTURED',
                inputs = [
                    icasdk.models.analysis_data_input.AnalysisDataInput(
                        parameter_code = '', 
                        data_ids = [
                            ''
                            ], 
                        mounts = [
                            icasdk.models.analysis_input_data_mount.AnalysisInputDataMount(
                                data_id = '', 
                                mount_path = '', )
                            ], 
                        external_data = [
                            icasdk.models.analysis_input_external_data.AnalysisInputExternalData(
                                url = '', 
                                type = 'http', 
                                mount_path = '', 
                                s3_details = icasdk.models.analysis_s3_data_details.AnalysisS3DataDetails(
                                    storage_credentials_id = '', ), )
                            ], )
                    ],
                input_json = '',
        )
        """

    def testCwlAnalysisInput(self):
        """Test CwlAnalysisInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
