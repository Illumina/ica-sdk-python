# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p>   # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from icasdk import schemas  # noqa: F401


class CreateNextflowAnalysis(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "activationCodeDetailId",
            "userReference",
            "analysisInput",
            "pipelineId",
            "tags",
        }
        
        class properties:
            
            
            class userReference(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 1
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9 _-]*(/[a-zA-Z0-9 _-]+)*$',  # noqa: E501
                    }]
            pipelineId = schemas.StrSchema
        
            @staticmethod
            def tags() -> typing.Type['AnalysisTag']:
                return AnalysisTag
            activationCodeDetailId = schemas.UUIDSchema
        
            @staticmethod
            def analysisInput() -> typing.Type['NextflowAnalysisInput']:
                return NextflowAnalysisInput
            
            
            class analysisStorageId(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'analysisStorageId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class outputParentFolderId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'outputParentFolderId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class analysisOutput(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AnalysisOutputMapping']:
                        return AnalysisOutputMapping
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'analysisOutput':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "userReference": userReference,
                "pipelineId": pipelineId,
                "tags": tags,
                "activationCodeDetailId": activationCodeDetailId,
                "analysisInput": analysisInput,
                "analysisStorageId": analysisStorageId,
                "outputParentFolderId": outputParentFolderId,
                "analysisOutput": analysisOutput,
            }
    
    activationCodeDetailId: MetaOapg.properties.activationCodeDetailId
    userReference: MetaOapg.properties.userReference
    analysisInput: 'NextflowAnalysisInput'
    pipelineId: MetaOapg.properties.pipelineId
    tags: 'AnalysisTag'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userReference"]) -> MetaOapg.properties.userReference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pipelineId"]) -> MetaOapg.properties.pipelineId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'AnalysisTag': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activationCodeDetailId"]) -> MetaOapg.properties.activationCodeDetailId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysisInput"]) -> 'NextflowAnalysisInput': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysisStorageId"]) -> MetaOapg.properties.analysisStorageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputParentFolderId"]) -> MetaOapg.properties.outputParentFolderId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysisOutput"]) -> MetaOapg.properties.analysisOutput: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userReference", "pipelineId", "tags", "activationCodeDetailId", "analysisInput", "analysisStorageId", "outputParentFolderId", "analysisOutput", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userReference"]) -> MetaOapg.properties.userReference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pipelineId"]) -> MetaOapg.properties.pipelineId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> 'AnalysisTag': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activationCodeDetailId"]) -> MetaOapg.properties.activationCodeDetailId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysisInput"]) -> 'NextflowAnalysisInput': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysisStorageId"]) -> typing.Union[MetaOapg.properties.analysisStorageId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputParentFolderId"]) -> typing.Union[MetaOapg.properties.outputParentFolderId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysisOutput"]) -> typing.Union[MetaOapg.properties.analysisOutput, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userReference", "pipelineId", "tags", "activationCodeDetailId", "analysisInput", "analysisStorageId", "outputParentFolderId", "analysisOutput", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        activationCodeDetailId: typing.Union[MetaOapg.properties.activationCodeDetailId, str, uuid.UUID, ],
        userReference: typing.Union[MetaOapg.properties.userReference, str, ],
        analysisInput: 'NextflowAnalysisInput',
        pipelineId: typing.Union[MetaOapg.properties.pipelineId, str, ],
        tags: 'AnalysisTag',
        analysisStorageId: typing.Union[MetaOapg.properties.analysisStorageId, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        outputParentFolderId: typing.Union[MetaOapg.properties.outputParentFolderId, None, str, schemas.Unset] = schemas.unset,
        analysisOutput: typing.Union[MetaOapg.properties.analysisOutput, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateNextflowAnalysis':
        return super().__new__(
            cls,
            *args,
            activationCodeDetailId=activationCodeDetailId,
            userReference=userReference,
            analysisInput=analysisInput,
            pipelineId=pipelineId,
            tags=tags,
            analysisStorageId=analysisStorageId,
            outputParentFolderId=outputParentFolderId,
            analysisOutput=analysisOutput,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.analysis_output_mapping import AnalysisOutputMapping
from icasdk.model.analysis_tag import AnalysisTag
from icasdk.model.nextflow_analysis_input import NextflowAnalysisInput
