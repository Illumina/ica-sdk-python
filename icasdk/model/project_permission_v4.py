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


class ProjectPermissionV4(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "uploadAllowed",
            "membershipType",
            "roleFlow",
            "roleBase",
            "tenantId",
            "downloadAllowed",
            "timeCreated",
            "id",
            "ownerId",
            "roleBench",
            "roleProject",
            "timeModified",
        }
        
        class properties:
            id = schemas.UUIDSchema
            timeCreated = schemas.DateTimeSchema
            timeModified = schemas.DateTimeSchema
            ownerId = schemas.UUIDSchema
            tenantId = schemas.UUIDSchema
            roleProject = schemas.StrSchema
            roleFlow = schemas.StrSchema
            roleBase = schemas.StrSchema
            roleBench = schemas.StrSchema
            
            
            class membershipType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "USER": "USER",
                        "EMAIL": "EMAIL",
                        "WORKGROUP": "WORKGROUP",
                    }
                
                @schemas.classproperty
                def USER(cls):
                    return cls("USER")
                
                @schemas.classproperty
                def EMAIL(cls):
                    return cls("EMAIL")
                
                @schemas.classproperty
                def WORKGROUP(cls):
                    return cls("WORKGROUP")
            uploadAllowed = schemas.BoolSchema
            downloadAllowed = schemas.BoolSchema
            
            
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
        
            @staticmethod
            def user() -> typing.Type['User']:
                return User
            
            
            class emailAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emailAddress':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def workgroup() -> typing.Type['Workgroup']:
                return Workgroup
            
            
            class invitationAccepted(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'invitationAccepted':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class invitationRejected(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'invitationRejected':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "timeCreated": timeCreated,
                "timeModified": timeModified,
                "ownerId": ownerId,
                "tenantId": tenantId,
                "roleProject": roleProject,
                "roleFlow": roleFlow,
                "roleBase": roleBase,
                "roleBench": roleBench,
                "membershipType": membershipType,
                "uploadAllowed": uploadAllowed,
                "downloadAllowed": downloadAllowed,
                "tenantName": tenantName,
                "user": user,
                "emailAddress": emailAddress,
                "workgroup": workgroup,
                "invitationAccepted": invitationAccepted,
                "invitationRejected": invitationRejected,
            }
    
    uploadAllowed: MetaOapg.properties.uploadAllowed
    membershipType: MetaOapg.properties.membershipType
    roleFlow: MetaOapg.properties.roleFlow
    roleBase: MetaOapg.properties.roleBase
    tenantId: MetaOapg.properties.tenantId
    downloadAllowed: MetaOapg.properties.downloadAllowed
    timeCreated: MetaOapg.properties.timeCreated
    id: MetaOapg.properties.id
    ownerId: MetaOapg.properties.ownerId
    roleBench: MetaOapg.properties.roleBench
    roleProject: MetaOapg.properties.roleProject
    timeModified: MetaOapg.properties.timeModified
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeModified"]) -> MetaOapg.properties.timeModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleProject"]) -> MetaOapg.properties.roleProject: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleFlow"]) -> MetaOapg.properties.roleFlow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleBase"]) -> MetaOapg.properties.roleBase: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleBench"]) -> MetaOapg.properties.roleBench: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["membershipType"]) -> MetaOapg.properties.membershipType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uploadAllowed"]) -> MetaOapg.properties.uploadAllowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["downloadAllowed"]) -> MetaOapg.properties.downloadAllowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantName"]) -> MetaOapg.properties.tenantName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'User': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workgroup"]) -> 'Workgroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invitationAccepted"]) -> MetaOapg.properties.invitationAccepted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invitationRejected"]) -> MetaOapg.properties.invitationRejected: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "timeCreated", "timeModified", "ownerId", "tenantId", "roleProject", "roleFlow", "roleBase", "roleBench", "membershipType", "uploadAllowed", "downloadAllowed", "tenantName", "user", "emailAddress", "workgroup", "invitationAccepted", "invitationRejected", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeModified"]) -> MetaOapg.properties.timeModified: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownerId"]) -> MetaOapg.properties.ownerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantId"]) -> MetaOapg.properties.tenantId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleProject"]) -> MetaOapg.properties.roleProject: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleFlow"]) -> MetaOapg.properties.roleFlow: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleBase"]) -> MetaOapg.properties.roleBase: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleBench"]) -> MetaOapg.properties.roleBench: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["membershipType"]) -> MetaOapg.properties.membershipType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uploadAllowed"]) -> MetaOapg.properties.uploadAllowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["downloadAllowed"]) -> MetaOapg.properties.downloadAllowed: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantName"]) -> typing.Union[MetaOapg.properties.tenantName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union['User', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailAddress"]) -> typing.Union[MetaOapg.properties.emailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workgroup"]) -> typing.Union['Workgroup', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invitationAccepted"]) -> typing.Union[MetaOapg.properties.invitationAccepted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invitationRejected"]) -> typing.Union[MetaOapg.properties.invitationRejected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "timeCreated", "timeModified", "ownerId", "tenantId", "roleProject", "roleFlow", "roleBase", "roleBench", "membershipType", "uploadAllowed", "downloadAllowed", "tenantName", "user", "emailAddress", "workgroup", "invitationAccepted", "invitationRejected", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uploadAllowed: typing.Union[MetaOapg.properties.uploadAllowed, bool, ],
        membershipType: typing.Union[MetaOapg.properties.membershipType, str, ],
        roleFlow: typing.Union[MetaOapg.properties.roleFlow, str, ],
        roleBase: typing.Union[MetaOapg.properties.roleBase, str, ],
        tenantId: typing.Union[MetaOapg.properties.tenantId, str, uuid.UUID, ],
        downloadAllowed: typing.Union[MetaOapg.properties.downloadAllowed, bool, ],
        timeCreated: typing.Union[MetaOapg.properties.timeCreated, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        ownerId: typing.Union[MetaOapg.properties.ownerId, str, uuid.UUID, ],
        roleBench: typing.Union[MetaOapg.properties.roleBench, str, ],
        roleProject: typing.Union[MetaOapg.properties.roleProject, str, ],
        timeModified: typing.Union[MetaOapg.properties.timeModified, str, datetime, ],
        tenantName: typing.Union[MetaOapg.properties.tenantName, None, str, schemas.Unset] = schemas.unset,
        user: typing.Union['User', schemas.Unset] = schemas.unset,
        emailAddress: typing.Union[MetaOapg.properties.emailAddress, None, str, schemas.Unset] = schemas.unset,
        workgroup: typing.Union['Workgroup', schemas.Unset] = schemas.unset,
        invitationAccepted: typing.Union[MetaOapg.properties.invitationAccepted, None, bool, schemas.Unset] = schemas.unset,
        invitationRejected: typing.Union[MetaOapg.properties.invitationRejected, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectPermissionV4':
        return super().__new__(
            cls,
            *args,
            uploadAllowed=uploadAllowed,
            membershipType=membershipType,
            roleFlow=roleFlow,
            roleBase=roleBase,
            tenantId=tenantId,
            downloadAllowed=downloadAllowed,
            timeCreated=timeCreated,
            id=id,
            ownerId=ownerId,
            roleBench=roleBench,
            roleProject=roleProject,
            timeModified=timeModified,
            tenantName=tenantName,
            user=user,
            emailAddress=emailAddress,
            workgroup=workgroup,
            invitationAccepted=invitationAccepted,
            invitationRejected=invitationRejected,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.user import User
from icasdk.model.workgroup import Workgroup
