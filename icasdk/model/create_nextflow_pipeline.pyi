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


class CreateNextflowPipeline(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "parametersXmlFile",
            "code",
            "mainNextflowFile",
            "description",
            "analysisStorageId",
        }
        
        class properties:
            
            
            class code(
                schemas.StrSchema
            ):
                pass
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            mainNextflowFile = schemas.BinarySchema
            parametersXmlFile = schemas.BinarySchema
            analysisStorageId = schemas.UUIDSchema
            
            
            class pipelineLanguageVersionId(
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
                ) -> 'pipelineLanguageVersionId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            nextflowConfigFile = schemas.BinarySchema
            
            
            class otherNextflowFiles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.BinarySchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'otherNextflowFiles':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class metadataModelFile(
                schemas.BinaryBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'binary'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'metadataModelFile':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def links() -> typing.Type['Links']:
                return Links
            
            
            class versionComment(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'versionComment':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class categories(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'categories':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class htmlDocumentation(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'htmlDocumentation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "code": code,
                "description": description,
                "mainNextflowFile": mainNextflowFile,
                "parametersXmlFile": parametersXmlFile,
                "analysisStorageId": analysisStorageId,
                "pipelineLanguageVersionId": pipelineLanguageVersionId,
                "nextflowConfigFile": nextflowConfigFile,
                "otherNextflowFiles": otherNextflowFiles,
                "metadataModelFile": metadataModelFile,
                "links": links,
                "versionComment": versionComment,
                "categories": categories,
                "htmlDocumentation": htmlDocumentation,
            }
    
    parametersXmlFile: MetaOapg.properties.parametersXmlFile
    code: MetaOapg.properties.code
    mainNextflowFile: MetaOapg.properties.mainNextflowFile
    description: MetaOapg.properties.description
    analysisStorageId: MetaOapg.properties.analysisStorageId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mainNextflowFile"]) -> MetaOapg.properties.mainNextflowFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parametersXmlFile"]) -> MetaOapg.properties.parametersXmlFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analysisStorageId"]) -> MetaOapg.properties.analysisStorageId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pipelineLanguageVersionId"]) -> MetaOapg.properties.pipelineLanguageVersionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextflowConfigFile"]) -> MetaOapg.properties.nextflowConfigFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["otherNextflowFiles"]) -> MetaOapg.properties.otherNextflowFiles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadataModelFile"]) -> MetaOapg.properties.metadataModelFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'Links': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionComment"]) -> MetaOapg.properties.versionComment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["categories"]) -> MetaOapg.properties.categories: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["htmlDocumentation"]) -> MetaOapg.properties.htmlDocumentation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "description", "mainNextflowFile", "parametersXmlFile", "analysisStorageId", "pipelineLanguageVersionId", "nextflowConfigFile", "otherNextflowFiles", "metadataModelFile", "links", "versionComment", "categories", "htmlDocumentation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mainNextflowFile"]) -> MetaOapg.properties.mainNextflowFile: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parametersXmlFile"]) -> MetaOapg.properties.parametersXmlFile: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analysisStorageId"]) -> MetaOapg.properties.analysisStorageId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pipelineLanguageVersionId"]) -> typing.Union[MetaOapg.properties.pipelineLanguageVersionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextflowConfigFile"]) -> typing.Union[MetaOapg.properties.nextflowConfigFile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["otherNextflowFiles"]) -> typing.Union[MetaOapg.properties.otherNextflowFiles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadataModelFile"]) -> typing.Union[MetaOapg.properties.metadataModelFile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['Links', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionComment"]) -> typing.Union[MetaOapg.properties.versionComment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["categories"]) -> typing.Union[MetaOapg.properties.categories, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["htmlDocumentation"]) -> typing.Union[MetaOapg.properties.htmlDocumentation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "description", "mainNextflowFile", "parametersXmlFile", "analysisStorageId", "pipelineLanguageVersionId", "nextflowConfigFile", "otherNextflowFiles", "metadataModelFile", "links", "versionComment", "categories", "htmlDocumentation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        parametersXmlFile: typing.Union[MetaOapg.properties.parametersXmlFile, bytes, io.FileIO, io.BufferedReader, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        mainNextflowFile: typing.Union[MetaOapg.properties.mainNextflowFile, bytes, io.FileIO, io.BufferedReader, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        analysisStorageId: typing.Union[MetaOapg.properties.analysisStorageId, str, uuid.UUID, ],
        pipelineLanguageVersionId: typing.Union[MetaOapg.properties.pipelineLanguageVersionId, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        nextflowConfigFile: typing.Union[MetaOapg.properties.nextflowConfigFile, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        otherNextflowFiles: typing.Union[MetaOapg.properties.otherNextflowFiles, list, tuple, schemas.Unset] = schemas.unset,
        metadataModelFile: typing.Union[MetaOapg.properties.metadataModelFile, None, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        links: typing.Union['Links', schemas.Unset] = schemas.unset,
        versionComment: typing.Union[MetaOapg.properties.versionComment, None, str, schemas.Unset] = schemas.unset,
        categories: typing.Union[MetaOapg.properties.categories, list, tuple, None, schemas.Unset] = schemas.unset,
        htmlDocumentation: typing.Union[MetaOapg.properties.htmlDocumentation, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateNextflowPipeline':
        return super().__new__(
            cls,
            *args,
            parametersXmlFile=parametersXmlFile,
            code=code,
            mainNextflowFile=mainNextflowFile,
            description=description,
            analysisStorageId=analysisStorageId,
            pipelineLanguageVersionId=pipelineLanguageVersionId,
            nextflowConfigFile=nextflowConfigFile,
            otherNextflowFiles=otherNextflowFiles,
            metadataModelFile=metadataModelFile,
            links=links,
            versionComment=versionComment,
            categories=categories,
            htmlDocumentation=htmlDocumentation,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.links import Links
