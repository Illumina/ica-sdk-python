import icasdk
from icasdk.apis.tags import sample_api
from icasdk.model.sample_paged_list import SamplePagedList
from icasdk.model.problem import Problem
from pprint import pprint
import os
from dotenv import load_dotenv


def test_sample_list():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")

    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = sample_api.SampleApi(api_client)

        # example passing only required values which don't have defaults set
        query_params = {
            "region": "c39b1feb-3e94-4440-805e-45e0c76462bf",
        }
        try:
            # Retrieve a list of samples.
            api_response = api_instance.get_samples(
                query_params=query_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling SampleApi->get_samples: %s\n" % e)

        items = api_response.body["items"]
        sampleList = []
        for i in items:
            sampleList.append(i.get_item_oapg("id"))
            pprint(i.get_item_oapg("id"))

        assert "038eeae2-6e56-43fd-9973-0d2da84283b7" in sampleList
        assert api_response.response.status == 200
