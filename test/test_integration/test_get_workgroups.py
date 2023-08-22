import icasdk
from icasdk.apis.tags import workgroup_api
from icasdk.model.problem import Problem
from icasdk.model.workgroup_list import WorkgroupList
from pprint import pprint

import os
from dotenv import load_dotenv


def test_user_list():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")

    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = workgroup_api.WorkgroupApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve a list of workgroups.
            api_response = api_instance.get_workgroups()
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling WorkgroupApi->get_workgroups: %s\n" % e)

        items = api_response.body["items"]
        workgroupList = []
        for i in items:
            workgroupList.append(i.get_item_oapg("id"))
            pprint(i.get_item_oapg("id"))
        assert "00f97a19-02c3-334d-9ee1-083a65901406" in workgroupList
        assert api_response.response.status == 200
