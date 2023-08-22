# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import icasdk
from icasdk.paths.api_activation_codesfind_all_matching_for_nextflow import post  # noqa: E501
from icasdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiActivationCodesfindAllMatchingForNextflow(ApiTestMixin, unittest.TestCase):
    """
    ApiActivationCodesfindAllMatchingForNextflow unit test stubs
        Search all matching activation code details for a Nextflow pipeline.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200








if __name__ == '__main__':
    unittest.main()
