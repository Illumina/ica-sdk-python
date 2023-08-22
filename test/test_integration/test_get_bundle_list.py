import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
from icasdk.model.problem import Problem
from pprint import pprint
from icasdk.apis.tags import bundle_api
from icasdk.model.bundle_paged_list import BundlePagedList
import os
from dotenv import load_dotenv


def test_auth():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")

    # Enter a context with an instance of the API client
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = token_api.TokenApi(api_client)

        # example passing only optional values
        query_params = {
            "tenant": "ilmn-cci",
        }
        try:
            # Generate a JWT using an API-key, Basic Authentication or a psToken.
            api_response = api_instance.create_jwt_token(
                query_params=query_params,
            )
            pprint(api_response)
            jwt = api_response.body["token"]
        except icasdk.ApiException as e:
            pprint("Exception when calling TokenApi->create_jwt_token: %s\n" % e)

    configuration = icasdk.Configuration(
        host="https://ica.illumina.com/ica/rest", access_token=jwt
    )

    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = bundle_api.BundleApi(api_client)

        # example passing only optional values
        query_params = {"pageSize": "10"}
        try:
            # Retrieve a list of bundles.
            api_response = api_instance.get_bundles(
                query_params=query_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling BundleApi->get_bundles: %s\n" % e)

        items = api_response.body["items"]
        bundleList = []
        for i in items:
            bundleList.append(i.get_item_oapg("name"))
            pprint(i.get_item_oapg("name"))

    assert "Test_bundle_sharon" in bundleList
    assert api_response.response.status == 200
