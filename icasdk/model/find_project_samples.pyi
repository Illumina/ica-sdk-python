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


class FindProjectSamples(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "dateConditions",
            "numberConditions",
            "booleanConditions",
            "conditions",
        }
        
        class properties:
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FindSampleCondition']:
                        return FindSampleCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FindSampleCondition'], typing.List['FindSampleCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FindSampleCondition':
                    return super().__getitem__(i)
            
            
            class dateConditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FindSampleDateCondition']:
                        return FindSampleDateCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FindSampleDateCondition'], typing.List['FindSampleDateCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dateConditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FindSampleDateCondition':
                    return super().__getitem__(i)
            
            
            class numberConditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FindSampleNumberCondition']:
                        return FindSampleNumberCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FindSampleNumberCondition'], typing.List['FindSampleNumberCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'numberConditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FindSampleNumberCondition':
                    return super().__getitem__(i)
            
            
            class booleanConditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FindSampleBooleanCondition']:
                        return FindSampleBooleanCondition
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FindSampleBooleanCondition'], typing.List['FindSampleBooleanCondition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'booleanConditions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FindSampleBooleanCondition':
                    return super().__getitem__(i)
            
            
            class fullTextSearchString(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fullTextSearchString':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class includeDeleted(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'includeDeleted':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class userTags(
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
                ) -> 'userTags':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class userTagMatchMode(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXACT": "EXACT",
                        "EXCLUDE": "EXCLUDE",
                        "FUZZY": "FUZZY",
                    }
                
                @schemas.classproperty
                def EXACT(cls):
                    return cls("EXACT")
                
                @schemas.classproperty
                def EXCLUDE(cls):
                    return cls("EXCLUDE")
                
                @schemas.classproperty
                def FUZZY(cls):
                    return cls("FUZZY")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'userTagMatchMode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class runInputTags(
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
                ) -> 'runInputTags':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class runInputTagMatchMode(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXACT": "EXACT",
                        "EXCLUDE": "EXCLUDE",
                        "FUZZY": "FUZZY",
                    }
                
                @schemas.classproperty
                def EXACT(cls):
                    return cls("EXACT")
                
                @schemas.classproperty
                def EXCLUDE(cls):
                    return cls("EXCLUDE")
                
                @schemas.classproperty
                def FUZZY(cls):
                    return cls("FUZZY")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'runInputTagMatchMode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class connectorTags(
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
                ) -> 'connectorTags':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class connectorTagMatchMode(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXACT": "EXACT",
                        "EXCLUDE": "EXCLUDE",
                        "FUZZY": "FUZZY",
                    }
                
                @schemas.classproperty
                def EXACT(cls):
                    return cls("EXACT")
                
                @schemas.classproperty
                def EXCLUDE(cls):
                    return cls("EXCLUDE")
                
                @schemas.classproperty
                def FUZZY(cls):
                    return cls("FUZZY")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'connectorTagMatchMode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class techTags(
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
                ) -> 'techTags':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class techTagMatchMode(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXACT": "EXACT",
                        "EXCLUDE": "EXCLUDE",
                        "FUZZY": "FUZZY",
                    }
                
                @schemas.classproperty
                def EXACT(cls):
                    return cls("EXACT")
                
                @schemas.classproperty
                def EXCLUDE(cls):
                    return cls("EXCLUDE")
                
                @schemas.classproperty
                def FUZZY(cls):
                    return cls("FUZZY")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'techTagMatchMode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class instrumentRunIds(
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
                ) -> 'instrumentRunIds':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "conditions": conditions,
                "dateConditions": dateConditions,
                "numberConditions": numberConditions,
                "booleanConditions": booleanConditions,
                "fullTextSearchString": fullTextSearchString,
                "includeDeleted": includeDeleted,
                "userTags": userTags,
                "userTagMatchMode": userTagMatchMode,
                "runInputTags": runInputTags,
                "runInputTagMatchMode": runInputTagMatchMode,
                "connectorTags": connectorTags,
                "connectorTagMatchMode": connectorTagMatchMode,
                "techTags": techTags,
                "techTagMatchMode": techTagMatchMode,
                "instrumentRunIds": instrumentRunIds,
            }
    
    dateConditions: MetaOapg.properties.dateConditions
    numberConditions: MetaOapg.properties.numberConditions
    booleanConditions: MetaOapg.properties.booleanConditions
    conditions: MetaOapg.properties.conditions
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateConditions"]) -> MetaOapg.properties.dateConditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberConditions"]) -> MetaOapg.properties.numberConditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["booleanConditions"]) -> MetaOapg.properties.booleanConditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullTextSearchString"]) -> MetaOapg.properties.fullTextSearchString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeDeleted"]) -> MetaOapg.properties.includeDeleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userTags"]) -> MetaOapg.properties.userTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userTagMatchMode"]) -> MetaOapg.properties.userTagMatchMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runInputTags"]) -> MetaOapg.properties.runInputTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runInputTagMatchMode"]) -> MetaOapg.properties.runInputTagMatchMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectorTags"]) -> MetaOapg.properties.connectorTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectorTagMatchMode"]) -> MetaOapg.properties.connectorTagMatchMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["techTags"]) -> MetaOapg.properties.techTags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["techTagMatchMode"]) -> MetaOapg.properties.techTagMatchMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instrumentRunIds"]) -> MetaOapg.properties.instrumentRunIds: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conditions", "dateConditions", "numberConditions", "booleanConditions", "fullTextSearchString", "includeDeleted", "userTags", "userTagMatchMode", "runInputTags", "runInputTagMatchMode", "connectorTags", "connectorTagMatchMode", "techTags", "techTagMatchMode", "instrumentRunIds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateConditions"]) -> MetaOapg.properties.dateConditions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberConditions"]) -> MetaOapg.properties.numberConditions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["booleanConditions"]) -> MetaOapg.properties.booleanConditions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullTextSearchString"]) -> typing.Union[MetaOapg.properties.fullTextSearchString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeDeleted"]) -> typing.Union[MetaOapg.properties.includeDeleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userTags"]) -> typing.Union[MetaOapg.properties.userTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userTagMatchMode"]) -> typing.Union[MetaOapg.properties.userTagMatchMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runInputTags"]) -> typing.Union[MetaOapg.properties.runInputTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runInputTagMatchMode"]) -> typing.Union[MetaOapg.properties.runInputTagMatchMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectorTags"]) -> typing.Union[MetaOapg.properties.connectorTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectorTagMatchMode"]) -> typing.Union[MetaOapg.properties.connectorTagMatchMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["techTags"]) -> typing.Union[MetaOapg.properties.techTags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["techTagMatchMode"]) -> typing.Union[MetaOapg.properties.techTagMatchMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instrumentRunIds"]) -> typing.Union[MetaOapg.properties.instrumentRunIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conditions", "dateConditions", "numberConditions", "booleanConditions", "fullTextSearchString", "includeDeleted", "userTags", "userTagMatchMode", "runInputTags", "runInputTagMatchMode", "connectorTags", "connectorTagMatchMode", "techTags", "techTagMatchMode", "instrumentRunIds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dateConditions: typing.Union[MetaOapg.properties.dateConditions, list, tuple, ],
        numberConditions: typing.Union[MetaOapg.properties.numberConditions, list, tuple, ],
        booleanConditions: typing.Union[MetaOapg.properties.booleanConditions, list, tuple, ],
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, ],
        fullTextSearchString: typing.Union[MetaOapg.properties.fullTextSearchString, None, str, schemas.Unset] = schemas.unset,
        includeDeleted: typing.Union[MetaOapg.properties.includeDeleted, None, bool, schemas.Unset] = schemas.unset,
        userTags: typing.Union[MetaOapg.properties.userTags, list, tuple, None, schemas.Unset] = schemas.unset,
        userTagMatchMode: typing.Union[MetaOapg.properties.userTagMatchMode, None, str, schemas.Unset] = schemas.unset,
        runInputTags: typing.Union[MetaOapg.properties.runInputTags, list, tuple, None, schemas.Unset] = schemas.unset,
        runInputTagMatchMode: typing.Union[MetaOapg.properties.runInputTagMatchMode, None, str, schemas.Unset] = schemas.unset,
        connectorTags: typing.Union[MetaOapg.properties.connectorTags, list, tuple, None, schemas.Unset] = schemas.unset,
        connectorTagMatchMode: typing.Union[MetaOapg.properties.connectorTagMatchMode, None, str, schemas.Unset] = schemas.unset,
        techTags: typing.Union[MetaOapg.properties.techTags, list, tuple, None, schemas.Unset] = schemas.unset,
        techTagMatchMode: typing.Union[MetaOapg.properties.techTagMatchMode, None, str, schemas.Unset] = schemas.unset,
        instrumentRunIds: typing.Union[MetaOapg.properties.instrumentRunIds, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FindProjectSamples':
        return super().__new__(
            cls,
            *args,
            dateConditions=dateConditions,
            numberConditions=numberConditions,
            booleanConditions=booleanConditions,
            conditions=conditions,
            fullTextSearchString=fullTextSearchString,
            includeDeleted=includeDeleted,
            userTags=userTags,
            userTagMatchMode=userTagMatchMode,
            runInputTags=runInputTags,
            runInputTagMatchMode=runInputTagMatchMode,
            connectorTags=connectorTags,
            connectorTagMatchMode=connectorTagMatchMode,
            techTags=techTags,
            techTagMatchMode=techTagMatchMode,
            instrumentRunIds=instrumentRunIds,
            _configuration=_configuration,
            **kwargs,
        )

from icasdk.model.find_sample_boolean_condition import FindSampleBooleanCondition
from icasdk.model.find_sample_condition import FindSampleCondition
from icasdk.model.find_sample_date_condition import FindSampleDateCondition
from icasdk.model.find_sample_number_condition import FindSampleNumberCondition
