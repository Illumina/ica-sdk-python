import typing_extensions

from icasdk.apis.tags import TagValues
from icasdk.apis.tags.analysis_storage_api import AnalysisStorageApi
from icasdk.apis.tags.bundle_api import BundleApi
from icasdk.apis.tags.bundle_data_api import BundleDataApi
from icasdk.apis.tags.bundle_pipeline_api import BundlePipelineApi
from icasdk.apis.tags.bundle_sample_api import BundleSampleApi
from icasdk.apis.tags.bundle_tool_api import BundleToolApi
from icasdk.apis.tags.connector_api import ConnectorApi
from icasdk.apis.tags.data_api import DataApi
from icasdk.apis.tags.data_format_api import DataFormatApi
from icasdk.apis.tags.entitled_bundle_api import EntitledBundleApi
from icasdk.apis.tags.entitlement_detail_api import EntitlementDetailApi
from icasdk.apis.tags.event_code_api import EventCodeApi
from icasdk.apis.tags.event_log_api import EventLogApi
from icasdk.apis.tags.job_api import JobApi
from icasdk.apis.tags.metadata_model_api import MetadataModelApi
from icasdk.apis.tags.notification_channel_api import NotificationChannelApi
from icasdk.apis.tags.pipeline_api import PipelineApi
from icasdk.apis.tags.pipeline_language_api import PipelineLanguageApi
from icasdk.apis.tags.project_api import ProjectApi
from icasdk.apis.tags.project_analysis_api import ProjectAnalysisApi
from icasdk.apis.tags.project_analysis_creation_batch_api import ProjectAnalysisCreationBatchApi
from icasdk.apis.tags.project_base_api import ProjectBaseApi
from icasdk.apis.tags.project_custom_events_api import ProjectCustomEventsApi
from icasdk.apis.tags.project_custom_notification_subscriptions_api import ProjectCustomNotificationSubscriptionsApi
from icasdk.apis.tags.project_data_api import ProjectDataApi
from icasdk.apis.tags.project_data_linking_batch_api import ProjectDataLinkingBatchApi
from icasdk.apis.tags.project_data_transfer_api import ProjectDataTransferApi
from icasdk.apis.tags.project_data_update_batch_api import ProjectDataUpdateBatchApi
from icasdk.apis.tags.project_notification_subscriptions_api import ProjectNotificationSubscriptionsApi
from icasdk.apis.tags.project_permission_api import ProjectPermissionApi
from icasdk.apis.tags.project_pipeline_api import ProjectPipelineApi
from icasdk.apis.tags.project_sample_api import ProjectSampleApi
from icasdk.apis.tags.project_sample_batch_api import ProjectSampleBatchApi
from icasdk.apis.tags.reference_set_api import ReferenceSetApi
from icasdk.apis.tags.region_api import RegionApi
from icasdk.apis.tags.sample_api import SampleApi
from icasdk.apis.tags.sequencing_run_api import SequencingRunApi
from icasdk.apis.tags.storage_bundle_api import StorageBundleApi
from icasdk.apis.tags.storage_configuration_api import StorageConfigurationApi
from icasdk.apis.tags.storage_credentials_api import StorageCredentialsApi
from icasdk.apis.tags.system_api import SystemApi
from icasdk.apis.tags.token_api import TokenApi
from icasdk.apis.tags.user_api import UserApi
from icasdk.apis.tags.workgroup_api import WorkgroupApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ANALYSIS_STORAGE: AnalysisStorageApi,
        TagValues.BUNDLE: BundleApi,
        TagValues.BUNDLE_DATA: BundleDataApi,
        TagValues.BUNDLE_PIPELINE: BundlePipelineApi,
        TagValues.BUNDLE_SAMPLE: BundleSampleApi,
        TagValues.BUNDLE_TOOL: BundleToolApi,
        TagValues.CONNECTOR: ConnectorApi,
        TagValues.DATA: DataApi,
        TagValues.DATA_FORMAT: DataFormatApi,
        TagValues.ENTITLED_BUNDLE: EntitledBundleApi,
        TagValues.ENTITLEMENT_DETAIL: EntitlementDetailApi,
        TagValues.EVENT_CODE: EventCodeApi,
        TagValues.EVENT_LOG: EventLogApi,
        TagValues.JOB: JobApi,
        TagValues.METADATA_MODEL: MetadataModelApi,
        TagValues.NOTIFICATION_CHANNEL: NotificationChannelApi,
        TagValues.PIPELINE: PipelineApi,
        TagValues.PIPELINE_LANGUAGE: PipelineLanguageApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.PROJECT_ANALYSIS: ProjectAnalysisApi,
        TagValues.PROJECT_ANALYSIS_CREATION_BATCH: ProjectAnalysisCreationBatchApi,
        TagValues.PROJECT_BASE: ProjectBaseApi,
        TagValues.PROJECT_CUSTOM_EVENTS: ProjectCustomEventsApi,
        TagValues.PROJECT_CUSTOM_NOTIFICATION_SUBSCRIPTIONS: ProjectCustomNotificationSubscriptionsApi,
        TagValues.PROJECT_DATA: ProjectDataApi,
        TagValues.PROJECT_DATA_LINKING_BATCH: ProjectDataLinkingBatchApi,
        TagValues.PROJECT_DATA_TRANSFER: ProjectDataTransferApi,
        TagValues.PROJECT_DATA_UPDATE_BATCH: ProjectDataUpdateBatchApi,
        TagValues.PROJECT_NOTIFICATION_SUBSCRIPTIONS: ProjectNotificationSubscriptionsApi,
        TagValues.PROJECT_PERMISSION: ProjectPermissionApi,
        TagValues.PROJECT_PIPELINE: ProjectPipelineApi,
        TagValues.PROJECT_SAMPLE: ProjectSampleApi,
        TagValues.PROJECT_SAMPLE_BATCH: ProjectSampleBatchApi,
        TagValues.REFERENCE_SET: ReferenceSetApi,
        TagValues.REGION: RegionApi,
        TagValues.SAMPLE: SampleApi,
        TagValues.SEQUENCING_RUN: SequencingRunApi,
        TagValues.STORAGE_BUNDLE: StorageBundleApi,
        TagValues.STORAGE_CONFIGURATION: StorageConfigurationApi,
        TagValues.STORAGE_CREDENTIALS: StorageCredentialsApi,
        TagValues.SYSTEM: SystemApi,
        TagValues.TOKEN: TokenApi,
        TagValues.USER: UserApi,
        TagValues.WORKGROUP: WorkgroupApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ANALYSIS_STORAGE: AnalysisStorageApi,
        TagValues.BUNDLE: BundleApi,
        TagValues.BUNDLE_DATA: BundleDataApi,
        TagValues.BUNDLE_PIPELINE: BundlePipelineApi,
        TagValues.BUNDLE_SAMPLE: BundleSampleApi,
        TagValues.BUNDLE_TOOL: BundleToolApi,
        TagValues.CONNECTOR: ConnectorApi,
        TagValues.DATA: DataApi,
        TagValues.DATA_FORMAT: DataFormatApi,
        TagValues.ENTITLED_BUNDLE: EntitledBundleApi,
        TagValues.ENTITLEMENT_DETAIL: EntitlementDetailApi,
        TagValues.EVENT_CODE: EventCodeApi,
        TagValues.EVENT_LOG: EventLogApi,
        TagValues.JOB: JobApi,
        TagValues.METADATA_MODEL: MetadataModelApi,
        TagValues.NOTIFICATION_CHANNEL: NotificationChannelApi,
        TagValues.PIPELINE: PipelineApi,
        TagValues.PIPELINE_LANGUAGE: PipelineLanguageApi,
        TagValues.PROJECT: ProjectApi,
        TagValues.PROJECT_ANALYSIS: ProjectAnalysisApi,
        TagValues.PROJECT_ANALYSIS_CREATION_BATCH: ProjectAnalysisCreationBatchApi,
        TagValues.PROJECT_BASE: ProjectBaseApi,
        TagValues.PROJECT_CUSTOM_EVENTS: ProjectCustomEventsApi,
        TagValues.PROJECT_CUSTOM_NOTIFICATION_SUBSCRIPTIONS: ProjectCustomNotificationSubscriptionsApi,
        TagValues.PROJECT_DATA: ProjectDataApi,
        TagValues.PROJECT_DATA_LINKING_BATCH: ProjectDataLinkingBatchApi,
        TagValues.PROJECT_DATA_TRANSFER: ProjectDataTransferApi,
        TagValues.PROJECT_DATA_UPDATE_BATCH: ProjectDataUpdateBatchApi,
        TagValues.PROJECT_NOTIFICATION_SUBSCRIPTIONS: ProjectNotificationSubscriptionsApi,
        TagValues.PROJECT_PERMISSION: ProjectPermissionApi,
        TagValues.PROJECT_PIPELINE: ProjectPipelineApi,
        TagValues.PROJECT_SAMPLE: ProjectSampleApi,
        TagValues.PROJECT_SAMPLE_BATCH: ProjectSampleBatchApi,
        TagValues.REFERENCE_SET: ReferenceSetApi,
        TagValues.REGION: RegionApi,
        TagValues.SAMPLE: SampleApi,
        TagValues.SEQUENCING_RUN: SequencingRunApi,
        TagValues.STORAGE_BUNDLE: StorageBundleApi,
        TagValues.STORAGE_CONFIGURATION: StorageConfigurationApi,
        TagValues.STORAGE_CREDENTIALS: StorageCredentialsApi,
        TagValues.SYSTEM: SystemApi,
        TagValues.TOKEN: TokenApi,
        TagValues.USER: UserApi,
        TagValues.WORKGROUP: WorkgroupApi,
    }
)
