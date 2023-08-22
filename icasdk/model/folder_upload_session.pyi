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


class FolderUploadSession(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "timeSessionExpires",
            "timeCreated",
            "id",
            "status",
        }
        
        class properties:
            id = schemas.StrSchema
            timeCreated = schemas.DateTimeSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("OPEN")
                
                @schemas.classproperty
                def CLOSED(cls):
                    return cls("CLOSED")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
            timeSessionExpires = schemas.DateTimeSchema
            
            
            class timeCompleted(
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
                ) -> 'timeCompleted':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class timeClosed(
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
                ) -> 'timeClosed':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def tempCredentials() -> typing.Type['TempCredentials']:
                return TempCredentials
            __annotations__ = {
                "id": id,
                "timeCreated": timeCreated,
                "status": status,
                "timeSessionExpires": timeSessionExpires,
                "timeCompleted": timeCompleted,
                "timeClosed": timeClosed,
                "tempCredentials": tempCredentials,
            }
    
    timeSessionExpires: MetaOapg.properties.timeSessionExpires
    timeCreated: MetaOapg.properties.timeCreated
    id: MetaOapg.properties.id
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeSessionExpires"]) -> MetaOapg.properties.timeSessionExpires: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeCompleted"]) -> MetaOapg.properties.timeCompleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeClosed"]) -> MetaOapg.properties.timeClosed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempCredentials"]) -> 'TempCredentials': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "timeCreated", "status", "timeSessionExpires", "timeCompleted", "timeClosed", "tempCredentials", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeCreated"]) -> MetaOapg.properties.timeCreated: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeSessionExpires"]) -> MetaOapg.properties.timeSessionExpires: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeCompleted"]) -> typing.Union[MetaOapg.properties.timeCompleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeClosed"]) -> typing.Union[MetaOapg.properties.timeClosed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempCredentials"]) -> typing.Union['TempCredentials', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "timeCreated", "status", "timeSessionExpires", "timeCompleted", "timeClosed", "tempCredentials", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        timeSessionExpires: typing.Union[MetaOapg.properties.timeSessionExpires, str, datetime, ],
        timeCreated: typing.Union[MetaOapg.properties.timeCreated, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        timeCompleted: typing.Union[MetaOapg.properties.timeCompleted, None, str, datetime, schemas.Unset] = schemas.unset,
        timeClosed: typing.Union[MetaOapg.properties.timeClosed, None, str, datetime, schemas.Unset] = schemas.unset,
        tempCredentials: typing.Union['TempCredentials', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FolderUploadSession':
        return super().__new__(
            cls,
            *args,
            timeSessionExpires=timeSessionExpires,
            timeCreated=timeCreated,
            id=id,
            status=status,
            timeCompleted=timeCompleted,
            timeClosed=timeClosed,
            tempCredentials=tempCredentials,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.temp_credentials import TempCredentials
