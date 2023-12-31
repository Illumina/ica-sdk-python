# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p>   # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from icasdk.paths.api_projects_project_id_samples_sample_id_metadata_metadata_model_id.post import AddMetadataModelToSample
from icasdk.paths.api_projects_project_id_samples_sample_idcomplete.post import CompleteProjectSample
from icasdk.paths.api_projects_project_id_samples.post import CreateSampleInProject
from icasdk.paths.api_projects_project_id_samples_sample_iddelete_deep.post import DeepDeleteSample
from icasdk.paths.api_projects_project_id_samples_sample_iddelete_unlink.post import DeleteAndUnlinkSample
from icasdk.paths.api_projects_project_id_samples_sample_iddelete_with_input.post import DeleteSampleWithInput
from icasdk.paths.api_projects_project_id_samples_sample_id.get import GetProjectSample
from icasdk.paths.api_projects_project_id_samples_sample_id_analyses.get import GetProjectSampleAnalyses
from icasdk.paths.api_projects_project_id_samplessearch.post import GetProjectSamples
from icasdk.paths.api_projects_project_id_samples_sample_id_projects.get import GetProjectsForSample
from icasdk.paths.api_projects_project_id_samples_sample_id_data.get import GetSampleDataList
from icasdk.paths.api_projects_project_id_samples_sample_id_history.get import GetSampleHistory
from icasdk.paths.api_projects_project_id_samples_sample_id_metadata_field_field_id.get import GetSampleMetadataField
from icasdk.paths.api_projects_project_id_samples_sample_id_metadata_field_id_field_count.get import GetSampleMetadataFieldCount
from icasdk.paths.api_projects_project_id_samples_sample_id_data_data_id.post import LinkDataToSample
from icasdk.paths.api_projects_project_id_samples_sample_id.post import LinkSampleToProject
from icasdk.paths.api_projects_project_id_samples_sample_iddelete_mark.post import MarkSampleDeleted
from icasdk.paths.api_projects_project_id_samples_sample_id_data_data_idunlink.post import UnlinkDataFromSample
from icasdk.paths.api_projects_project_id_samples_sample_idunlink.post import UnlinkSampleFromProject
from icasdk.paths.api_projects_project_id_samples_sample_id.put import UpdateProjectSample
from icasdk.paths.api_projects_project_id_samples_sample_id_metadataupdate_fields.post import UpdateSampleMetadataFields


class ProjectSampleApi(
    AddMetadataModelToSample,
    CompleteProjectSample,
    CreateSampleInProject,
    DeepDeleteSample,
    DeleteAndUnlinkSample,
    DeleteSampleWithInput,
    GetProjectSample,
    GetProjectSampleAnalyses,
    GetProjectSamples,
    GetProjectsForSample,
    GetSampleDataList,
    GetSampleHistory,
    GetSampleMetadataField,
    GetSampleMetadataFieldCount,
    LinkDataToSample,
    LinkSampleToProject,
    MarkSampleDeleted,
    UnlinkDataFromSample,
    UnlinkSampleFromProject,
    UpdateProjectSample,
    UpdateSampleMetadataFields,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
