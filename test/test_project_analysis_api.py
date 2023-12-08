# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p> 

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from icasdk.api.project_analysis_api import ProjectAnalysisApi


class TestProjectAnalysisApi(unittest.TestCase):
    """ProjectAnalysisApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectAnalysisApi()

    def tearDown(self) -> None:
        pass

    def test_abort_analysis(self) -> None:
        """Test case for abort_analysis

        Abort an analysis.
        """
        pass

    def test_create_cwl_analysis(self) -> None:
        """Test case for create_cwl_analysis

        Create and start an analysis for a CWL pipeline.
        """
        pass

    def test_create_nextflow_analysis(self) -> None:
        """Test case for create_nextflow_analysis

        Create and start an analysis for a Nextflow pipeline.
        """
        pass

    def test_get_analyses(self) -> None:
        """Test case for get_analyses

        Retrieve the list of analyses.
        """
        pass

    def test_get_analysis(self) -> None:
        """Test case for get_analysis

        Retrieve an analysis.
        """
        pass

    def test_get_analysis_configurations(self) -> None:
        """Test case for get_analysis_configurations

        Retrieve the configurations of an analysis.
        """
        pass

    def test_get_analysis_inputs(self) -> None:
        """Test case for get_analysis_inputs

        Retrieve the inputs of an analysis.
        """
        pass

    def test_get_analysis_outputs(self) -> None:
        """Test case for get_analysis_outputs

        Retrieve the outputs of an analysis. The list might be incomplete if a folder contains too many output files, but all the data can always be retrieved through the GET data endpoint.
        """
        pass

    def test_get_analysis_steps(self) -> None:
        """Test case for get_analysis_steps

        Retrieve the individual steps of an analysis.
        """
        pass

    def test_get_cwl_input_json(self) -> None:
        """Test case for get_cwl_input_json

        Retrieve the input json of a CWL analysis.
        """
        pass

    def test_get_cwl_output_json(self) -> None:
        """Test case for get_cwl_output_json

        Retrieve the output json of a CWL analysis.
        """
        pass

    def test_get_raw_analysis_output(self) -> None:
        """Test case for get_raw_analysis_output

        Retrieve the raw output of an analysis.
        """
        pass

    def test_update_analysis(self) -> None:
        """Test case for update_analysis

        Update an analysis.
        """
        pass


if __name__ == '__main__':
    unittest.main()
