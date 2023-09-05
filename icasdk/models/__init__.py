# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from icasdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from icasdk.model.aws_details import AWSDetails
from icasdk.model.activation_code_detail import ActivationCodeDetail
from icasdk.model.activation_code_detail_list import ActivationCodeDetailList
from icasdk.model.activation_code_detail_usage import ActivationCodeDetailUsage
from icasdk.model.analysis import Analysis
from icasdk.model.analysis_creation_batch import AnalysisCreationBatch
from icasdk.model.analysis_creation_batch_item import AnalysisCreationBatchItem
from icasdk.model.analysis_creation_batch_item_paged_list import AnalysisCreationBatchItemPagedList
from icasdk.model.analysis_creation_batch_item_processing import AnalysisCreationBatchItemProcessing
from icasdk.model.analysis_creation_batch_item_request import AnalysisCreationBatchItemRequest
from icasdk.model.analysis_data import AnalysisData
from icasdk.model.analysis_data_input import AnalysisDataInput
from icasdk.model.analysis_external_data import AnalysisExternalData
from icasdk.model.analysis_input import AnalysisInput
from icasdk.model.analysis_input_data_mount import AnalysisInputDataMount
from icasdk.model.analysis_input_external_data import AnalysisInputExternalData
from icasdk.model.analysis_input_list import AnalysisInputList
from icasdk.model.analysis_output import AnalysisOutput
from icasdk.model.analysis_output_list import AnalysisOutputList
from icasdk.model.analysis_output_mapping import AnalysisOutputMapping
from icasdk.model.analysis_paged_list import AnalysisPagedList
from icasdk.model.analysis_parameter_input import AnalysisParameterInput
from icasdk.model.analysis_raw_output import AnalysisRawOutput
from icasdk.model.analysis_reference_data_parameter import AnalysisReferenceDataParameter
from icasdk.model.analysis_s3_data_details import AnalysisS3DataDetails
from icasdk.model.analysis_step import AnalysisStep
from icasdk.model.analysis_step_list import AnalysisStepList
from icasdk.model.analysis_step_logs import AnalysisStepLogs
from icasdk.model.analysis_storage import AnalysisStorage
from icasdk.model.analysis_storage_list import AnalysisStorageList
from icasdk.model.analysis_tag import AnalysisTag
from icasdk.model.application import Application
from icasdk.model.aws_credentials import AwsCredentials
from icasdk.model.aws_temp_credentials import AwsTempCredentials
from icasdk.model.base_connection import BaseConnection
from icasdk.model.base_job import BaseJob
from icasdk.model.base_job_list import BaseJobList
from icasdk.model.bundle import Bundle
from icasdk.model.bundle_data import BundleData
from icasdk.model.bundle_data_paged_list import BundleDataPagedList
from icasdk.model.bundle_list import BundleList
from icasdk.model.bundle_paged_list import BundlePagedList
from icasdk.model.bundle_pipeline import BundlePipeline
from icasdk.model.bundle_pipeline_list import BundlePipelineList
from icasdk.model.bundle_sample import BundleSample
from icasdk.model.bundle_sample_paged_list import BundleSamplePagedList
from icasdk.model.bundle_tool import BundleTool
from icasdk.model.bundle_tools_list import BundleToolsList
from icasdk.model.cwl_tool_definition import CWLToolDefinition
from icasdk.model.complete_folder_upload_session import CompleteFolderUploadSession
from icasdk.model.connector import Connector
from icasdk.model.connector_list import ConnectorList
from icasdk.model.country import Country
from icasdk.model.create_analysis_creation_batch import CreateAnalysisCreationBatch
from icasdk.model.create_bundle import CreateBundle
from icasdk.model.create_connector import CreateConnector
from icasdk.model.create_custom_event import CreateCustomEvent
from icasdk.model.create_custom_notification_subscription import CreateCustomNotificationSubscription
from icasdk.model.create_cwl_analysis import CreateCwlAnalysis
from icasdk.model.create_cwl_pipeline import CreateCwlPipeline
from icasdk.model.create_data import CreateData
from icasdk.model.create_download_rule import CreateDownloadRule
from icasdk.model.create_nextflow_analysis import CreateNextflowAnalysis
from icasdk.model.create_nextflow_pipeline import CreateNextflowPipeline
from icasdk.model.create_notification_channel import CreateNotificationChannel
from icasdk.model.create_notification_subscription import CreateNotificationSubscription
from icasdk.model.create_project import CreateProject
from icasdk.model.create_project_data_linking_batch import CreateProjectDataLinkingBatch
from icasdk.model.create_project_data_linking_batch_item import CreateProjectDataLinkingBatchItem
from icasdk.model.create_project_data_update_batch import CreateProjectDataUpdateBatch
from icasdk.model.create_project_permission import CreateProjectPermission
from icasdk.model.create_project_permission_v4 import CreateProjectPermissionV4
from icasdk.model.create_sample import CreateSample
from icasdk.model.create_sample_creation_batch import CreateSampleCreationBatch
from icasdk.model.create_sample_creation_batch_data_item import CreateSampleCreationBatchDataItem
from icasdk.model.create_sample_creation_batch_sample_item import CreateSampleCreationBatchSampleItem
from icasdk.model.create_storage_configuration import CreateStorageConfiguration
from icasdk.model.create_storage_credential import CreateStorageCredential
from icasdk.model.create_temporary_credentials import CreateTemporaryCredentials
from icasdk.model.create_terms_of_use import CreateTermsOfUse
from icasdk.model.create_upload_rule import CreateUploadRule
from icasdk.model.custom_notification_subscription import CustomNotificationSubscription
from icasdk.model.custom_notification_subscription_list import CustomNotificationSubscriptionList
from icasdk.model.cwl_analysis_input import CwlAnalysisInput
from icasdk.model.cwl_analysis_input_json import CwlAnalysisInputJson
from icasdk.model.cwl_analysis_json_input import CwlAnalysisJsonInput
from icasdk.model.cwl_analysis_output_json import CwlAnalysisOutputJson
from icasdk.model.cwl_analysis_structured_input import CwlAnalysisStructuredInput
from icasdk.model.cwl_tool_definition_list import CwlToolDefinitionList
from icasdk.model.data import Data
from icasdk.model.data_details import DataDetails
from icasdk.model.data_format import DataFormat
from icasdk.model.data_format_paged_list import DataFormatPagedList
from icasdk.model.data_id_or_path_list import DataIdOrPathList
from icasdk.model.data_list import DataList
from icasdk.model.data_paged_list import DataPagedList
from icasdk.model.data_tag import DataTag
from icasdk.model.data_transfer import DataTransfer
from icasdk.model.data_transfer_paged_list import DataTransferPagedList
from icasdk.model.data_update_group import DataUpdateGroup
from icasdk.model.data_url_with_path import DataUrlWithPath
from icasdk.model.data_url_with_path_list import DataUrlWithPathList
from icasdk.model.download import Download
from icasdk.model.download_rule import DownloadRule
from icasdk.model.download_rule_list import DownloadRuleList
from icasdk.model.event_code import EventCode
from icasdk.model.event_code_list import EventCodeList
from icasdk.model.event_log import EventLog
from icasdk.model.event_log_list import EventLogList
from icasdk.model.execution_configuration import ExecutionConfiguration
from icasdk.model.execution_configuration_list import ExecutionConfigurationList
from icasdk.model.field import Field
from icasdk.model.field_id import FieldId
from icasdk.model.field_list import FieldList
from icasdk.model.find_project_samples import FindProjectSamples
from icasdk.model.find_sample_boolean_condition import FindSampleBooleanCondition
from icasdk.model.find_sample_condition import FindSampleCondition
from icasdk.model.find_sample_date_condition import FindSampleDateCondition
from icasdk.model.find_sample_number_condition import FindSampleNumberCondition
from icasdk.model.folder_upload_session import FolderUploadSession
from icasdk.model.inline_view import InlineView
from icasdk.model.input_parameter import InputParameter
from icasdk.model.input_parameter_list import InputParameterList
from icasdk.model.input_part import InputPart
from icasdk.model.integer_settings import IntegerSettings
from icasdk.model.job import Job
from icasdk.model.job_paged_list import JobPagedList
from icasdk.model.link import Link
from icasdk.model.links import Links
from icasdk.model.load_data_in_base_request import LoadDataInBaseRequest
from icasdk.model.metadata_field import MetadataField
from icasdk.model.metadata_model import MetadataModel
from icasdk.model.metadata_model_list import MetadataModelList
from icasdk.model.model import Model
from icasdk.model.multipart_form_data_input import MultipartFormDataInput
from icasdk.model.nextflow_analysis_input import NextflowAnalysisInput
from icasdk.model.notification_channel import NotificationChannel
from icasdk.model.notification_channel_list import NotificationChannelList
from icasdk.model.notification_subscription import NotificationSubscription
from icasdk.model.notification_subscription_list import NotificationSubscriptionList
from icasdk.model.option_settings import OptionSettings
from icasdk.model.optional_sample_tags import OptionalSampleTags
from icasdk.model.pipeline import Pipeline
from icasdk.model.pipeline_bundle import PipelineBundle
from icasdk.model.pipeline_configuration_parameter import PipelineConfigurationParameter
from icasdk.model.pipeline_configuration_parameter_list import PipelineConfigurationParameterList
from icasdk.model.pipeline_file import PipelineFile
from icasdk.model.pipeline_file_content_spec import PipelineFileContentSpec
from icasdk.model.pipeline_file_list import PipelineFileList
from icasdk.model.pipeline_html_documentation import PipelineHtmlDocumentation
from icasdk.model.pipeline_language_version import PipelineLanguageVersion
from icasdk.model.pipeline_language_version_list import PipelineLanguageVersionList
from icasdk.model.pipeline_list import PipelineList
from icasdk.model.pipeline_tag import PipelineTag
from icasdk.model.problem import Problem
from icasdk.model.project import Project
from icasdk.model.project_base_table import ProjectBaseTable
from icasdk.model.project_base_table_list import ProjectBaseTableList
from icasdk.model.project_bundle import ProjectBundle
from icasdk.model.project_bundle_list import ProjectBundleList
from icasdk.model.project_data import ProjectData
from icasdk.model.project_data_linking_batch import ProjectDataLinkingBatch
from icasdk.model.project_data_linking_batch_item import ProjectDataLinkingBatchItem
from icasdk.model.project_data_linking_batch_item_paged_list import ProjectDataLinkingBatchItemPagedList
from icasdk.model.project_data_linking_batch_item_processing import ProjectDataLinkingBatchItemProcessing
from icasdk.model.project_data_linking_batch_item_request import ProjectDataLinkingBatchItemRequest
from icasdk.model.project_data_paged_list import ProjectDataPagedList
from icasdk.model.project_data_update_batch import ProjectDataUpdateBatch
from icasdk.model.project_data_update_batch_item import ProjectDataUpdateBatchItem
from icasdk.model.project_data_update_batch_item_paged_list import ProjectDataUpdateBatchItemPagedList
from icasdk.model.project_data_update_batch_item_processing import ProjectDataUpdateBatchItemProcessing
from icasdk.model.project_data_update_batch_item_request import ProjectDataUpdateBatchItemRequest
from icasdk.model.project_list import ProjectList
from icasdk.model.project_paged_list import ProjectPagedList
from icasdk.model.project_permission import ProjectPermission
from icasdk.model.project_permission_list import ProjectPermissionList
from icasdk.model.project_permission_list_v4 import ProjectPermissionListV4
from icasdk.model.project_permission_v4 import ProjectPermissionV4
from icasdk.model.project_pipeline import ProjectPipeline
from icasdk.model.project_pipeline_list import ProjectPipelineList
from icasdk.model.project_sample import ProjectSample
from icasdk.model.project_sample_paged_list import ProjectSamplePagedList
from icasdk.model.project_tag import ProjectTag
from icasdk.model.rclone_temp_credentials import RcloneTempCredentials
from icasdk.model.reference_data import ReferenceData
from icasdk.model.reference_data_list import ReferenceDataList
from icasdk.model.reference_set import ReferenceSet
from icasdk.model.reference_set_list import ReferenceSetList
from icasdk.model.region import Region
from icasdk.model.region_list import RegionList
from icasdk.model.sample import Sample
from icasdk.model.sample_creation_batch import SampleCreationBatch
from icasdk.model.sample_creation_batch_item_paged_list import SampleCreationBatchItemPagedList
from icasdk.model.sample_creation_batch_item_processing import SampleCreationBatchItemProcessing
from icasdk.model.sample_creation_batch_item_request import SampleCreationBatchItemRequest
from icasdk.model.sample_creation_batch_sample_item import SampleCreationBatchSampleItem
from icasdk.model.sample_history import SampleHistory
from icasdk.model.sample_history_list import SampleHistoryList
from icasdk.model.sample_paged_list import SamplePagedList
from icasdk.model.sample_tag import SampleTag
from icasdk.model.schedule_download import ScheduleDownload
from icasdk.model.search_matching_activation_codes_for_cwl_analysis import SearchMatchingActivationCodesForCwlAnalysis
from icasdk.model.search_matching_activation_codes_for_nextflow_analysis import SearchMatchingActivationCodesForNextflowAnalysis
from icasdk.model.sequencing_run import SequencingRun
from icasdk.model.settings import Settings
from icasdk.model.species import Species
from icasdk.model.species_list import SpeciesList
from icasdk.model.storage_bundle import StorageBundle
from icasdk.model.storage_bundle_list import StorageBundleList
from icasdk.model.storage_configuration import StorageConfiguration
from icasdk.model.storage_configuration_details import StorageConfigurationDetails
from icasdk.model.storage_configuration_with_details import StorageConfigurationWithDetails
from icasdk.model.storage_configuration_with_details_list import StorageConfigurationWithDetailsList
from icasdk.model.storage_credential import StorageCredential
from icasdk.model.storage_credential_list import StorageCredentialList
from icasdk.model.string_settings import StringSettings
from icasdk.model.system_info import SystemInfo
from icasdk.model.tag_update import TagUpdate
from icasdk.model.temp_credentials import TempCredentials
from icasdk.model.terms_of_use import TermsOfUse
from icasdk.model.terms_of_use_acceptance import TermsOfUseAcceptance
from icasdk.model.token import Token
from icasdk.model.type import Type
from icasdk.model.type_list import TypeList
from icasdk.model.update_metadata import UpdateMetadata
from icasdk.model.update_metadata_field_group import UpdateMetadataFieldGroup
from icasdk.model.update_single_metadata_field import UpdateSingleMetadataField
from icasdk.model.update_storage_credential_secrets import UpdateStorageCredentialSecrets
from icasdk.model.upload import Upload
from icasdk.model.upload_rule import UploadRule
from icasdk.model.upload_rule_list import UploadRuleList
from icasdk.model.user import User
from icasdk.model.user_list import UserList
from icasdk.model.workflow import Workflow
from icasdk.model.workflow_session import WorkflowSession
from icasdk.model.workflow_session_tag import WorkflowSessionTag
from icasdk.model.workgroup import Workgroup
from icasdk.model.workgroup_list import WorkgroupList
