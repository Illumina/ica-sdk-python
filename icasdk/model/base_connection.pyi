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


class BaseConnection(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "databaseName",
            "roleName",
            "dnsName",
            "accessToken",
            "schemaName",
            "authenticator",
            "warehouseName",
            "userPrincipalName",
        }
        
        class properties:
            authenticator = schemas.StrSchema
            accessToken = schemas.StrSchema
            dnsName = schemas.StrSchema
            userPrincipalName = schemas.StrSchema
            databaseName = schemas.StrSchema
            schemaName = schemas.StrSchema
            warehouseName = schemas.StrSchema
            roleName = schemas.StrSchema
            __annotations__ = {
                "authenticator": authenticator,
                "accessToken": accessToken,
                "dnsName": dnsName,
                "userPrincipalName": userPrincipalName,
                "databaseName": databaseName,
                "schemaName": schemaName,
                "warehouseName": warehouseName,
                "roleName": roleName,
            }
    
    databaseName: MetaOapg.properties.databaseName
    roleName: MetaOapg.properties.roleName
    dnsName: MetaOapg.properties.dnsName
    accessToken: MetaOapg.properties.accessToken
    schemaName: MetaOapg.properties.schemaName
    authenticator: MetaOapg.properties.authenticator
    warehouseName: MetaOapg.properties.warehouseName
    userPrincipalName: MetaOapg.properties.userPrincipalName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authenticator"]) -> MetaOapg.properties.authenticator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessToken"]) -> MetaOapg.properties.accessToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dnsName"]) -> MetaOapg.properties.dnsName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userPrincipalName"]) -> MetaOapg.properties.userPrincipalName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["databaseName"]) -> MetaOapg.properties.databaseName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schemaName"]) -> MetaOapg.properties.schemaName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warehouseName"]) -> MetaOapg.properties.warehouseName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roleName"]) -> MetaOapg.properties.roleName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authenticator", "accessToken", "dnsName", "userPrincipalName", "databaseName", "schemaName", "warehouseName", "roleName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authenticator"]) -> MetaOapg.properties.authenticator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessToken"]) -> MetaOapg.properties.accessToken: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dnsName"]) -> MetaOapg.properties.dnsName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userPrincipalName"]) -> MetaOapg.properties.userPrincipalName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["databaseName"]) -> MetaOapg.properties.databaseName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schemaName"]) -> MetaOapg.properties.schemaName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warehouseName"]) -> MetaOapg.properties.warehouseName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roleName"]) -> MetaOapg.properties.roleName: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authenticator", "accessToken", "dnsName", "userPrincipalName", "databaseName", "schemaName", "warehouseName", "roleName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        databaseName: typing.Union[MetaOapg.properties.databaseName, str, ],
        roleName: typing.Union[MetaOapg.properties.roleName, str, ],
        dnsName: typing.Union[MetaOapg.properties.dnsName, str, ],
        accessToken: typing.Union[MetaOapg.properties.accessToken, str, ],
        schemaName: typing.Union[MetaOapg.properties.schemaName, str, ],
        authenticator: typing.Union[MetaOapg.properties.authenticator, str, ],
        warehouseName: typing.Union[MetaOapg.properties.warehouseName, str, ],
        userPrincipalName: typing.Union[MetaOapg.properties.userPrincipalName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BaseConnection':
        return super().__new__(
            cls,
            *args,
            databaseName=databaseName,
            roleName=roleName,
            dnsName=dnsName,
            accessToken=accessToken,
            schemaName=schemaName,
            authenticator=authenticator,
            warehouseName=warehouseName,
            userPrincipalName=userPrincipalName,
            _configuration=_configuration,
            **kwargs,
        )
