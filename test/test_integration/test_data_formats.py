import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
from icasdk.apis.tags import data_format_api
from icasdk.model.data_format_paged_list import DataFormatPagedList
from icasdk.model.problem import Problem
from pprint import pprint
import os
from dotenv import load_dotenv


def test_data_formats():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # The client must configure the authentication and authorization parameters
    # in accordance with the API server security policy.
    # Examples for each auth method are provided below, use the example that
    # satisfies your auth use case.

    # Configure API key authorization: ApiKeyAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")

    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

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
            # pprint(api_response)
            jwt = api_response.body["token"]
        except icasdk.ApiException as e:
            pprint("Exception when calling TokenApi->create_jwt_token: %s\n" % e)

    configuration = icasdk.Configuration(
        host="https://ica.illumina.com/ica/rest", access_token=jwt
    )

    # Enter a context with an instance of the API client
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = data_format_api.DataFormatApi(api_client)

        # example passing only optional values
        query_params = {"pageSize": "10"}
        try:
            # Retrieve a list of data formats.
            api_response = api_instance.get_data_formats(
                query_params=query_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling DataFormatApi->get_data_formats: %s\n" % e)

        items = api_response.body["items"]
        dataFormatsList = []
        for i in items:
            dataFormatsList.append(i.get_item_oapg("code"))
            pprint(i.get_item_oapg("code"))

        assert "BED" in dataFormatsList
        assert api_response.response.status == 200
