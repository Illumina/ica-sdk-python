import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
from icasdk.model.problem import Problem
from icasdk.apis.tags import analysis_storage_api
from icasdk.model.analysis_storage_list import AnalysisStorageList
from pprint import pprint

import os
from dotenv import load_dotenv


def test_analysis_storage_list():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")

    # Enter a context with an instance of the API client
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = analysis_storage_api.AnalysisStorageApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve the list of analysis storage options.
            api_response = api_instance.get_analysis_storage_options()
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling AnalysisStorageApi->get_analysis_storage_options: %s\n"
                % e
            )

        items = api_response.body["items"]
        analysisList = []
        for i in items:
            analysisList.append(i.get_item_oapg("name"))
            pprint(i.get_item_oapg("name"))

        assert "Small" in analysisList
        assert api_response.response.status == 200
