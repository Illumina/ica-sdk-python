# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import icasdk
from icasdk.paths.api_reference_sets_reference_set_id_species import get  # noqa: E501
from icasdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiReferenceSetsReferenceSetIdSpecies(ApiTestMixin, unittest.TestCase):
    """
    ApiReferenceSetsReferenceSetIdSpecies unit test stubs
        Retrieve a list of species linked to the reference set.  # noqa: E501
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
