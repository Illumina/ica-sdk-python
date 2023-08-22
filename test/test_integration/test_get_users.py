import icasdk
from icasdk.apis.tags import user_api
from icasdk.model.user_list import UserList
from icasdk.model.problem import Problem
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
        api_instance = user_api.UserApi(api_client)

        # example passing only optional values
        query_params = {}
        try:
            # Retrieve a list of users.
            api_response = api_instance.get_users(
                query_params=query_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling UserApi->get_users: %s\n" % e)

        items = api_response.body["items"]
        userList = []
        for i in items:
            userList.append(i.get_item_oapg("id"))
            pprint(i.get_item_oapg("id"))
        assert "47793c21-75a6-3aa8-8147-81b354d0af4d" in userList
        assert api_response.response.status == 200
