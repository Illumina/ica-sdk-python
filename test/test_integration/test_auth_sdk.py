import icasdk
from icasdk.apis.tags import token_api
from icasdk.model.token import Token
from icasdk.model.problem import Problem
from pprint import pprint
from icasdk.apis.tags import storage_bundle_api
from icasdk.model.storage_bundle_list import StorageBundleList
from icasdk.apis.tags import project_api
from icasdk.model.create_project import CreateProject
from icasdk.model.project import Project
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

        api_instance = storage_bundle_api.StorageBundleApi(api_client)
        try:
            # Retrieve a list of storage bundles.
            api_response = api_instance.get_storage_bundles()
            pprint(api_response)
            items = api_response.body["items"]
            for i in items:
                if i.region.country.name == "United States":
                    pprint(f"storageBundleName:Id={i.entitlementName}:{i.id}")
                    pprint(f"regionName:Id={i.region.country.name}:{i.region.id}")
                    storageId = i.id
                    regionId = i.region.id

        except icasdk.ApiException as e:
            print(
                "Exception when calling StorageBundleApi->get_storage_bundles: %s\n" % e
            )

        assert api_response.response.status == 200
        assert regionId == "c39b1feb-3e94-4440-805e-45e0c76462bf"
