# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import icasdk
from icasdk.paths.api_projects_project_id_data_update_batch_batch_id_items_item_id import get  # noqa: E501
from icasdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiProjectsProjectIdDataUpdateBatchBatchIdItemsItemId(ApiTestMixin, unittest.TestCase):
    """
    ApiProjectsProjectIdDataUpdateBatchBatchIdItemsItemId unit test stubs
        Retrieve a project data update batch item.  # noqa: E501
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