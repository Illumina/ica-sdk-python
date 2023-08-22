import icasdk
from icasdk.apis.tags import storage_credentials_api
from icasdk.model.problem import Problem
from icasdk.model.storage_credential_list import StorageCredentialList
from pprint import pprint

import os
from dotenv import load_dotenv


def test_storage_credential_list():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = storage_credentials_api.StorageCredentialsApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve a list of storage credentials.
            api_response = api_instance.get_storage_credentials()
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling StorageCredentialsApi->get_storage_credentials: %s\n"
                % e
            )

        items = api_response.body["items"]
        credList = []
        for i in items:
            credList.append(i.get_item_oapg("id"))
            pprint(i.get_item_oapg("id"))
        assert "7f087458-42d3-4ca2-bc96-1de1dbdc0fd9" in credList
        assert api_response.response.status == 200
