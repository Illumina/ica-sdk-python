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


class ActivationCodeDetail(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "allowedSlots",
            "originalSlots",
            "pipelineBundle",
            "usedSlots",
            "movedSlots",
            "id",
            "usages",
        }
        
        class properties:
            id = schemas.UUIDSchema
            
            
            class allowedSlots(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = -1
            
            
            class usedSlots(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 0
            
            
            class movedSlots(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 0
            
            
            class originalSlots(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = -1
        
            @staticmethod
            def pipelineBundle() -> typing.Type['PipelineBundle']:
                return PipelineBundle
            
            
            class usages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ActivationCodeDetailUsage']:
                        return ActivationCodeDetailUsage
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ActivationCodeDetailUsage'], typing.List['ActivationCodeDetailUsage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'usages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ActivationCodeDetailUsage':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "allowedSlots": allowedSlots,
                "usedSlots": usedSlots,
                "movedSlots": movedSlots,
                "originalSlots": originalSlots,
                "pipelineBundle": pipelineBundle,
                "usages": usages,
            }
    
    allowedSlots: MetaOapg.properties.allowedSlots
    originalSlots: MetaOapg.properties.originalSlots
    pipelineBundle: 'PipelineBundle'
    usedSlots: MetaOapg.properties.usedSlots
    movedSlots: MetaOapg.properties.movedSlots
    id: MetaOapg.properties.id
    usages: MetaOapg.properties.usages
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedSlots"]) -> MetaOapg.properties.allowedSlots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usedSlots"]) -> MetaOapg.properties.usedSlots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["movedSlots"]) -> MetaOapg.properties.movedSlots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originalSlots"]) -> MetaOapg.properties.originalSlots: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pipelineBundle"]) -> 'PipelineBundle': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usages"]) -> MetaOapg.properties.usages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "allowedSlots", "usedSlots", "movedSlots", "originalSlots", "pipelineBundle", "usages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedSlots"]) -> MetaOapg.properties.allowedSlots: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usedSlots"]) -> MetaOapg.properties.usedSlots: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["movedSlots"]) -> MetaOapg.properties.movedSlots: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originalSlots"]) -> MetaOapg.properties.originalSlots: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pipelineBundle"]) -> 'PipelineBundle': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usages"]) -> MetaOapg.properties.usages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "allowedSlots", "usedSlots", "movedSlots", "originalSlots", "pipelineBundle", "usages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        allowedSlots: typing.Union[MetaOapg.properties.allowedSlots, decimal.Decimal, int, ],
        originalSlots: typing.Union[MetaOapg.properties.originalSlots, decimal.Decimal, int, ],
        pipelineBundle: 'PipelineBundle',
        usedSlots: typing.Union[MetaOapg.properties.usedSlots, decimal.Decimal, int, ],
        movedSlots: typing.Union[MetaOapg.properties.movedSlots, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        usages: typing.Union[MetaOapg.properties.usages, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ActivationCodeDetail':
        return super().__new__(
            cls,
            *args,
            allowedSlots=allowedSlots,
            originalSlots=originalSlots,
            pipelineBundle=pipelineBundle,
            usedSlots=usedSlots,
            movedSlots=movedSlots,
            id=id,
            usages=usages,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.activation_code_detail_usage import ActivationCodeDetailUsage
from icasdk.model.pipeline_bundle import PipelineBundle
