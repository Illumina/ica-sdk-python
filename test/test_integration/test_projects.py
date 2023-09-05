import icasdk
from icasdk.apis.tags import project_api
from icasdk.model.project_paged_list import ProjectPagedList
from icasdk.model.problem import Problem
from pprint import pprint

import os
from dotenv import load_dotenv


def test_get_projects():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_api.ProjectApi(api_client)
        project_name = "emedgene-demo"
        next_page_token = ""
        # example passing only optional values
        query_params = {
            "search": project_name,
            "pageToken": next_page_token,
        }
        try:
            # Retrieve a list of projects.
            api_response = api_instance.get_projects(query_params=query_params)
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling ProjectApi->get_projects: %s\n" % e)

        items = api_response.body["items"]
        projectList = []
        for i in items:
            projectList.append(i.get_item_oapg("id"))
            pprint(i.get_item_oapg("id"))

        assert "2fab46b1-5930-476b-94c7-010f8d1fb3f3" in projectList
        assert api_response.response.status == 200
