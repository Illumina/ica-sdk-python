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


class WorkflowSession(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "workflow",
            "tenantId",
            "timeCreated",
            "id",
            "userReference",
            "ownerId",
            "status",
            "tags",
        }
        
        class properties:
            id = schemas.UUIDSchema
            timeCreated = schemas.DateTimeSchema
            ownerId = schemas.UUIDSchema
            tenantId = schemas.UUIDSchema
            
            
            class userReference(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def workflow() -> typing.Type['Workflow']:
                return Workflow
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def REQUESTED(cls):
                    return cls("REQUESTED")
                
                @schemas.classproperty
                def AWAITINGINPUT(cls):
                    return cls("AWAITINGINPUT")
                
                @schemas.classproperty
                def INPROGRESS(cls):
                    return cls("INPROGRESS")
                
                @schemas.classproperty
                def SUCCEEDED(cls):
                    return cls("SUCCEEDED")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def FAILEDFINAL(cls):
                    return cls("FAILEDFINAL")
                
                @schemas.classproperty
                def ABORTED(cls):
                    return cls("ABORTED")
        
            @staticmethod
            def tags() -> typing.Type['WorkflowSessionTag']:
                return WorkflowSessionTag
            
            
            class tenantName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tenantName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class startDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'startDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class endDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'endDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class summary(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'summary':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "timeCreated": timeCreated,
                "ownerId": ownerId,
                "tenantId": tenantId,
                "userReference": userReference,
                "workflow": workflow,
                "status": status,
                "tags": tags,
                "tenantName": tenantName,
                "startDate": startDate,
                "endDate": endDate,
                "summary": summary,
            }

    
    workflow: 'Workflow'
    tenantId: MetaOapg.properties.tenantId
    timeCreated: MetaOapg.properties.timeCreated
    id: MetaOapg.properties.id
    userReference: MetaOapg.properties.userReference
    ownerId: MetaOapg.properties.ownerId
    status: MetaOapg.properties.status
    tags: 'WorkflowSessionTag'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userReference"]) -> MetaOapg.properties.userReference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflow"]) -> 'Workflow': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'WorkflowSessionTag': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantName"]) -> MetaOapg.properties.tenantName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["summary"]) -> MetaOapg.properties.summary: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "timeCreated", "ownerId", "tenantId", "userReference", "workflow", "status", "tags", "tenantName", "startDate", "endDate", "summary", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userReference"]) -> MetaOapg.properties.userReference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflow"]) -> 'Workflow': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> 'WorkflowSessionTag': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantName"]) -> typing.Union[MetaOapg.properties.tenantName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["summary"]) -> typing.Union[MetaOapg.properties.summary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "timeCreated", "ownerId", "tenantId", "userReference", "workflow", "status", "tags", "tenantName", "startDate", "endDate", "summary", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        tenantName: typing.Union[MetaOapg.properties.tenantName, None, str, schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, None, str, datetime, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, None, str, datetime, schemas.Unset] = schemas.unset,
        summary: typing.Union[MetaOapg.properties.summary, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowSession':
        return super().__new__(
            cls,
            *args,
            tenantName=tenantName,
            startDate=startDate,
            endDate=endDate,
            summary=summary,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.workflow import Workflow
from icasdk.model.workflow_session_tag import WorkflowSessionTag
