import os
from dotenv import load_dotenv
import icasdk
from icasdk.apis.tags import (
    token_api,
    project_api,
    analysis_storage_api,
    project_pipeline_api,
)
from icasdk import ApiException
from icasdk.model.create_nextflow_pipeline import CreateNextflowPipeline

load_dotenv()
host = "https://ica.illumina.com/ica/rest"

# Set API_KEY as an environment variable
# It is best practice to exchange the API key with a JWT
token_response = token_api.CreateJwtToken(
    api_client=icasdk.ApiClient(
        icasdk.Configuration(
            host=host,
            api_key={"ApiKeyAuth": os.getenv("APIKEY")},
        )
    )
).create_jwt_token()
jwt = token_response.body.get_item_oapg("token")

# See configuration.py for a list of all supported configuration parameters.
configuration = icasdk.Configuration(
    host=host,
    access_token=jwt,
)

# Enter a context with an instance of the API client
with icasdk.ApiClient(configuration) as api_client:
    # Retrieve the list of projects.  The results are paged.
    # Find project with name "DRAGEN Dev"
    # The program will halt at this point if the project is not found
    # project_name = "DRAGEN Dev"
    project_name = "emedgene-demo"
    project_api_client = project_api.ProjectApi(api_client)
    next_page_token = ""
    while True:
        projects_response = project_api_client.get_projects(
            query_params={
                "search": project_name,
                "pageToken": next_page_token,
            },
        )
        print(projects_response)
        project_id = next(
            (
                project.id
                for project in projects_response.body["items"]
                if project.name == project_name
            ),
            None,
        )
        if project_id is not None:
            break

        next_page_token = projects_response.body.get_item_oapg("nextPageToken")
        if not next_page_token:
            raise ValueError(f'Project with name "{project_name}" not found')

    # Find the ID for the small storage size
    storage_options = analysis_storage_api.AnalysisStorageApi(
        api_client
    ).get_analysis_storage_options()
    small_storage_id = next(
        storage.id
        for storage in storage_options.body["items"]
        if storage.name == "Small"
    )

    # Deploy the sample pipeline
    # If the pipeline with the same name already exists, we'll get a 409
    pipeline_code = "icasdk Sample DRAGEN pipeline"
    try:
        with open("sample-dragen.nf", "rb") as main_wf_file, open(
            "sample-dragen.xml", "rb"
        ) as xml_file:
            pipeline = (
                project_pipeline_api.CreateNextflowPipeline(api_client)
                .create_nextflow_pipeline(
                    body=CreateNextflowPipeline(
                        code=pipeline_code,
                        description="Sample DRAGEN pipeline",
                        parametersXmlFile=xml_file,
                        mainNextflowFile=main_wf_file,
                        analysisStorageId=small_storage_id,
                    ),
                    path_params={"projectId": project_id},
                )
                .body.pipeline
            )
    except ApiException as e:
        if not e.status == 409:
            raise e

        project_pipelines = project_pipeline_api.ProjectPipelineApi(
            api_client
        ).get_project_pipelines(
            path_params={"projectId": project_id},
        )
        pipeline = next(
            p.pipeline
            for p in project_pipelines.body["items"]
            if p.pipeline.code == pipeline_code
        )

    print(pipeline)
