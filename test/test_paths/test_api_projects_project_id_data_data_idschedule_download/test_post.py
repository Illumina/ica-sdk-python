# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import icasdk
from icasdk.paths.api_projects_project_id_data_data_idschedule_download import post  # noqa: E501
from icasdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiProjectsProjectIdDataDataIdscheduleDownload(ApiTestMixin, unittest.TestCase):
    """
    ApiProjectsProjectIdDataDataIdscheduleDownload unit test stubs
        Schedule a download.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 0








if __name__ == '__main__':
    unittest.main()
