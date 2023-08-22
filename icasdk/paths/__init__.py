# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from icasdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_ANALYSIS_STORAGES = "/api/analysisStorages"
    API_BUNDLES = "/api/bundles"
    API_BUNDLES_BUNDLE_ID = "/api/bundles/{bundleId}"
    API_BUNDLES_BUNDLE_IDRELEASE = "/api/bundles/{bundleId}:release"
    API_BUNDLES_BUNDLE_ID_TERMS_OF_USE = "/api/bundles/{bundleId}/termsOfUse"
    API_BUNDLES_BUNDLE_ID_TERMS_OF_USENEW = "/api/bundles/{bundleId}/termsOfUse:new"
    API_BUNDLES_BUNDLE_IDDEPRECATE = "/api/bundles/{bundleId}:deprecate"
    API_BUNDLES_BUNDLE_ID_DATA = "/api/bundles/{bundleId}/data"
    API_BUNDLES_BUNDLE_ID_DATA_DATA_ID = "/api/bundles/{bundleId}/data/{dataId}"
    API_BUNDLES_BUNDLE_ID_PIPELINES = "/api/bundles/{bundleId}/pipelines"
    API_BUNDLES_BUNDLE_ID_PIPELINES_PIPELINE_ID = "/api/bundles/{bundleId}/pipelines/{pipelineId}"
    API_BUNDLES_BUNDLE_ID_SAMPLES = "/api/bundles/{bundleId}/samples"
    API_BUNDLES_BUNDLE_ID_SAMPLES_SAMPLE_ID = "/api/bundles/{bundleId}/samples/{sampleId}"
    API_BUNDLES_BUNDLE_ID_TOOLS = "/api/bundles/{bundleId}/tools"
    API_BUNDLES_BUNDLE_ID_TOOLS_ELIGIBLE_FOR_LINKING = "/api/bundles/{bundleId}/tools/eligibleForLinking"
    API_BUNDLES_BUNDLE_ID_TOOLS_TOOL_ID = "/api/bundles/{bundleId}/tools/{toolId}"
    API_CONNECTORS = "/api/connectors"
    API_CONNECTORS_CONNECTOR_ID = "/api/connectors/{connectorId}"
    API_CONNECTORS_CONNECTOR_ID_UPLOAD_RULES = "/api/connectors/{connectorId}/uploadRules"
    API_CONNECTORS_CONNECTOR_ID_UPLOAD_RULES_UPLOAD_RULE_ID = "/api/connectors/{connectorId}/uploadRules/{uploadRuleId}"
    API_CONNECTORS_CONNECTOR_ID_DOWNLOAD_RULES = "/api/connectors/{connectorId}/downloadRules"
    API_CONNECTORS_CONNECTOR_ID_DOWNLOAD_RULES_DOWNLOAD_RULE_ID = "/api/connectors/{connectorId}/downloadRules/{downloadRuleId}"
    API_CONNECTORS_CONNECTOR_IDCANCEL = "/api/connectors/{connectorId}:cancel"
    API_CONNECTORS_CONNECTOR_IDENABLE = "/api/connectors/{connectorId}:enable"
    API_CONNECTORS_CONNECTOR_IDDISABLE = "/api/connectors/{connectorId}:disable"
    API_DATA_DATA_URN = "/api/data/{dataUrn}"
    API_DATA_DATA_URNCREATE_INLINE_VIEW_URL = "/api/data/{dataUrn}:createInlineViewUrl"
    API_DATA_DATA_URNCREATE_DOWNLOAD_URL = "/api/data/{dataUrn}:createDownloadUrl"
    API_DATA_FORMATS = "/api/dataFormats"
    API_ENTITLEDBUNDLES = "/api/entitledbundles"
    API_ENTITLEDBUNDLES_ENTITLED_BUNDLE_ID = "/api/entitledbundles/{entitledBundleId}"
    API_ACTIVATION_CODESFIND_BEST_MATCHING_FOR_CWL = "/api/activationCodes:findBestMatchingForCwl"
    API_ACTIVATION_CODESFIND_BEST_MATCHING_FOR_NEXTFLOW = "/api/activationCodes:findBestMatchingForNextflow"
    API_ACTIVATION_CODESFIND_ALL_MATCHING_FOR_CWL = "/api/activationCodes:findAllMatchingForCwl"
    API_ACTIVATION_CODESFIND_ALL_MATCHING_FOR_NEXTFLOW = "/api/activationCodes:findAllMatchingForNextflow"
    API_EVENT_CODES = "/api/eventCodes"
    API_EVENT_LOG = "/api/eventLog"
    API_JOBS = "/api/jobs"
    API_JOBS_JOB_ID = "/api/jobs/{jobId}"
    API_METADATA_MODELS = "/api/metadataModels"
    API_METADATA_MODELS_METADATA_MODEL_ID = "/api/metadataModels/{metadataModelId}"
    API_METADATA_MODELS_METADATA_MODEL_ID_FIELDS = "/api/metadataModels/{metadataModelId}/fields"
    API_METADATA_MODELS_TENANT_MODEL = "/api/metadataModels/tenantModel"
    API_NOTIFICATION_CHANNELS = "/api/notificationChannels"
    API_NOTIFICATION_CHANNELS_CHANNEL_ID = "/api/notificationChannels/{channelId}"
    API_PIPELINES = "/api/pipelines"
    API_PIPELINES_PIPELINE_ID = "/api/pipelines/{pipelineId}"
    API_PIPELINES_PIPELINE_ID_INPUT_PARAMETERS = "/api/pipelines/{pipelineId}/inputParameters"
    API_PIPELINES_PIPELINE_ID_CONFIGURATION_PARAMETERS = "/api/pipelines/{pipelineId}/configurationParameters"
    API_PIPELINES_PIPELINE_ID_REFERENCE_SETS = "/api/pipelines/{pipelineId}/referenceSets"
    API_PIPELINES_PIPELINE_ID_DOCUMENTATION_HTML = "/api/pipelines/{pipelineId}/documentation/HTML"
    API_PIPELINE_LANGUAGES_NEXTFLOW_VERSIONS = "/api/pipelineLanguages/nextflow/versions"
    API_PROJECTS_PROJECT_ID_ANALYSES = "/api/projects/{projectId}/analyses"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID = "/api/projects/{projectId}/analyses/{analysisId}"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_STEPS = "/api/projects/{projectId}/analyses/{analysisId}/steps"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_INPUTS = "/api/projects/{projectId}/analyses/{analysisId}/inputs"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_OUTPUTS = "/api/projects/{projectId}/analyses/{analysisId}/outputs"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_RAW_OUTPUT = "/api/projects/{projectId}/analyses/{analysisId}/rawOutput"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CONFIGURATIONS = "/api/projects/{projectId}/analyses/{analysisId}/configurations"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_IDABORT = "/api/projects/{projectId}/analyses/{analysisId}:abort"
    API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH = "/api/projects/{projectId}/analysisCreationBatch"
    API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID = "/api/projects/{projectId}/analysisCreationBatch/{batchId}"
    API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID_ITEMS = "/api/projects/{projectId}/analysisCreationBatch/{batchId}/items"
    API_PROJECTS_PROJECT_ID_ANALYSIS_CREATION_BATCH_BATCH_ID_ITEMS_ITEM_ID = "/api/projects/{projectId}/analysisCreationBatch/{batchId}/items/{itemId}"
    API_PROJECTS_PROJECT_ID_ANALYSISCWL = "/api/projects/{projectId}/analysis:cwl"
    API_PROJECTS_PROJECT_ID_ANALYSISNEXTFLOW = "/api/projects/{projectId}/analysis:nextflow"
    API_PROJECTS = "/api/projects"
    API_PROJECTS_PROJECT_ID = "/api/projects/{projectId}"
    API_PROJECTS_PROJECT_ID_BUNDLES = "/api/projects/{projectId}/bundles"
    API_PROJECTS_PROJECT_ID_BUNDLES_BUNDLE_ID = "/api/projects/{projectId}/bundles/{bundleId}"
    API_PROJECTS_PROJECT_IDHIDE = "/api/projects/{projectId}:hide"
    API_PROJECTS_PROJECT_ID_BASECONNECTION_DETAILS = "/api/projects/{projectId}/base:connectionDetails"
    API_PROJECTS_PROJECT_ID_BASE_JOBS = "/api/projects/{projectId}/base/jobs"
    API_PROJECTS_PROJECT_ID_BASE_JOBS_BASE_JOB_ID = "/api/projects/{projectId}/base/jobs/{baseJobId}"
    API_PROJECTS_PROJECT_ID_BASE_TABLES = "/api/projects/{projectId}/base/tables"
    API_PROJECTS_PROJECT_ID_BASE_TABLES_TABLE_IDLOAD_DATA = "/api/projects/{projectId}/base/tables/{tableId}:loadData"
    API_PROJECTS_PROJECT_ID_CUSTOM_EVENTS = "/api/projects/{projectId}/customEvents"
    API_PROJECTS_PROJECT_ID_CUSTOM_NOTIFICATION_SUBSCRIPTIONS = "/api/projects/{projectId}/customNotificationSubscriptions"
    API_PROJECTS_PROJECT_ID_CUSTOM_NOTIFICATION_SUBSCRIPTIONS_SUBSCRIPTION_ID = "/api/projects/{projectId}/customNotificationSubscriptions/{subscriptionId}"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CWL_INPUT_JSON = "/api/projects/{projectId}/analyses/{analysisId}/cwl/inputJson"
    API_PROJECTS_PROJECT_ID_ANALYSES_ANALYSIS_ID_CWL_OUTPUT_JSON = "/api/projects/{projectId}/analyses/{analysisId}/cwl/outputJson"
    API_PROJECTS_PROJECT_ID_DATA = "/api/projects/{projectId}/data"
    API_PROJECTS_PROJECT_ID_DATA_ELIGIBLE_FOR_LINKING = "/api/projects/{projectId}/data/eligibleForLinking"
    API_PROJECTS_PROJECT_ID_DATA_NON_SAMPLE_DATA = "/api/projects/{projectId}/data/nonSampleData"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID = "/api/projects/{projectId}/data/{dataId}"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_CHILDREN = "/api/projects/{projectId}/data/{dataId}/children"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_LINKED_PROJECTS = "/api/projects/{projectId}/data/{dataId}/linkedProjects"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_SECONDARY_DATA = "/api/projects/{projectId}/data/{dataId}/secondaryData"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_SECONDARY_DATA_SECONDARY_DATA_ID = "/api/projects/{projectId}/data/{dataId}/secondaryData/{secondaryDataId}"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_INLINE_VIEW_URL = "/api/projects/{projectId}/data/{dataId}:createInlineViewUrl"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_DOWNLOAD_URL = "/api/projects/{projectId}/data/{dataId}:createDownloadUrl"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_UPLOAD_URL = "/api/projects/{projectId}/data/{dataId}:createUploadUrl"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDCREATE_TEMPORARY_CREDENTIALS = "/api/projects/{projectId}/data/{dataId}:createTemporaryCredentials"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDSCHEDULE_DOWNLOAD = "/api/projects/{projectId}/data/{dataId}:scheduleDownload"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDUNLINK = "/api/projects/{projectId}/data/{dataId}:unlink"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDARCHIVE = "/api/projects/{projectId}/data/{dataId}:archive"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDUNARCHIVE = "/api/projects/{projectId}/data/{dataId}:unarchive"
    API_PROJECTS_PROJECT_ID_DATA_DATA_IDDELETE = "/api/projects/{projectId}/data/{dataId}:delete"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS = "/api/projects/{projectId}/data/{dataId}/folderUploadSessions"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS_FOLDER_UPLOAD_SESSION_ID = "/api/projects/{projectId}/data/{dataId}/folderUploadSessions/{folderUploadSessionId}"
    API_PROJECTS_PROJECT_ID_DATA_DATA_ID_FOLDER_UPLOAD_SESSIONS_FOLDER_UPLOAD_SESSION_IDCOMPLETE = "/api/projects/{projectId}/data/{dataId}/folderUploadSessions/{folderUploadSessionId}:complete"
    API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH = "/api/projects/{projectId}/dataLinkingBatch"
    API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID = "/api/projects/{projectId}/dataLinkingBatch/{batchId}"
    API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID_ITEMS = "/api/projects/{projectId}/dataLinkingBatch/{batchId}/items"
    API_PROJECTS_PROJECT_ID_DATA_LINKING_BATCH_BATCH_ID_ITEMS_ITEM_ID = "/api/projects/{projectId}/dataLinkingBatch/{batchId}/items/{itemId}"
    API_PROJECTS_PROJECT_ID_DATA_TRANSFERS = "/api/projects/{projectId}/dataTransfers"
    API_PROJECTS_PROJECT_ID_DATA_TRANSFERS_DATA_TRANSFER_ID = "/api/projects/{projectId}/dataTransfers/{dataTransferId}"
    API_PROJECTS_PROJECT_ID_DATA_TRANSFERS_DATA_TRANSFER_IDABORT = "/api/projects/{projectId}/dataTransfers/{dataTransferId}:abort"
    API_PROJECTS_PROJECT_ID_NOTIFICATION_SUBSCRIPTIONS = "/api/projects/{projectId}/notificationSubscriptions"
    API_PROJECTS_PROJECT_ID_NOTIFICATION_SUBSCRIPTIONS_SUBSCRIPTION_ID = "/api/projects/{projectId}/notificationSubscriptions/{subscriptionId}"
    API_PROJECTS_PROJECT_ID_PERMISSIONS = "/api/projects/{projectId}/permissions"
    API_PROJECTS_PROJECT_ID_PERMISSIONS_PERMISSION_ID = "/api/projects/{projectId}/permissions/{permissionId}"
    API_PROJECTS_PROJECT_ID_PIPELINES = "/api/projects/{projectId}/pipelines"
    API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID = "/api/projects/{projectId}/pipelines/{pipelineId}"
    API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_INPUT_PARAMETERS = "/api/projects/{projectId}/pipelines/{pipelineId}/inputParameters"
    API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_CONFIGURATION_PARAMETERS = "/api/projects/{projectId}/pipelines/{pipelineId}/configurationParameters"
    API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_REFERENCE_SETS = "/api/projects/{projectId}/pipelines/{pipelineId}/referenceSets"
    API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_IDRELEASE = "/api/projects/{projectId}/pipelines/{pipelineId}:release"
    API_PROJECTS_PROJECT_ID_PIPELINES_PIPELINE_ID_DOCUMENTATION_HTML = "/api/projects/{projectId}/pipelines/{pipelineId}/documentation/HTML"
    API_PROJECTS_PROJECT_ID_PIPELINESCREATE_NEXTFLOW_PIPELINE = "/api/projects/{projectId}/pipelines:createNextflowPipeline"
    API_PROJECTS_PROJECT_ID_PIPELINESCREATE_CWL_PIPELINE = "/api/projects/{projectId}/pipelines:createCwlPipeline"
    API_PROJECTS_PROJECT_ID_SAMPLES = "/api/projects/{projectId}/samples"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID = "/api/projects/{projectId}/samples/{sampleId}"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_HISTORY = "/api/projects/{projectId}/samples/{sampleId}/history"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDCOMPLETE = "/api/projects/{projectId}/samples/{sampleId}:complete"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDUNLINK = "/api/projects/{projectId}/samples/{sampleId}:unlink"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_PROJECTS = "/api/projects/{projectId}/samples/{sampleId}/projects"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA = "/api/projects/{projectId}/samples/{sampleId}/data"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA_DATA_ID = "/api/projects/{projectId}/samples/{sampleId}/data/{dataId}"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_DATA_DATA_IDUNLINK = "/api/projects/{projectId}/samples/{sampleId}/data/{dataId}:unlink"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_DEEP = "/api/projects/{projectId}/samples/{sampleId}:deleteDeep"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_WITH_INPUT = "/api/projects/{projectId}/samples/{sampleId}:deleteWithInput"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_MARK = "/api/projects/{projectId}/samples/{sampleId}:deleteMark"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_IDDELETE_UNLINK = "/api/projects/{projectId}/samples/{sampleId}:deleteUnlink"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_METADATA_MODEL_ID = "/api/projects/{projectId}/samples/{sampleId}/metadata/{metadataModelId}"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATAUPDATE_FIELDS = "/api/projects/{projectId}/samples/{sampleId}/metadata:updateFields"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_FIELD_FIELD_ID = "/api/projects/{projectId}/samples/{sampleId}/metadata/field/{fieldId}"
    API_PROJECTS_PROJECT_ID_SAMPLES_SAMPLE_ID_METADATA_FIELD_ID_FIELD_COUNT = "/api/projects/{projectId}/samples/{sampleId}/metadata/{fieldId}/fieldCount"
    API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH = "/api/projects/{projectId}/sampleCreationBatch"
    API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID = "/api/projects/{projectId}/sampleCreationBatch/{batchId}"
    API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID_ITEMS = "/api/projects/{projectId}/sampleCreationBatch/{batchId}/items"
    API_PROJECTS_PROJECT_ID_SAMPLE_CREATION_BATCH_BATCH_ID_ITEMS_ITEM_ID = "/api/projects/{projectId}/sampleCreationBatch/{batchId}/items/{itemId}"
    API_REFERENCE_SETS = "/api/referenceSets"
    API_REFERENCE_SETS_REFERENCE_SET_ID_SPECIES = "/api/referenceSets/{referenceSetId}/species"
    API_REGIONS = "/api/regions"
    API_REGIONS_REGION_ID = "/api/regions/{regionId}"
    API_SAMPLES = "/api/samples"
    API_STORAGE_BUNDLES = "/api/storageBundles"
    API_STORAGE_CONFIGURATIONS = "/api/storageConfigurations"
    API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_ID = "/api/storageConfigurations/{storageConfigurationId}"
    API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_ID_DETAILS = "/api/storageConfigurations/{storageConfigurationId}/details"
    API_STORAGE_CONFIGURATIONS_STORAGE_CONFIGURATION_IDSHARE = "/api/storageConfigurations/{storageConfigurationId}:share"
    API_STORAGE_CREDENTIALS = "/api/storageCredentials"
    API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_ID = "/api/storageCredentials/{storageCredentialId}"
    API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_IDSHARE = "/api/storageCredentials/{storageCredentialId}:share"
    API_STORAGE_CREDENTIALS_STORAGE_CREDENTIAL_IDUPDATE_SECRETS = "/api/storageCredentials/{storageCredentialId}:updateSecrets"
    API_TOKENS = "/api/tokens"
    API_TOKENSREFRESH = "/api/tokens:refresh"
    API_USERS = "/api/users"
    API_USERS_USER_ID = "/api/users/{userId}"
    API_USERS_USER_IDAPPROVE = "/api/users/{userId}:approve"
    API_USERS_USER_IDASSIGN_TENANT_ADMINISTRATOR_RIGHTS = "/api/users/{userId}:assignTenantAdministratorRights"
    API_USERS_USER_IDREVOKE_TENANT_ADMINISTRATOR_RIGHTS = "/api/users/{userId}:revokeTenantAdministratorRights"
    API_WORKGROUPS = "/api/workgroups"
    API_WORKGROUPS_WORKGROUP_ID = "/api/workgroups/{workgroupId}"
    API_PROJECTS_PROJECT_ID_DATACREATE_DOWNLOAD_URLS = "/api/projects/{projectId}/data:createDownloadUrls"
    API_PROJECTS_PROJECT_ID_SAMPLESSEARCH = "/api/projects/{projectId}/samples:search"