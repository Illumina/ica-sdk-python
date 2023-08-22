import typing_extensions

from icasdk.paths import PathValues
from icasdk.apis.paths.api_analysis_storages import ApiAnalysisStorages
from icasdk.apis.paths.api_bundles import ApiBundles
from icasdk.apis.paths.api_bundles_bundle_id import ApiBundlesBundleId
from icasdk.apis.paths.api_bundles_bundle_idrelease import ApiBundlesBundleIdrelease
from icasdk.apis.paths.api_bundles_bundle_id_terms_of_use import ApiBundlesBundleIdTermsOfUse
from icasdk.apis.paths.api_bundles_bundle_id_terms_of_usenew import ApiBundlesBundleIdTermsOfUsenew
from icasdk.apis.paths.api_bundles_bundle_iddeprecate import ApiBundlesBundleIddeprecate
from icasdk.apis.paths.api_bundles_bundle_id_data import ApiBundlesBundleIdData
from icasdk.apis.paths.api_bundles_bundle_id_data_data_id import ApiBundlesBundleIdDataDataId
from icasdk.apis.paths.api_bundles_bundle_id_pipelines import ApiBundlesBundleIdPipelines
from icasdk.apis.paths.api_bundles_bundle_id_pipelines_pipeline_id import ApiBundlesBundleIdPipelinesPipelineId
from icasdk.apis.paths.api_bundles_bundle_id_samples import ApiBundlesBundleIdSamples
from icasdk.apis.paths.api_bundles_bundle_id_samples_sample_id import ApiBundlesBundleIdSamplesSampleId
from icasdk.apis.paths.api_bundles_bundle_id_tools import ApiBundlesBundleIdTools
from icasdk.apis.paths.api_bundles_bundle_id_tools_eligible_for_linking import ApiBundlesBundleIdToolsEligibleForLinking
from icasdk.apis.paths.api_bundles_bundle_id_tools_tool_id import ApiBundlesBundleIdToolsToolId
from icasdk.apis.paths.api_connectors import ApiConnectors
from icasdk.apis.paths.api_connectors_connector_id import ApiConnectorsConnectorId
from icasdk.apis.paths.api_connectors_connector_id_upload_rules import ApiConnectorsConnectorIdUploadRules
from icasdk.apis.paths.api_connectors_connector_id_upload_rules_upload_rule_id import ApiConnectorsConnectorIdUploadRulesUploadRuleId
from icasdk.apis.paths.api_connectors_connector_id_download_rules import ApiConnectorsConnectorIdDownloadRules
from icasdk.apis.paths.api_connectors_connector_id_download_rules_download_rule_id import ApiConnectorsConnectorIdDownloadRulesDownloadRuleId
from icasdk.apis.paths.api_connectors_connector_idcancel import ApiConnectorsConnectorIdcancel
from icasdk.apis.paths.api_connectors_connector_idenable import ApiConnectorsConnectorIdenable
from icasdk.apis.paths.api_connectors_connector_iddisable import ApiConnectorsConnectorIddisable
from icasdk.apis.paths.api_data_data_urn import ApiDataDataUrn
from icasdk.apis.paths.api_data_data_urncreate_inline_view_url import ApiDataDataUrncreateInlineViewUrl
from icasdk.apis.paths.api_data_data_urncreate_download_url import ApiDataDataUrncreateDownloadUrl
from icasdk.apis.paths.api_data_formats import ApiDataFormats
from icasdk.apis.paths.api_entitledbundles import ApiEntitledbundles
from icasdk.apis.paths.api_entitledbundles_entitled_bundle_id import ApiEntitledbundlesEntitledBundleId
from icasdk.apis.paths.api_activation_codesfind_best_matching_for_cwl import ApiActivationCodesfindBestMatchingForCwl
from icasdk.apis.paths.api_activation_codesfind_best_matching_for_nextflow import ApiActivationCodesfindBestMatchingForNextflow
from icasdk.apis.paths.api_activation_codesfind_all_matching_for_cwl import ApiActivationCodesfindAllMatchingForCwl
from icasdk.apis.paths.api_activation_codesfind_all_matching_for_nextflow import ApiActivationCodesfindAllMatchingForNextflow
from icasdk.apis.paths.api_event_codes import ApiEventCodes
from icasdk.apis.paths.api_event_log import ApiEventLog
from icasdk.apis.paths.api_jobs import ApiJobs
from icasdk.apis.paths.api_jobs_job_id import ApiJobsJobId
from icasdk.apis.paths.api_metadata_models import ApiMetadataModels
from icasdk.apis.paths.api_metadata_models_metadata_model_id import ApiMetadataModelsMetadataModelId
from icasdk.apis.paths.api_metadata_models_metadata_model_id_fields import ApiMetadataModelsMetadataModelIdFields
from icasdk.apis.paths.api_metadata_models_tenant_model import ApiMetadataModelsTenantModel
from icasdk.apis.paths.api_notification_channels import ApiNotificationChannels
from icasdk.apis.paths.api_notification_channels_channel_id import ApiNotificationChannelsChannelId
from icasdk.apis.paths.api_pipelines import ApiPipelines
from icasdk.apis.paths.api_pipelines_pipeline_id import ApiPipelinesPipelineId
from icasdk.apis.paths.api_pipelines_pipeline_id_input_parameters import ApiPipelinesPipelineIdInputParameters
from icasdk.apis.paths.api_pipelines_pipeline_id_configuration_parameters import ApiPipelinesPipelineIdConfigurationParameters
from icasdk.apis.paths.api_pipelines_pipeline_id_reference_sets import ApiPipelinesPipelineIdReferenceSets
from icasdk.apis.paths.api_pipelines_pipeline_id_documentation_html import ApiPipelinesPipelineIdDocumentationHTML
from icasdk.apis.paths.api_pipeline_languages_nextflow_versions import ApiPipelineLanguagesNextflowVersions
from icasdk.apis.paths.api_projects_project_id_analyses import ApiProjectsProjectIdAnalyses
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id import ApiProjectsProjectIdAnalysesAnalysisId
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_steps import ApiProjectsProjectIdAnalysesAnalysisIdSteps
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_inputs import ApiProjectsProjectIdAnalysesAnalysisIdInputs
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_outputs import ApiProjectsProjectIdAnalysesAnalysisIdOutputs
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_raw_output import ApiProjectsProjectIdAnalysesAnalysisIdRawOutput
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_configurations import ApiProjectsProjectIdAnalysesAnalysisIdConfigurations
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_idabort import ApiProjectsProjectIdAnalysesAnalysisIdabort
from icasdk.apis.paths.api_projects_project_id_analysis_creation_batch import ApiProjectsProjectIdAnalysisCreationBatch
from icasdk.apis.paths.api_projects_project_id_analysis_creation_batch_batch_id import ApiProjectsProjectIdAnalysisCreationBatchBatchId
from icasdk.apis.paths.api_projects_project_id_analysis_creation_batch_batch_id_items import ApiProjectsProjectIdAnalysisCreationBatchBatchIdItems
from icasdk.apis.paths.api_projects_project_id_analysis_creation_batch_batch_id_items_item_id import ApiProjectsProjectIdAnalysisCreationBatchBatchIdItemsItemId
from icasdk.apis.paths.api_projects_project_id_analysiscwl import ApiProjectsProjectIdAnalysiscwl
from icasdk.apis.paths.api_projects_project_id_analysisnextflow import ApiProjectsProjectIdAnalysisnextflow
from icasdk.apis.paths.api_projects import ApiProjects
from icasdk.apis.paths.api_projects_project_id import ApiProjectsProjectId
from icasdk.apis.paths.api_projects_project_id_bundles import ApiProjectsProjectIdBundles
from icasdk.apis.paths.api_projects_project_id_bundles_bundle_id import ApiProjectsProjectIdBundlesBundleId
from icasdk.apis.paths.api_projects_project_idhide import ApiProjectsProjectIdhide
from icasdk.apis.paths.api_projects_project_id_baseconnection_details import ApiProjectsProjectIdBaseconnectionDetails
from icasdk.apis.paths.api_projects_project_id_base_jobs import ApiProjectsProjectIdBaseJobs
from icasdk.apis.paths.api_projects_project_id_base_jobs_base_job_id import ApiProjectsProjectIdBaseJobsBaseJobId
from icasdk.apis.paths.api_projects_project_id_base_tables import ApiProjectsProjectIdBaseTables
from icasdk.apis.paths.api_projects_project_id_base_tables_table_idload_data import ApiProjectsProjectIdBaseTablesTableIdloadData
from icasdk.apis.paths.api_projects_project_id_custom_events import ApiProjectsProjectIdCustomEvents
from icasdk.apis.paths.api_projects_project_id_custom_notification_subscriptions import ApiProjectsProjectIdCustomNotificationSubscriptions
from icasdk.apis.paths.api_projects_project_id_custom_notification_subscriptions_subscription_id import ApiProjectsProjectIdCustomNotificationSubscriptionsSubscriptionId
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_cwl_input_json import ApiProjectsProjectIdAnalysesAnalysisIdCwlInputJson
from icasdk.apis.paths.api_projects_project_id_analyses_analysis_id_cwl_output_json import ApiProjectsProjectIdAnalysesAnalysisIdCwlOutputJson
from icasdk.apis.paths.api_projects_project_id_data import ApiProjectsProjectIdData
from icasdk.apis.paths.api_projects_project_id_data_eligible_for_linking import ApiProjectsProjectIdDataEligibleForLinking
from icasdk.apis.paths.api_projects_project_id_data_non_sample_data import ApiProjectsProjectIdDataNonSampleData
from icasdk.apis.paths.api_projects_project_id_data_data_id import ApiProjectsProjectIdDataDataId
from icasdk.apis.paths.api_projects_project_id_data_data_id_children import ApiProjectsProjectIdDataDataIdChildren
from icasdk.apis.paths.api_projects_project_id_data_data_id_linked_projects import ApiProjectsProjectIdDataDataIdLinkedProjects
from icasdk.apis.paths.api_projects_project_id_data_data_id_secondary_data import ApiProjectsProjectIdDataDataIdSecondaryData
from icasdk.apis.paths.api_projects_project_id_data_data_id_secondary_data_secondary_data_id import ApiProjectsProjectIdDataDataIdSecondaryDataSecondaryDataId
from icasdk.apis.paths.api_projects_project_id_data_data_idcreate_inline_view_url import ApiProjectsProjectIdDataDataIdcreateInlineViewUrl
from icasdk.apis.paths.api_projects_project_id_data_data_idcreate_download_url import ApiProjectsProjectIdDataDataIdcreateDownloadUrl
from icasdk.apis.paths.api_projects_project_id_data_data_idcreate_upload_url import ApiProjectsProjectIdDataDataIdcreateUploadUrl
from icasdk.apis.paths.api_projects_project_id_data_data_idcreate_temporary_credentials import ApiProjectsProjectIdDataDataIdcreateTemporaryCredentials
from icasdk.apis.paths.api_projects_project_id_data_data_idschedule_download import ApiProjectsProjectIdDataDataIdscheduleDownload
from icasdk.apis.paths.api_projects_project_id_data_data_idunlink import ApiProjectsProjectIdDataDataIdunlink
from icasdk.apis.paths.api_projects_project_id_data_data_idarchive import ApiProjectsProjectIdDataDataIdarchive
from icasdk.apis.paths.api_projects_project_id_data_data_idunarchive import ApiProjectsProjectIdDataDataIdunarchive
from icasdk.apis.paths.api_projects_project_id_data_data_iddelete import ApiProjectsProjectIdDataDataIddelete
from icasdk.apis.paths.api_projects_project_id_data_data_id_folder_upload_sessions import ApiProjectsProjectIdDataDataIdFolderUploadSessions
from icasdk.apis.paths.api_projects_project_id_data_data_id_folder_upload_sessions_folder_upload_session_id import ApiProjectsProjectIdDataDataIdFolderUploadSessionsFolderUploadSessionId
from icasdk.apis.paths.api_projects_project_id_data_data_id_folder_upload_sessions_folder_upload_session_idcomplete import ApiProjectsProjectIdDataDataIdFolderUploadSessionsFolderUploadSessionIdcomplete
from icasdk.apis.paths.api_projects_project_id_data_linking_batch import ApiProjectsProjectIdDataLinkingBatch
from icasdk.apis.paths.api_projects_project_id_data_linking_batch_batch_id import ApiProjectsProjectIdDataLinkingBatchBatchId
from icasdk.apis.paths.api_projects_project_id_data_linking_batch_batch_id_items import ApiProjectsProjectIdDataLinkingBatchBatchIdItems
from icasdk.apis.paths.api_projects_project_id_data_linking_batch_batch_id_items_item_id import ApiProjectsProjectIdDataLinkingBatchBatchIdItemsItemId
from icasdk.apis.paths.api_projects_project_id_data_transfers import ApiProjectsProjectIdDataTransfers
from icasdk.apis.paths.api_projects_project_id_data_transfers_data_transfer_id import ApiProjectsProjectIdDataTransfersDataTransferId
from icasdk.apis.paths.api_projects_project_id_data_transfers_data_transfer_idabort import ApiProjectsProjectIdDataTransfersDataTransferIdabort
from icasdk.apis.paths.api_projects_project_id_notification_subscriptions import ApiProjectsProjectIdNotificationSubscriptions
from icasdk.apis.paths.api_projects_project_id_notification_subscriptions_subscription_id import ApiProjectsProjectIdNotificationSubscriptionsSubscriptionId
from icasdk.apis.paths.api_projects_project_id_permissions import ApiProjectsProjectIdPermissions
from icasdk.apis.paths.api_projects_project_id_permissions_permission_id import ApiProjectsProjectIdPermissionsPermissionId
from icasdk.apis.paths.api_projects_project_id_pipelines import ApiProjectsProjectIdPipelines
from icasdk.apis.paths.api_projects_project_id_pipelines_pipeline_id import ApiProjectsProjectIdPipelinesPipelineId
from icasdk.apis.paths.api_projects_project_id_pipelines_pipeline_id_input_parameters import ApiProjectsProjectIdPipelinesPipelineIdInputParameters
from icasdk.apis.paths.api_projects_project_id_pipelines_pipeline_id_configuration_parameters import ApiProjectsProjectIdPipelinesPipelineIdConfigurationParameters
from icasdk.apis.paths.api_projects_project_id_pipelines_pipeline_id_reference_sets import ApiProjectsProjectIdPipelinesPipelineIdReferenceSets
from icasdk.apis.paths.api_projects_project_id_pipelines_pipeline_idrelease import ApiProjectsProjectIdPipelinesPipelineIdrelease
from icasdk.apis.paths.api_projects_project_id_pipelines_pipeline_id_documentation_html import ApiProjectsProjectIdPipelinesPipelineIdDocumentationHTML
from icasdk.apis.paths.api_projects_project_id_pipelinescreate_nextflow_pipeline import ApiProjectsProjectIdPipelinescreateNextflowPipeline
from icasdk.apis.paths.api_projects_project_id_pipelinescreate_cwl_pipeline import ApiProjectsProjectIdPipelinescreateCwlPipeline
from icasdk.apis.paths.api_projects_project_id_samples import ApiProjectsProjectIdSamples
from icasdk.apis.paths.api_projects_project_id_samples_sample_id import ApiProjectsProjectIdSamplesSampleId
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_history import ApiProjectsProjectIdSamplesSampleIdHistory
from icasdk.apis.paths.api_projects_project_id_samples_sample_idcomplete import ApiProjectsProjectIdSamplesSampleIdcomplete
from icasdk.apis.paths.api_projects_project_id_samples_sample_idunlink import ApiProjectsProjectIdSamplesSampleIdunlink
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_projects import ApiProjectsProjectIdSamplesSampleIdProjects
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_data import ApiProjectsProjectIdSamplesSampleIdData
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_data_data_id import ApiProjectsProjectIdSamplesSampleIdDataDataId
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_data_data_idunlink import ApiProjectsProjectIdSamplesSampleIdDataDataIdunlink
from icasdk.apis.paths.api_projects_project_id_samples_sample_iddelete_deep import ApiProjectsProjectIdSamplesSampleIddeleteDeep
from icasdk.apis.paths.api_projects_project_id_samples_sample_iddelete_with_input import ApiProjectsProjectIdSamplesSampleIddeleteWithInput
from icasdk.apis.paths.api_projects_project_id_samples_sample_iddelete_mark import ApiProjectsProjectIdSamplesSampleIddeleteMark
from icasdk.apis.paths.api_projects_project_id_samples_sample_iddelete_unlink import ApiProjectsProjectIdSamplesSampleIddeleteUnlink
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_metadata_metadata_model_id import ApiProjectsProjectIdSamplesSampleIdMetadataMetadataModelId
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_metadataupdate_fields import ApiProjectsProjectIdSamplesSampleIdMetadataupdateFields
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_metadata_field_field_id import ApiProjectsProjectIdSamplesSampleIdMetadataFieldFieldId
from icasdk.apis.paths.api_projects_project_id_samples_sample_id_metadata_field_id_field_count import ApiProjectsProjectIdSamplesSampleIdMetadataFieldIdFieldCount
from icasdk.apis.paths.api_projects_project_id_sample_creation_batch import ApiProjectsProjectIdSampleCreationBatch
from icasdk.apis.paths.api_projects_project_id_sample_creation_batch_batch_id import ApiProjectsProjectIdSampleCreationBatchBatchId
from icasdk.apis.paths.api_projects_project_id_sample_creation_batch_batch_id_items import ApiProjectsProjectIdSampleCreationBatchBatchIdItems
from icasdk.apis.paths.api_projects_project_id_sample_creation_batch_batch_id_items_item_id import ApiProjectsProjectIdSampleCreationBatchBatchIdItemsItemId
from icasdk.apis.paths.api_reference_sets import ApiReferenceSets
from icasdk.apis.paths.api_reference_sets_reference_set_id_species import ApiReferenceSetsReferenceSetIdSpecies
from icasdk.apis.paths.api_regions import ApiRegions
from icasdk.apis.paths.api_regions_region_id import ApiRegionsRegionId
from icasdk.apis.paths.api_samples import ApiSamples
from icasdk.apis.paths.api_storage_bundles import ApiStorageBundles
from icasdk.apis.paths.api_storage_configurations import ApiStorageConfigurations
from icasdk.apis.paths.api_storage_configurations_storage_configuration_id import ApiStorageConfigurationsStorageConfigurationId
from icasdk.apis.paths.api_storage_configurations_storage_configuration_id_details import ApiStorageConfigurationsStorageConfigurationIdDetails
from icasdk.apis.paths.api_storage_configurations_storage_configuration_idshare import ApiStorageConfigurationsStorageConfigurationIdshare
from icasdk.apis.paths.api_storage_credentials import ApiStorageCredentials
from icasdk.apis.paths.api_storage_credentials_storage_credential_id import ApiStorageCredentialsStorageCredentialId
from icasdk.apis.paths.api_storage_credentials_storage_credential_idshare import ApiStorageCredentialsStorageCredentialIdshare
from icasdk.apis.paths.api_storage_credentials_storage_credential_idupdate_secrets import ApiStorageCredentialsStorageCredentialIdupdateSecrets
from icasdk.apis.paths.api_tokens import ApiTokens
from icasdk.apis.paths.api_tokensrefresh import ApiTokensrefresh
from icasdk.apis.paths.api_users import ApiUsers
from icasdk.apis.paths.api_users_user_id import ApiUsersUserId
from icasdk.apis.paths.api_users_user_idapprove import ApiUsersUserIdapprove
from icasdk.apis.paths.api_users_user_idassign_tenant_administrator_rights import ApiUsersUserIdassignTenantAdministratorRights
from icasdk.apis.paths.api_users_user_idrevoke_tenant_administrator_rights import ApiUsersUserIdrevokeTenantAdministratorRights
from icasdk.apis.paths.api_workgroups import ApiWorkgroups
from icasdk.apis.paths.api_workgroups_workgroup_id import ApiWorkgroupsWorkgroupId
from icasdk.apis.paths.api_projects_project_id_datacreate_download_urls import ApiProjectsProjectIdDatacreateDownloadUrls
from icasdk.apis.paths.api_projects_project_id_samplessearch import ApiProjectsProjectIdSamplessearch

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_ANALYSIS_STORAGES: ApiAnalysisStorages,
        PathValues.API_BUNDLES: ApiBundles,
        PathValues.API_BUNDLES_BUNDLE_ID: ApiBundlesBundleId,
        PathValues.API_BUNDLES_BUNDLE_IDRELEASE: ApiBundlesBundleIdrelease,
        PathValues.API_BUNDLES_BUNDLE_ID_TERMS_OF_USE: ApiBundlesBundleIdTermsOfUse,
        PathValues.API_BUNDLES_BUNDLE_ID_TERMS_OF_USENEW: ApiBundlesBundleIdTermsOfUsenew,
        PathValues.API_BUNDLES_BUNDLE_IDDEPRECATE: ApiBundlesBundleIddeprecate,
        PathValues.API_BUNDLES_BUNDLE_ID_DATA: ApiBundlesBundleIdData,
        PathValues.API_BUNDLES_BUNDLE_ID_DATA_DATA_ID: ApiBundlesBundleIdDataDataId,
        PathValues.API_BUNDLES_BUNDLE_ID_PIPELINES: ApiBundlesBundleIdPipelines,
        PathValues.API_BUNDLES_BUNDLE_ID_PIPELINES_PIPELINE_ID: ApiBundlesBundleIdPipelinesPipelineId,
        PathValues.API_BUNDLES_BUNDLE_ID_SAMPLES: ApiBundlesBundleIdSamples,
        PathValues.API_BUNDLES_BUNDLE_ID_SAMPLES_SAMPLE_ID: ApiBundlesBundleIdSamplesSampleId,
        PathValues.API_BUNDLES_BUNDLE_ID_TOOLS: ApiBundlesBundleIdTools,
        PathValues.API_BUNDLES_BUNDLE_ID_TOOLS_ELIGIBLE_FOR_LINKING: ApiBundlesBundleIdToolsEligibleForLinking,
        PathValues.API_BUNDLES_BUNDLE_ID_TOOLS_TOOL_ID: ApiBundlesBundleIdToolsToolId,
        PathValues.API_CONNECTORS: ApiConnectors,
        PathValues.API_CONNECTORS_CONNECTOR_ID: ApiConnectorsConnectorId,
        PathValues.API_CONNECTORS_CONNECTOR_ID_UPLOAD_RULES: ApiConnectorsConnectorIdUploadRules,
        PathValues.API_CONNECTORS_CONNECTOR_ID_UPLOAD_RULES_UPLOAD_RULE_ID: ApiConnectorsConnectorIdUploadRulesUploadRuleId,
        PathValues.API_CONNECTORS_CONNECTOR_ID_DOWNLOAD_RULES: ApiConnectorsConnectorIdDownloadRules,
        PathValues.API_CONNECTORS_CONNECTOR_ID_DOWNLOAD_RULES_DOWNLOAD_RULE_ID: ApiConnectorsConnectorIdDownloadRulesDownloadRuleId,
        PathValues.API_CONNECTORS_CONNECTOR_IDCANCEL: ApiConnectorsConnectorIdcancel,
        PathValues.API_CONNECTORS_CONNECTOR_IDENABLE: ApiConnectorsConnectorIdenable,
        PathValues.API_CONNECTORS_CONNECTOR_IDDISABLE: ApiConnectorsConnectorIddisable,
        PathValues.API_DATA_DATA_URN: ApiDataDataUrn,
        PathValues.API_DATA_DATA_URNCREATE_INLINE_VIEW_URL: ApiDataDataUrncreateInlineViewUrl,
        PathValues.API_DATA_DATA_URNCREATE_DOWNLOAD_URL: ApiDataDataUrncreateDownloadUrl,
        PathValues.API_DATA_FORMATS: ApiDataFormats,
        PathValues.API_ENTITLEDBUNDLES: ApiEntitledbundles,
        PathValues.API_ENTITLEDBUNDLES_ENTITLED_BUNDLE_ID: ApiEntitledbundlesEntitledBundleId,
        PathValues.API_ACTIVATION_CODESFIND_BEST_MATCHING_FOR_CWL: ApiActivationCodesfindBestMatchingForCwl,
        PathValues.API_ACTIVATION_CODESFIND_BEST_MATCHING_FOR_NEXTFLOW: ApiActivationCodesfindBestMatchingForNextflow,
        PathValues.API_ACTIVATION_CODESFIND_ALL_MATCHING_FOR_CWL: ApiActivationCodesfindAllMatchingForCwl,
        PathValues.API_ACTIVATION_CODESFIND_ALL_MATCHING_FOR_NEXTFLOW: ApiActivationCodesfindAllMatchingForNextflow,
        PathValues.API_EVENT_CODES: ApiEventCodes,
        PathValues.API_EVENT_LOG: ApiEventLog,
        PathValues.API_JOBS: ApiJobs,
        PathValues.API_JOBS_JOB_ID: ApiJobsJobId,
        PathValues.API_METADATA_MODELS: ApiMetadataModels,
        PathValues.API_METADATA_MODELS_METADATA_MODEL_ID: ApiMetadataModelsMetadataModelId,
        PathValues.API_METADATA_MODELS_METADATA_MODEL_ID_FIELDS: ApiMetadataModelsMetadataModelIdFields,
        PathValues.API_METADATA_MODELS_TENANT_MODEL: ApiMetadataModelsTenantModel,
        PathValues.API_NOTIFICATION_CHANNELS: ApiNotificationChannels,
        PathValues.API_NOTIFICATION_CHANNELS_CHANNEL_ID: ApiNotificationChannelsChannelId,
        PathValues.API_PIPELINES: ApiPipelines,
        PathValues.API_PIPELINES_PIPELINE_ID: ApiPipelinesPipelineId,
        PathValues.API_PIPELINES_PIPELINE_ID_INPUT_PARAMETERS: ApiPipelinesPipelineIdInputParameters,
        PathValues.API_PIPELINES_PIPELINE_ID_CONFIGURATION_PARAMETERS: ApiPipelinesPipelineIdConfigurationParameters,
        PathValues.API_PIPELINES_PIPELINE_ID_REFERENCE_SETS: ApiPipelinesPipelineIdReferenceSets,
        PathValues.API_PIPELINES_PIPELINE_ID_DOCUMENTATION_HTML: ApiPipelinesPipelineIdDocumentationHTML,
        PathValues.API_PIPELINE_LANGUAGES_NEXTFLOW_VERSIONS: ApiPipelineLanguagesNextflowVersions,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES: ApiProjectsProjectIdAnalyses,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID: ApiProjectsProjectIdAnalysesAnalysisId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_STEPS: ApiProjectsProjectIdAnalysesAnalysisIdSteps,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_INPUTS: ApiProjectsProjectIdAnalysesAnalysisIdInputs,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_OUTPUTS: ApiProjectsProjectIdAnalysesAnalysisIdOutputs,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_RAW_OUTPUT: ApiProjectsProjectIdAnalysesAnalysisIdRawOutput,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CONFIGURATIONS: ApiProjectsProjectIdAnalysesAnalysisIdConfigurations,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_IDABORT: ApiProjectsProjectIdAnalysesAnalysisIdabort,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH: ApiProjectsProjectIdAnalysisCreationBatch,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID: ApiProjectsProjectIdAnalysisCreationBatchBatchId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID_ITEMS: ApiProjectsProjectIdAnalysisCreationBatchBatchIdItems,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID_ITEMS_ITEM_ID: ApiProjectsProjectIdAnalysisCreationBatchBatchIdItemsItemId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSISCWL: ApiProjectsProjectIdAnalysiscwl,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSISNEXTFLOW: ApiProjectsProjectIdAnalysisnextflow,
        PathValues.API_PROJECTS: ApiProjects,
        PathValues.API_PROJECTS_PROJECT_ID: ApiProjectsProjectId,
        PathValues.API_PROJECTS_PROJECT_ID_BUNDLES: ApiProjectsProjectIdBundles,
        PathValues.API_PROJECTS_PROJECT_ID_BUNDLES_BUNDLE_ID: ApiProjectsProjectIdBundlesBundleId,
        PathValues.API_PROJECTS_PROJECT_IDHIDE: ApiProjectsProjectIdhide,
        PathValues.API_PROJECTS_PROJECT_ID_BASECONNECTION_DETAILS: ApiProjectsProjectIdBaseconnectionDetails,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_JOBS: ApiProjectsProjectIdBaseJobs,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_JOBS_BASE_JOB_ID: ApiProjectsProjectIdBaseJobsBaseJobId,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_TABLES: ApiProjectsProjectIdBaseTables,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_TABLES_TABLE_IDLOAD_DATA: ApiProjectsProjectIdBaseTablesTableIdloadData,
        PathValues.API_PROJECTS_PROJECT_ID_CUSTOM_EVENTS: ApiProjectsProjectIdCustomEvents,
        PathValues.API_PROJECTS_PROJECT_ID_CUSTOM_NOTIFICATION_SUBSCRIPTIONS: ApiProjectsProjectIdCustomNotificationSubscriptions,
        PathValues.API_PROJECTS_PROJECT_ID_CUSTOM_NOTIFICATION_SUBSCRIPTIONS_SUBSCRIPTION_ID: ApiProjectsProjectIdCustomNotificationSubscriptionsSubscriptionId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CWL_INPUT_JSON: ApiProjectsProjectIdAnalysesAnalysisIdCwlInputJson,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CWL_OUTPUT_JSON: ApiProjectsProjectIdAnalysesAnalysisIdCwlOutputJson,
        PathValues.API_PROJECTS_PROJECT_ID_DATA: ApiProjectsProjectIdData,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_ELIGIBLE_FOR_LINKING: ApiProjectsProjectIdDataEligibleForLinking,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_NON_SAMPLE_DATA: ApiProjectsProjectIdDataNonSampleData,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID: ApiProjectsProjectIdDataDataId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_CHILDREN: ApiProjectsProjectIdDataDataIdChildren,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_LINKED_PROJECTS: ApiProjectsProjectIdDataDataIdLinkedProjects,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_SECONDARY_DATA: ApiProjectsProjectIdDataDataIdSecondaryData,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_SECONDARY_DATA_SECONDARY_DATA_ID: ApiProjectsProjectIdDataDataIdSecondaryDataSecondaryDataId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_INLINE_VIEW_URL: ApiProjectsProjectIdDataDataIdcreateInlineViewUrl,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_DOWNLOAD_URL: ApiProjectsProjectIdDataDataIdcreateDownloadUrl,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_UPLOAD_URL: ApiProjectsProjectIdDataDataIdcreateUploadUrl,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_TEMPORARY_CREDENTIALS: ApiProjectsProjectIdDataDataIdcreateTemporaryCredentials,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDSCHEDULE_DOWNLOAD: ApiProjectsProjectIdDataDataIdscheduleDownload,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDUNLINK: ApiProjectsProjectIdDataDataIdunlink,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDARCHIVE: ApiProjectsProjectIdDataDataIdarchive,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDUNARCHIVE: ApiProjectsProjectIdDataDataIdunarchive,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDDELETE: ApiProjectsProjectIdDataDataIddelete,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS: ApiProjectsProjectIdDataDataIdFolderUploadSessions,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS_FOLDER_UPLOAD_SESSION_ID: ApiProjectsProjectIdDataDataIdFolderUploadSessionsFolderUploadSessionId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS_FOLDER_UPLOAD_SESSION_IDCOMPLETE: ApiProjectsProjectIdDataDataIdFolderUploadSessionsFolderUploadSessionIdcomplete,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH: ApiProjectsProjectIdDataLinkingBatch,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID: ApiProjectsProjectIdDataLinkingBatchBatchId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID_ITEMS: ApiProjectsProjectIdDataLinkingBatchBatchIdItems,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID_ITEMS_ITEM_ID: ApiProjectsProjectIdDataLinkingBatchBatchIdItemsItemId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_TRANSFERS: ApiProjectsProjectIdDataTransfers,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_TRANSFERS_DATA_TRANSFER_ID: ApiProjectsProjectIdDataTransfersDataTransferId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_TRANSFERS_DATA_TRANSFER_IDABORT: ApiProjectsProjectIdDataTransfersDataTransferIdabort,
        PathValues.API_PROJECTS_PROJECT_ID_NOTIFICATION_SUBSCRIPTIONS: ApiProjectsProjectIdNotificationSubscriptions,
        PathValues.API_PROJECTS_PROJECT_ID_NOTIFICATION_SUBSCRIPTIONS_SUBSCRIPTION_ID: ApiProjectsProjectIdNotificationSubscriptionsSubscriptionId,
        PathValues.API_PROJECTS_PROJECT_ID_PERMISSIONS: ApiProjectsProjectIdPermissions,
        PathValues.API_PROJECTS_PROJECT_ID_PERMISSIONS_PERMISSION_ID: ApiProjectsProjectIdPermissionsPermissionId,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES: ApiProjectsProjectIdPipelines,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID: ApiProjectsProjectIdPipelinesPipelineId,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_INPUT_PARAMETERS: ApiProjectsProjectIdPipelinesPipelineIdInputParameters,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_CONFIGURATION_PARAMETERS: ApiProjectsProjectIdPipelinesPipelineIdConfigurationParameters,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_REFERENCE_SETS: ApiProjectsProjectIdPipelinesPipelineIdReferenceSets,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_IDRELEASE: ApiProjectsProjectIdPipelinesPipelineIdrelease,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_DOCUMENTATION_HTML: ApiProjectsProjectIdPipelinesPipelineIdDocumentationHTML,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINESCREATE_NEXTFLOW_PIPELINE: ApiProjectsProjectIdPipelinescreateNextflowPipeline,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINESCREATE_CWL_PIPELINE: ApiProjectsProjectIdPipelinescreateCwlPipeline,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES: ApiProjectsProjectIdSamples,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID: ApiProjectsProjectIdSamplesSampleId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_HISTORY: ApiProjectsProjectIdSamplesSampleIdHistory,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDCOMPLETE: ApiProjectsProjectIdSamplesSampleIdcomplete,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDUNLINK: ApiProjectsProjectIdSamplesSampleIdunlink,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_PROJECTS: ApiProjectsProjectIdSamplesSampleIdProjects,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA: ApiProjectsProjectIdSamplesSampleIdData,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA_DATA_ID: ApiProjectsProjectIdSamplesSampleIdDataDataId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA_DATA_IDUNLINK: ApiProjectsProjectIdSamplesSampleIdDataDataIdunlink,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_DEEP: ApiProjectsProjectIdSamplesSampleIddeleteDeep,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_WITH_INPUT: ApiProjectsProjectIdSamplesSampleIddeleteWithInput,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_MARK: ApiProjectsProjectIdSamplesSampleIddeleteMark,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_UNLINK: ApiProjectsProjectIdSamplesSampleIddeleteUnlink,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_METADATA_MODEL_ID: ApiProjectsProjectIdSamplesSampleIdMetadataMetadataModelId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATAUPDATE_FIELDS: ApiProjectsProjectIdSamplesSampleIdMetadataupdateFields,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_FIELD_FIELD_ID: ApiProjectsProjectIdSamplesSampleIdMetadataFieldFieldId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_FIELD_ID_FIELD_COUNT: ApiProjectsProjectIdSamplesSampleIdMetadataFieldIdFieldCount,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH: ApiProjectsProjectIdSampleCreationBatch,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID: ApiProjectsProjectIdSampleCreationBatchBatchId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID_ITEMS: ApiProjectsProjectIdSampleCreationBatchBatchIdItems,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID_ITEMS_ITEM_ID: ApiProjectsProjectIdSampleCreationBatchBatchIdItemsItemId,
        PathValues.API_REFERENCE_SETS: ApiReferenceSets,
        PathValues.API_REFERENCE_SETS_REFERENCE_SET_ID_SPECIES: ApiReferenceSetsReferenceSetIdSpecies,
        PathValues.API_REGIONS: ApiRegions,
        PathValues.API_REGIONS_REGION_ID: ApiRegionsRegionId,
        PathValues.API_SAMPLES: ApiSamples,
        PathValues.API_STORAGE_BUNDLES: ApiStorageBundles,
        PathValues.API_STORAGE_CONFIGURATIONS: ApiStorageConfigurations,
        PathValues.API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_ID: ApiStorageConfigurationsStorageConfigurationId,
        PathValues.API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_ID_DETAILS: ApiStorageConfigurationsStorageConfigurationIdDetails,
        PathValues.API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_IDSHARE: ApiStorageConfigurationsStorageConfigurationIdshare,
        PathValues.API_STORAGE_CREDENTIALS: ApiStorageCredentials,
        PathValues.API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_ID: ApiStorageCredentialsStorageCredentialId,
        PathValues.API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_IDSHARE: ApiStorageCredentialsStorageCredentialIdshare,
        PathValues.API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_IDUPDATE_SECRETS: ApiStorageCredentialsStorageCredentialIdupdateSecrets,
        PathValues.API_TOKENS: ApiTokens,
        PathValues.API_TOKENSREFRESH: ApiTokensrefresh,
        PathValues.API_USERS: ApiUsers,
        PathValues.API_USERS_USER_ID: ApiUsersUserId,
        PathValues.API_USERS_USER_IDAPPROVE: ApiUsersUserIdapprove,
        PathValues.API_USERS_USER_IDASSIGN_TENANT_ADMINISTRATOR_RIGHTS: ApiUsersUserIdassignTenantAdministratorRights,
        PathValues.API_USERS_USER_IDREVOKE_TENANT_ADMINISTRATOR_RIGHTS: ApiUsersUserIdrevokeTenantAdministratorRights,
        PathValues.API_WORKGROUPS: ApiWorkgroups,
        PathValues.API_WORKGROUPS_WORKGROUP_ID: ApiWorkgroupsWorkgroupId,
        PathValues.API_PROJECTS_PROJECT_ID_DATACREATE_DOWNLOAD_URLS: ApiProjectsProjectIdDatacreateDownloadUrls,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLESSEARCH: ApiProjectsProjectIdSamplessearch,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_ANALYSIS_STORAGES: ApiAnalysisStorages,
        PathValues.API_BUNDLES: ApiBundles,
        PathValues.API_BUNDLES_BUNDLE_ID: ApiBundlesBundleId,
        PathValues.API_BUNDLES_BUNDLE_IDRELEASE: ApiBundlesBundleIdrelease,
        PathValues.API_BUNDLES_BUNDLE_ID_TERMS_OF_USE: ApiBundlesBundleIdTermsOfUse,
        PathValues.API_BUNDLES_BUNDLE_ID_TERMS_OF_USENEW: ApiBundlesBundleIdTermsOfUsenew,
        PathValues.API_BUNDLES_BUNDLE_IDDEPRECATE: ApiBundlesBundleIddeprecate,
        PathValues.API_BUNDLES_BUNDLE_ID_DATA: ApiBundlesBundleIdData,
        PathValues.API_BUNDLES_BUNDLE_ID_DATA_DATA_ID: ApiBundlesBundleIdDataDataId,
        PathValues.API_BUNDLES_BUNDLE_ID_PIPELINES: ApiBundlesBundleIdPipelines,
        PathValues.API_BUNDLES_BUNDLE_ID_PIPELINES_PIPELINE_ID: ApiBundlesBundleIdPipelinesPipelineId,
        PathValues.API_BUNDLES_BUNDLE_ID_SAMPLES: ApiBundlesBundleIdSamples,
        PathValues.API_BUNDLES_BUNDLE_ID_SAMPLES_SAMPLE_ID: ApiBundlesBundleIdSamplesSampleId,
        PathValues.API_BUNDLES_BUNDLE_ID_TOOLS: ApiBundlesBundleIdTools,
        PathValues.API_BUNDLES_BUNDLE_ID_TOOLS_ELIGIBLE_FOR_LINKING: ApiBundlesBundleIdToolsEligibleForLinking,
        PathValues.API_BUNDLES_BUNDLE_ID_TOOLS_TOOL_ID: ApiBundlesBundleIdToolsToolId,
        PathValues.API_CONNECTORS: ApiConnectors,
        PathValues.API_CONNECTORS_CONNECTOR_ID: ApiConnectorsConnectorId,
        PathValues.API_CONNECTORS_CONNECTOR_ID_UPLOAD_RULES: ApiConnectorsConnectorIdUploadRules,
        PathValues.API_CONNECTORS_CONNECTOR_ID_UPLOAD_RULES_UPLOAD_RULE_ID: ApiConnectorsConnectorIdUploadRulesUploadRuleId,
        PathValues.API_CONNECTORS_CONNECTOR_ID_DOWNLOAD_RULES: ApiConnectorsConnectorIdDownloadRules,
        PathValues.API_CONNECTORS_CONNECTOR_ID_DOWNLOAD_RULES_DOWNLOAD_RULE_ID: ApiConnectorsConnectorIdDownloadRulesDownloadRuleId,
        PathValues.API_CONNECTORS_CONNECTOR_IDCANCEL: ApiConnectorsConnectorIdcancel,
        PathValues.API_CONNECTORS_CONNECTOR_IDENABLE: ApiConnectorsConnectorIdenable,
        PathValues.API_CONNECTORS_CONNECTOR_IDDISABLE: ApiConnectorsConnectorIddisable,
        PathValues.API_DATA_DATA_URN: ApiDataDataUrn,
        PathValues.API_DATA_DATA_URNCREATE_INLINE_VIEW_URL: ApiDataDataUrncreateInlineViewUrl,
        PathValues.API_DATA_DATA_URNCREATE_DOWNLOAD_URL: ApiDataDataUrncreateDownloadUrl,
        PathValues.API_DATA_FORMATS: ApiDataFormats,
        PathValues.API_ENTITLEDBUNDLES: ApiEntitledbundles,
        PathValues.API_ENTITLEDBUNDLES_ENTITLED_BUNDLE_ID: ApiEntitledbundlesEntitledBundleId,
        PathValues.API_ACTIVATION_CODESFIND_BEST_MATCHING_FOR_CWL: ApiActivationCodesfindBestMatchingForCwl,
        PathValues.API_ACTIVATION_CODESFIND_BEST_MATCHING_FOR_NEXTFLOW: ApiActivationCodesfindBestMatchingForNextflow,
        PathValues.API_ACTIVATION_CODESFIND_ALL_MATCHING_FOR_CWL: ApiActivationCodesfindAllMatchingForCwl,
        PathValues.API_ACTIVATION_CODESFIND_ALL_MATCHING_FOR_NEXTFLOW: ApiActivationCodesfindAllMatchingForNextflow,
        PathValues.API_EVENT_CODES: ApiEventCodes,
        PathValues.API_EVENT_LOG: ApiEventLog,
        PathValues.API_JOBS: ApiJobs,
        PathValues.API_JOBS_JOB_ID: ApiJobsJobId,
        PathValues.API_METADATA_MODELS: ApiMetadataModels,
        PathValues.API_METADATA_MODELS_METADATA_MODEL_ID: ApiMetadataModelsMetadataModelId,
        PathValues.API_METADATA_MODELS_METADATA_MODEL_ID_FIELDS: ApiMetadataModelsMetadataModelIdFields,
        PathValues.API_METADATA_MODELS_TENANT_MODEL: ApiMetadataModelsTenantModel,
        PathValues.API_NOTIFICATION_CHANNELS: ApiNotificationChannels,
        PathValues.API_NOTIFICATION_CHANNELS_CHANNEL_ID: ApiNotificationChannelsChannelId,
        PathValues.API_PIPELINES: ApiPipelines,
        PathValues.API_PIPELINES_PIPELINE_ID: ApiPipelinesPipelineId,
        PathValues.API_PIPELINES_PIPELINE_ID_INPUT_PARAMETERS: ApiPipelinesPipelineIdInputParameters,
        PathValues.API_PIPELINES_PIPELINE_ID_CONFIGURATION_PARAMETERS: ApiPipelinesPipelineIdConfigurationParameters,
        PathValues.API_PIPELINES_PIPELINE_ID_REFERENCE_SETS: ApiPipelinesPipelineIdReferenceSets,
        PathValues.API_PIPELINES_PIPELINE_ID_DOCUMENTATION_HTML: ApiPipelinesPipelineIdDocumentationHTML,
        PathValues.API_PIPELINE_LANGUAGES_NEXTFLOW_VERSIONS: ApiPipelineLanguagesNextflowVersions,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES: ApiProjectsProjectIdAnalyses,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID: ApiProjectsProjectIdAnalysesAnalysisId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_STEPS: ApiProjectsProjectIdAnalysesAnalysisIdSteps,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_INPUTS: ApiProjectsProjectIdAnalysesAnalysisIdInputs,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_OUTPUTS: ApiProjectsProjectIdAnalysesAnalysisIdOutputs,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_RAW_OUTPUT: ApiProjectsProjectIdAnalysesAnalysisIdRawOutput,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CONFIGURATIONS: ApiProjectsProjectIdAnalysesAnalysisIdConfigurations,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_IDABORT: ApiProjectsProjectIdAnalysesAnalysisIdabort,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH: ApiProjectsProjectIdAnalysisCreationBatch,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID: ApiProjectsProjectIdAnalysisCreationBatchBatchId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID_ITEMS: ApiProjectsProjectIdAnalysisCreationBatchBatchIdItems,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID_ITEMS_ITEM_ID: ApiProjectsProjectIdAnalysisCreationBatchBatchIdItemsItemId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSISCWL: ApiProjectsProjectIdAnalysiscwl,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSISNEXTFLOW: ApiProjectsProjectIdAnalysisnextflow,
        PathValues.API_PROJECTS: ApiProjects,
        PathValues.API_PROJECTS_PROJECT_ID: ApiProjectsProjectId,
        PathValues.API_PROJECTS_PROJECT_ID_BUNDLES: ApiProjectsProjectIdBundles,
        PathValues.API_PROJECTS_PROJECT_ID_BUNDLES_BUNDLE_ID: ApiProjectsProjectIdBundlesBundleId,
        PathValues.API_PROJECTS_PROJECT_IDHIDE: ApiProjectsProjectIdhide,
        PathValues.API_PROJECTS_PROJECT_ID_BASECONNECTION_DETAILS: ApiProjectsProjectIdBaseconnectionDetails,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_JOBS: ApiProjectsProjectIdBaseJobs,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_JOBS_BASE_JOB_ID: ApiProjectsProjectIdBaseJobsBaseJobId,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_TABLES: ApiProjectsProjectIdBaseTables,
        PathValues.API_PROJECTS_PROJECT_ID_BASE_TABLES_TABLE_IDLOAD_DATA: ApiProjectsProjectIdBaseTablesTableIdloadData,
        PathValues.API_PROJECTS_PROJECT_ID_CUSTOM_EVENTS: ApiProjectsProjectIdCustomEvents,
        PathValues.API_PROJECTS_PROJECT_ID_CUSTOM_NOTIFICATION_SUBSCRIPTIONS: ApiProjectsProjectIdCustomNotificationSubscriptions,
        PathValues.API_PROJECTS_PROJECT_ID_CUSTOM_NOTIFICATION_SUBSCRIPTIONS_SUBSCRIPTION_ID: ApiProjectsProjectIdCustomNotificationSubscriptionsSubscriptionId,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CWL_INPUT_JSON: ApiProjectsProjectIdAnalysesAnalysisIdCwlInputJson,
        PathValues.API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CWL_OUTPUT_JSON: ApiProjectsProjectIdAnalysesAnalysisIdCwlOutputJson,
        PathValues.API_PROJECTS_PROJECT_ID_DATA: ApiProjectsProjectIdData,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_ELIGIBLE_FOR_LINKING: ApiProjectsProjectIdDataEligibleForLinking,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_NON_SAMPLE_DATA: ApiProjectsProjectIdDataNonSampleData,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID: ApiProjectsProjectIdDataDataId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_CHILDREN: ApiProjectsProjectIdDataDataIdChildren,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_LINKED_PROJECTS: ApiProjectsProjectIdDataDataIdLinkedProjects,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_SECONDARY_DATA: ApiProjectsProjectIdDataDataIdSecondaryData,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_SECONDARY_DATA_SECONDARY_DATA_ID: ApiProjectsProjectIdDataDataIdSecondaryDataSecondaryDataId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_INLINE_VIEW_URL: ApiProjectsProjectIdDataDataIdcreateInlineViewUrl,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_DOWNLOAD_URL: ApiProjectsProjectIdDataDataIdcreateDownloadUrl,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_UPLOAD_URL: ApiProjectsProjectIdDataDataIdcreateUploadUrl,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_TEMPORARY_CREDENTIALS: ApiProjectsProjectIdDataDataIdcreateTemporaryCredentials,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDSCHEDULE_DOWNLOAD: ApiProjectsProjectIdDataDataIdscheduleDownload,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDUNLINK: ApiProjectsProjectIdDataDataIdunlink,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDARCHIVE: ApiProjectsProjectIdDataDataIdarchive,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDUNARCHIVE: ApiProjectsProjectIdDataDataIdunarchive,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_IDDELETE: ApiProjectsProjectIdDataDataIddelete,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS: ApiProjectsProjectIdDataDataIdFolderUploadSessions,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS_FOLDER_UPLOAD_SESSION_ID: ApiProjectsProjectIdDataDataIdFolderUploadSessionsFolderUploadSessionId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS_FOLDER_UPLOAD_SESSION_IDCOMPLETE: ApiProjectsProjectIdDataDataIdFolderUploadSessionsFolderUploadSessionIdcomplete,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH: ApiProjectsProjectIdDataLinkingBatch,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID: ApiProjectsProjectIdDataLinkingBatchBatchId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID_ITEMS: ApiProjectsProjectIdDataLinkingBatchBatchIdItems,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID_ITEMS_ITEM_ID: ApiProjectsProjectIdDataLinkingBatchBatchIdItemsItemId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_TRANSFERS: ApiProjectsProjectIdDataTransfers,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_TRANSFERS_DATA_TRANSFER_ID: ApiProjectsProjectIdDataTransfersDataTransferId,
        PathValues.API_PROJECTS_PROJECT_ID_DATA_TRANSFERS_DATA_TRANSFER_IDABORT: ApiProjectsProjectIdDataTransfersDataTransferIdabort,
        PathValues.API_PROJECTS_PROJECT_ID_NOTIFICATION_SUBSCRIPTIONS: ApiProjectsProjectIdNotificationSubscriptions,
        PathValues.API_PROJECTS_PROJECT_ID_NOTIFICATION_SUBSCRIPTIONS_SUBSCRIPTION_ID: ApiProjectsProjectIdNotificationSubscriptionsSubscriptionId,
        PathValues.API_PROJECTS_PROJECT_ID_PERMISSIONS: ApiProjectsProjectIdPermissions,
        PathValues.API_PROJECTS_PROJECT_ID_PERMISSIONS_PERMISSION_ID: ApiProjectsProjectIdPermissionsPermissionId,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES: ApiProjectsProjectIdPipelines,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID: ApiProjectsProjectIdPipelinesPipelineId,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_INPUT_PARAMETERS: ApiProjectsProjectIdPipelinesPipelineIdInputParameters,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_CONFIGURATION_PARAMETERS: ApiProjectsProjectIdPipelinesPipelineIdConfigurationParameters,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_REFERENCE_SETS: ApiProjectsProjectIdPipelinesPipelineIdReferenceSets,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_IDRELEASE: ApiProjectsProjectIdPipelinesPipelineIdrelease,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_DOCUMENTATION_HTML: ApiProjectsProjectIdPipelinesPipelineIdDocumentationHTML,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINESCREATE_NEXTFLOW_PIPELINE: ApiProjectsProjectIdPipelinescreateNextflowPipeline,
        PathValues.API_PROJECTS_PROJECT_ID_PIPELINESCREATE_CWL_PIPELINE: ApiProjectsProjectIdPipelinescreateCwlPipeline,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES: ApiProjectsProjectIdSamples,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID: ApiProjectsProjectIdSamplesSampleId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_HISTORY: ApiProjectsProjectIdSamplesSampleIdHistory,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDCOMPLETE: ApiProjectsProjectIdSamplesSampleIdcomplete,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDUNLINK: ApiProjectsProjectIdSamplesSampleIdunlink,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_PROJECTS: ApiProjectsProjectIdSamplesSampleIdProjects,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA: ApiProjectsProjectIdSamplesSampleIdData,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA_DATA_ID: ApiProjectsProjectIdSamplesSampleIdDataDataId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA_DATA_IDUNLINK: ApiProjectsProjectIdSamplesSampleIdDataDataIdunlink,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_DEEP: ApiProjectsProjectIdSamplesSampleIddeleteDeep,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_WITH_INPUT: ApiProjectsProjectIdSamplesSampleIddeleteWithInput,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_MARK: ApiProjectsProjectIdSamplesSampleIddeleteMark,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_UNLINK: ApiProjectsProjectIdSamplesSampleIddeleteUnlink,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_METADATA_MODEL_ID: ApiProjectsProjectIdSamplesSampleIdMetadataMetadataModelId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATAUPDATE_FIELDS: ApiProjectsProjectIdSamplesSampleIdMetadataupdateFields,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_FIELD_FIELD_ID: ApiProjectsProjectIdSamplesSampleIdMetadataFieldFieldId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_FIELD_ID_FIELD_COUNT: ApiProjectsProjectIdSamplesSampleIdMetadataFieldIdFieldCount,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH: ApiProjectsProjectIdSampleCreationBatch,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID: ApiProjectsProjectIdSampleCreationBatchBatchId,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID_ITEMS: ApiProjectsProjectIdSampleCreationBatchBatchIdItems,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID_ITEMS_ITEM_ID: ApiProjectsProjectIdSampleCreationBatchBatchIdItemsItemId,
        PathValues.API_REFERENCE_SETS: ApiReferenceSets,
        PathValues.API_REFERENCE_SETS_REFERENCE_SET_ID_SPECIES: ApiReferenceSetsReferenceSetIdSpecies,
        PathValues.API_REGIONS: ApiRegions,
        PathValues.API_REGIONS_REGION_ID: ApiRegionsRegionId,
        PathValues.API_SAMPLES: ApiSamples,
        PathValues.API_STORAGE_BUNDLES: ApiStorageBundles,
        PathValues.API_STORAGE_CONFIGURATIONS: ApiStorageConfigurations,
        PathValues.API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_ID: ApiStorageConfigurationsStorageConfigurationId,
        PathValues.API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_ID_DETAILS: ApiStorageConfigurationsStorageConfigurationIdDetails,
        PathValues.API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_IDSHARE: ApiStorageConfigurationsStorageConfigurationIdshare,
        PathValues.API_STORAGE_CREDENTIALS: ApiStorageCredentials,
        PathValues.API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_ID: ApiStorageCredentialsStorageCredentialId,
        PathValues.API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_IDSHARE: ApiStorageCredentialsStorageCredentialIdshare,
        PathValues.API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_IDUPDATE_SECRETS: ApiStorageCredentialsStorageCredentialIdupdateSecrets,
        PathValues.API_TOKENS: ApiTokens,
        PathValues.API_TOKENSREFRESH: ApiTokensrefresh,
        PathValues.API_USERS: ApiUsers,
        PathValues.API_USERS_USER_ID: ApiUsersUserId,
        PathValues.API_USERS_USER_IDAPPROVE: ApiUsersUserIdapprove,
        PathValues.API_USERS_USER_IDASSIGN_TENANT_ADMINISTRATOR_RIGHTS: ApiUsersUserIdassignTenantAdministratorRights,
        PathValues.API_USERS_USER_IDREVOKE_TENANT_ADMINISTRATOR_RIGHTS: ApiUsersUserIdrevokeTenantAdministratorRights,
        PathValues.API_WORKGROUPS: ApiWorkgroups,
        PathValues.API_WORKGROUPS_WORKGROUP_ID: ApiWorkgroupsWorkgroupId,
        PathValues.API_PROJECTS_PROJECT_ID_DATACREATE_DOWNLOAD_URLS: ApiProjectsProjectIdDatacreateDownloadUrls,
        PathValues.API_PROJECTS_PROJECT_ID_SAMPLESSEARCH: ApiProjectsProjectIdSamplessearch,
    }
)