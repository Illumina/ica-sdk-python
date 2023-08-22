import icasdk
from icasdk.apis.tags import pipeline_api
from icasdk.model.problem import Problem
from icasdk.model.pipeline import Pipeline
from icasdk.model.pipeline_list import PipelineList
from icasdk.model.pipeline_configuration_parameter_list import (
    PipelineConfigurationParameterList,
)
from icasdk.model.pipeline_html_documentation import PipelineHtmlDocumentation
from icasdk.model.input_parameter_list import InputParameterList
from icasdk.model.reference_set_list import ReferenceSetList
from pprint import pprint

import os
from dotenv import load_dotenv


def test_get_pipeline_list():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pipeline_api.PipelineApi(api_client)

        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve a list of pipelines.
            api_response = api_instance.get_pipelines()
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling PipelineApi->get_pipelines: %s\n" % e)

        assert api_response.response.status == 200


def test_get_pipeline():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pipeline_api.PipelineApi(api_client)

        path_params = {
            "pipelineId": "1dbd4e0a-c30b-4096-a222-b4c1c8646087",
        }
        try:
            # Retrieve a list of pipelines.
            api_response = api_instance.get_pipeline(
                path_params=path_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)

        assert api_response.response.status == 200


def test_get_pipeline_input():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pipeline_api.PipelineApi(api_client)

        path_params = {
            "pipelineId": "1dbd4e0a-c30b-4096-a222-b4c1c8646087",
        }
        try:
            # Retrieve a list of pipelines.
            api_response = api_instance.get_pipeline_input_parameters(
                path_params=path_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling PipelineApi->get_pipeline_input_parameters: %s\n"
                % e
            )

        assert api_response.response.status == 200


def test_get_pipeline_configuration():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pipeline_api.PipelineApi(api_client)

        path_params = {
            "pipelineId": "1dbd4e0a-c30b-4096-a222-b4c1c8646087",
        }
        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve a list of pipelines.
            api_response = api_instance.get_pipeline_configuration_parameters(
                path_params=path_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling PipelineApi->get_pipeline_configuration_parameters: %s\n"
                % e
            )

        assert api_response.response.status == 200


def test_get_pipeline_reference_sets():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pipeline_api.PipelineApi(api_client)

        path_params = {
            "pipelineId": "1dbd4e0a-c30b-4096-a222-b4c1c8646087",
        }
        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve a list of pipelines.
            api_response = api_instance.get_pipeline_reference_sets(
                path_params=path_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling PipelineApi->get_pipeline_reference_sets: %s\n"
                % e
            )

        assert api_response.response.status == 200


def test_get_pipeline_documentation():
    # Defining the host is optional and defaults to /ica/rest
    # See configuration.py for a list of all supported configuration parameters.
    load_dotenv()
    configuration = icasdk.Configuration(host="https://ica.illumina.com/ica/rest")

    # Configure HTTP basic authorization: BasicAuth
    configuration.api_key["ApiKeyAuth"] = os.getenv("APIKEY")
    with icasdk.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pipeline_api.PipelineApi(api_client)

        path_params = {
            "pipelineId": "1dbd4e0a-c30b-4096-a222-b4c1c8646087",
        }
        # example, this endpoint has no required or optional parameters
        try:
            # Retrieve a list of pipelines.
            api_response = api_instance.get_pipeline_html_documentation(
                path_params=path_params,
            )
            pprint(api_response)
        except icasdk.ApiException as e:
            print(
                "Exception when calling PipelineApi->get_pipeline_html_documentation: %s\n"
                % e
            )

        assert api_response.response.status == 200
