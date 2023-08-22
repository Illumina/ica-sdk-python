# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import icasdk
from icasdk.paths.api_projects_project_id_pipelines_pipeline_id_reference_sets import get  # noqa: E501
from icasdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiProjectsProjectIdPipelinesPipelineIdReferenceSets(ApiTestMixin, unittest.TestCase):
    """
    ApiProjectsProjectIdPipelinesPipelineIdReferenceSets unit test stubs
        Retrieve the reference sets of a project pipeline.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
