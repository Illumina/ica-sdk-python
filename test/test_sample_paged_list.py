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

from icasdk.models.sample_paged_list import SamplePagedList

class TestSamplePagedList(unittest.TestCase):
    """SamplePagedList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SamplePagedList:
        """Test SamplePagedList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SamplePagedList`
        """
        model = SamplePagedList()
        if include_optional:
            return SamplePagedList(
                items = [
                    icasdk.models.sample.Sample(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        name = '0', 
                        description = '0', 
                        tags = icasdk.models.sample_tag.SampleTag(
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
                                ], ), 
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
                        status = 'DELETED', 
                        metadata_valid = True, 
                        metadata = [
                            icasdk.models.metadata_field.MetadataField(
                                id = '', 
                                index = 56, 
                                name = '', 
                                field_type = 'TEXT', 
                                values = [
                                    ''
                                    ], 
                                group_values = [
                                    icasdk.models.metadata_field.MetadataField(
                                        id = '', 
                                        index = 56, 
                                        name = '', 
                                        field_type = 'TEXT', )
                                    ], )
                            ], 
                        sequencing_runs = [
                            icasdk.models.sequencing_run.SequencingRun(
                                id = '', 
                                instrument_run_id = '', 
                                name = '', )
                            ], )
                    ],
                next_page_token = '',
                remaining_records = 0,
                total_item_count = 0
            )
        else:
            return SamplePagedList(
                items = [
                    icasdk.models.sample.Sample(
                        id = '', 
                        time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        owner_id = '', 
                        tenant_id = '', 
                        tenant_name = '', 
                        name = '0', 
                        description = '0', 
                        tags = icasdk.models.sample_tag.SampleTag(
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
                                ], ), 
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
                        status = 'DELETED', 
                        metadata_valid = True, 
                        metadata = [
                            icasdk.models.metadata_field.MetadataField(
                                id = '', 
                                index = 56, 
                                name = '', 
                                field_type = 'TEXT', 
                                values = [
                                    ''
                                    ], 
                                group_values = [
                                    icasdk.models.metadata_field.MetadataField(
                                        id = '', 
                                        index = 56, 
                                        name = '', 
                                        field_type = 'TEXT', )
                                    ], )
                            ], 
                        sequencing_runs = [
                            icasdk.models.sequencing_run.SequencingRun(
                                id = '', 
                                instrument_run_id = '', 
                                name = '', )
                            ], )
                    ],
        )
        """

    def testSamplePagedList(self):
        """Test SamplePagedList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
