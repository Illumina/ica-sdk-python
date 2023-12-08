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

from icasdk.models.data import Data

class TestData(unittest.TestCase):
    """Data unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Data:
        """Test Data
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Data`
        """
        model = Data()
        if include_optional:
            return Data(
                id = '0',
                urn = '0',
                details = icasdk.models.data_details.DataDetails(
                    time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    creator_id = '', 
                    tenant_id = '', 
                    tenant_name = '', 
                    owning_project_id = '', 
                    owning_project_name = '', 
                    name = '', 
                    path = '', 
                    file_size_in_bytes = 56, 
                    status = 'PARTIAL', 
                    tags = icasdk.models.data_tag.DataTag(
                        technical_tags = [
                            ''
                            ], 
                        user_tags = [
                            ''
                            ], 
                        connector_tags = [
                            ''
                            ], 
                        run_in_tags = [
                            ''
                            ], 
                        run_out_tags = [
                            ''
                            ], 
                        reference_tags = [
                            ''
                            ], ), 
                    format = icasdk.models.data_format.DataFormat(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        code = '0', 
                        description = '0', 
                        mime_type = '0', ), 
                    data_type = 'FILE', 
                    object_e_tag = '', 
                    stored_for_the_first_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    region = icasdk.models.region.Region(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        code = '0', 
                        country = icasdk.models.country.Country(
                            id = '', 
                            time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            owner_id = '', 
                            tenant_id = '', 
                            tenant_name = '', 
                            code = '', 
                            name = '', 
                            region = '', ), 
                        city_name = '0', ), 
                    will_be_archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    will_be_deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    sequencing_run = icasdk.models.sequencing_run.SequencingRun(
                        id = '', 
                        instrument_run_id = '', 
                        name = '', ), )
            )
        else:
            return Data(
                id = '0',
        )
        """

    def testData(self):
        """Test Data"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
