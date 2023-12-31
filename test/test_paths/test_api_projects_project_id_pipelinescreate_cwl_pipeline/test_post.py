# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import icasdk
from icasdk.paths.api_projects_project_id_pipelinescreate_cwl_pipeline import post  # noqa: E501
from icasdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiProjectsProjectIdPipelinescreateCwlPipeline(ApiTestMixin, unittest.TestCase):
    """
    ApiProjectsProjectIdPipelinescreateCwlPipeline unit test stubs
        Create a CWL pipeline within a project.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
