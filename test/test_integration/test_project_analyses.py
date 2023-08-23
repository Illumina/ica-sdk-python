import icasdk
from icasdk.apis.tags import project_analysis_api

from icasdk.model.analysis import Analysis
from icasdk.model.analysis_paged_list import AnalysisPagedList
from icasdk.model.execution_configuration_list import ExecutionConfigurationList
from icasdk.model.analysis_input_list import AnalysisInputList
from icasdk.model.analysis_output_list import AnalysisOutputList
from icasdk.model.analysis_step_list import AnalysisStepList
from icasdk.model.cwl_analysis_input_json import CwlAnalysisInputJson
from icasdk.model.cwl_analysis_output_json import CwlAnalysisOutputJson
from icasdk.model.problem import Problem

from pprint import pprint

import os
from dotenv import load_dotenv


def test_get_analyses():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
        }
        query_params = {}
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_analyses(
                path_params=path_params,
                query_params=query_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling ProjectAnalysisApi->get_analyses: %s\n" % e)
        assert api_response.response.status == 200


def test_get_analysis():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "29a55b38-1726-4038-bd2e-131d72475d63",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_analysis(
                path_params=path_params, skip_deserialization=True
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling ProjectAnalysisApi->get_analysis: %s\n" % e)
        assert api_response.response.status == 200


def test_get_analysis_configurations():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "29a55b38-1726-4038-bd2e-131d72475d63",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_analysis_configurations(
                path_params=path_params
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling ProjectAnalysisApi->get_analysis_configurations: %s\n"
                % e
            )
        assert api_response.response.status == 200


def test_get_analysis_inputs():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "29a55b38-1726-4038-bd2e-131d72475d63",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_analysis_inputs(path_params=path_params)
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling ProjectAnalysisApi->get_analysis_inputs: %s\n"
                % e
            )
        assert api_response.response.status == 200


def test_get_analysis_outputs():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "29a55b38-1726-4038-bd2e-131d72475d63",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_analysis_outputs(path_params=path_params)
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling ProjectAnalysisApi->get_analysis_outputs: %s\n"
                % e
            )
        assert api_response.response.status == 200


def test_get_analysis_steps():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "29a55b38-1726-4038-bd2e-131d72475d63",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_analysis_steps(path_params=path_params)
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling ProjectAnalysisApi->get_analysis_steps: %s\n"
                % e
            )
        assert api_response.response.status == 200


def test_get_cwl_input_json():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "db34d08d-e5d3-47a9-84d2-0ef6e99ba03d",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_cwl_input_json(path_params=path_params)
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling ProjectAnalysisApi->get_cwl_input_json: %s\n"
                % e
            )
        assert api_response.response.status == 200


def test_get_cwl_output_json():
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = project_analysis_api.ProjectAnalysisApi(api_client)

        # example passing only required values which don't have defaults set
        path_params = {
            "projectId": "ad9111ca-f885-45f6-b2ef-e1bf339a32ef",
            "analysisId": "db34d08d-e5d3-47a9-84d2-0ef6e99ba03d",
        }
        try:
            # Retrieve the list of analyses.
            api_response = api_instance.get_cwl_output_json(path_params=path_params)
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling ProjectAnalysisApi->get_cwl_output_json: %s\n"
                % e
            )
        assert api_response.response.status == 200
