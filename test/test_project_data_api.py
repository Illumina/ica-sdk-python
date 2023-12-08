# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p> 

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from icasdk.api.project_data_api import ProjectDataApi


class TestProjectDataApi(unittest.TestCase):
    """ProjectDataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectDataApi()

    def tearDown(self) -> None:
        pass

    def test_add_secondary_data(self) -> None:
        """Test case for add_secondary_data

        Add secondary data to data.
        """
        pass

    def test_archive_data(self) -> None:
        """Test case for archive_data

        Schedule this data for archival.
        """
        pass

    def test_complete_folder_upload_session(self) -> None:
        """Test case for complete_folder_upload_session

        Complete a trackable folder upload session.
        """
        pass

    def test_create_data_in_project(self) -> None:
        """Test case for create_data_in_project

        Create data in this project.
        """
        pass

    def test_create_download_url_for_data(self) -> None:
        """Test case for create_download_url_for_data

        Retrieve a download URL for this data.
        """
        pass

    def test_create_download_urls_for_data(self) -> None:
        """Test case for create_download_urls_for_data

        Retrieve download URLs for the data.
        """
        pass

    def test_create_folder_upload_session(self) -> None:
        """Test case for create_folder_upload_session

        Create a trackable folder upload session.
        """
        pass

    def test_create_inline_view_url_for_data(self) -> None:
        """Test case for create_inline_view_url_for_data

        Retrieve an URL for this data to use for inline view in a browser.
        """
        pass

    def test_create_temporary_credentials_for_data(self) -> None:
        """Test case for create_temporary_credentials_for_data

        Retrieve temporary credentials for this data.
        """
        pass

    def test_create_upload_url_for_data(self) -> None:
        """Test case for create_upload_url_for_data

        Retrieve an upload URL for this data.
        """
        pass

    def test_delete_data(self) -> None:
        """Test case for delete_data

        Schedule this data for deletion.
        """
        pass

    def test_get_data_eligible_for_linking(self) -> None:
        """Test case for get_data_eligible_for_linking

        Retrieve a list of data eligible for linking to the current project.
        """
        pass

    def test_get_folder_upload_session(self) -> None:
        """Test case for get_folder_upload_session

        Retrieve folder upload session details.
        """
        pass

    def test_get_non_sample_project_data(self) -> None:
        """Test case for get_non_sample_project_data

        Retrieve a list of project data not linked to a sample.
        """
        pass

    def test_get_project_data(self) -> None:
        """Test case for get_project_data

        Retrieve a project data.
        """
        pass

    def test_get_project_data_children(self) -> None:
        """Test case for get_project_data_children

        Retrieve the children of this data.
        """
        pass

    def test_get_project_data_list(self) -> None:
        """Test case for get_project_data_list

        Retrieve the list of project data.
        """
        pass

    def test_get_projects_linked_to_data(self) -> None:
        """Test case for get_projects_linked_to_data

        Retrieve a list of projects to which this data is linked.
        """
        pass

    def test_get_secondary_data(self) -> None:
        """Test case for get_secondary_data

        Retrieve a list of secondary data for data.
        """
        pass

    def test_link_data_to_project(self) -> None:
        """Test case for link_data_to_project

        Link data to this project.
        """
        pass

    def test_remove_secondary_data(self) -> None:
        """Test case for remove_secondary_data

        Remove secondary data from data.
        """
        pass

    def test_schedule_download_for_data(self) -> None:
        """Test case for schedule_download_for_data

        Schedule a download.
        """
        pass

    def test_unarchive_data(self) -> None:
        """Test case for unarchive_data

        Schedule this data for unarchival.
        """
        pass

    def test_unlink_data_from_project(self) -> None:
        """Test case for unlink_data_from_project

        Unlink data from this project.
        """
        pass

    def test_update_project_data(self) -> None:
        """Test case for update_project_data

        Update this project data.
        """
        pass


if __name__ == '__main__':
    unittest.main()
