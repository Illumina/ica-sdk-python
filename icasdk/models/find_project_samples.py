# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p> 

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from icasdk.models.find_sample_boolean_condition import FindSampleBooleanCondition
from icasdk.models.find_sample_condition import FindSampleCondition
from icasdk.models.find_sample_date_condition import FindSampleDateCondition
from icasdk.models.find_sample_number_condition import FindSampleNumberCondition
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FindProjectSamples(BaseModel):
    """
    FindProjectSamples
    """ # noqa: E501
    conditions: List[FindSampleCondition] = Field(description="Adds a condition on a string field.")
    date_conditions: List[FindSampleDateCondition] = Field(description="Adds a condition on a date metadate field. If both the dateBefore and dateAfter parameter are null it will return any sample that has no value for the date field.", alias="dateConditions")
    number_conditions: List[FindSampleNumberCondition] = Field(description="Adds a condition on a number metadata field. If both the lowerBoundary and upperBoundary parameter are null it will return any sample that has no value for the number field.", alias="numberConditions")
    boolean_conditions: List[FindSampleBooleanCondition] = Field(description="Adds a condition on a boolean field.", alias="booleanConditions")
    full_text_search_string: Optional[StrictStr] = Field(default=None, description="Adds a fuzzy matching condition for the text on all string fields of the sample i.e. on both the fixed fields (name, description) as any metadata text field.", alias="fullTextSearchString")
    include_deleted: Optional[StrictBool] = Field(default=False, description="Indicates whether deleted samples should be included.", alias="includeDeleted")
    user_tags: Optional[List[StrictStr]] = Field(default=None, description="The usertags to filter on. The userTagMatchMode-parameter determines how the filtering is done.", alias="userTags")
    user_tag_match_mode: Optional[StrictStr] = Field(default=None, description="How the usertags are filtered.", alias="userTagMatchMode")
    run_input_tags: Optional[List[StrictStr]] = Field(default=None, description="The runInputTags to filter on. The runInputTagMatchMode-parameter determines how the filtering is done.", alias="runInputTags")
    run_input_tag_match_mode: Optional[StrictStr] = Field(default=None, description="How the runInputTags are filtered.", alias="runInputTagMatchMode")
    connector_tags: Optional[List[StrictStr]] = Field(default=None, description="The connectorTags to filter on. The connectorTagMatchMode-parameter determines how the filtering is done.", alias="connectorTags")
    connector_tag_match_mode: Optional[StrictStr] = Field(default=None, description="How the connectorTags are filtered.", alias="connectorTagMatchMode")
    tech_tags: Optional[List[StrictStr]] = Field(default=None, description="The technicalTags to filter on. The techTagMatchMode-parameter determines how the filtering is done.", alias="techTags")
    tech_tag_match_mode: Optional[StrictStr] = Field(default=None, description="How the technicalTags are filtered.", alias="techTagMatchMode")
    instrument_run_ids: Optional[List[StrictStr]] = Field(default=None, alias="instrumentRunIds")
    __properties: ClassVar[List[str]] = ["conditions", "dateConditions", "numberConditions", "booleanConditions", "fullTextSearchString", "includeDeleted", "userTags", "userTagMatchMode", "runInputTags", "runInputTagMatchMode", "connectorTags", "connectorTagMatchMode", "techTags", "techTagMatchMode", "instrumentRunIds"]

    @field_validator('user_tag_match_mode')
    def user_tag_match_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EXACT', 'EXCLUDE', 'FUZZY'):
            raise ValueError("must be one of enum values ('EXACT', 'EXCLUDE', 'FUZZY')")
        return value

    @field_validator('run_input_tag_match_mode')
    def run_input_tag_match_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EXACT', 'EXCLUDE', 'FUZZY'):
            raise ValueError("must be one of enum values ('EXACT', 'EXCLUDE', 'FUZZY')")
        return value

    @field_validator('connector_tag_match_mode')
    def connector_tag_match_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EXACT', 'EXCLUDE', 'FUZZY'):
            raise ValueError("must be one of enum values ('EXACT', 'EXCLUDE', 'FUZZY')")
        return value

    @field_validator('tech_tag_match_mode')
    def tech_tag_match_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EXACT', 'EXCLUDE', 'FUZZY'):
            raise ValueError("must be one of enum values ('EXACT', 'EXCLUDE', 'FUZZY')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FindProjectSamples from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in date_conditions (list)
        _items = []
        if self.date_conditions:
            for _item in self.date_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dateConditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in number_conditions (list)
        _items = []
        if self.number_conditions:
            for _item in self.number_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['numberConditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in boolean_conditions (list)
        _items = []
        if self.boolean_conditions:
            for _item in self.boolean_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['booleanConditions'] = _items
        # set to None if full_text_search_string (nullable) is None
        # and model_fields_set contains the field
        if self.full_text_search_string is None and "full_text_search_string" in self.model_fields_set:
            _dict['fullTextSearchString'] = None

        # set to None if include_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.include_deleted is None and "include_deleted" in self.model_fields_set:
            _dict['includeDeleted'] = None

        # set to None if user_tags (nullable) is None
        # and model_fields_set contains the field
        if self.user_tags is None and "user_tags" in self.model_fields_set:
            _dict['userTags'] = None

        # set to None if user_tag_match_mode (nullable) is None
        # and model_fields_set contains the field
        if self.user_tag_match_mode is None and "user_tag_match_mode" in self.model_fields_set:
            _dict['userTagMatchMode'] = None

        # set to None if run_input_tags (nullable) is None
        # and model_fields_set contains the field
        if self.run_input_tags is None and "run_input_tags" in self.model_fields_set:
            _dict['runInputTags'] = None

        # set to None if run_input_tag_match_mode (nullable) is None
        # and model_fields_set contains the field
        if self.run_input_tag_match_mode is None and "run_input_tag_match_mode" in self.model_fields_set:
            _dict['runInputTagMatchMode'] = None

        # set to None if connector_tags (nullable) is None
        # and model_fields_set contains the field
        if self.connector_tags is None and "connector_tags" in self.model_fields_set:
            _dict['connectorTags'] = None

        # set to None if connector_tag_match_mode (nullable) is None
        # and model_fields_set contains the field
        if self.connector_tag_match_mode is None and "connector_tag_match_mode" in self.model_fields_set:
            _dict['connectorTagMatchMode'] = None

        # set to None if tech_tags (nullable) is None
        # and model_fields_set contains the field
        if self.tech_tags is None and "tech_tags" in self.model_fields_set:
            _dict['techTags'] = None

        # set to None if tech_tag_match_mode (nullable) is None
        # and model_fields_set contains the field
        if self.tech_tag_match_mode is None and "tech_tag_match_mode" in self.model_fields_set:
            _dict['techTagMatchMode'] = None

        # set to None if instrument_run_ids (nullable) is None
        # and model_fields_set contains the field
        if self.instrument_run_ids is None and "instrument_run_ids" in self.model_fields_set:
            _dict['instrumentRunIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FindProjectSamples from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conditions": [FindSampleCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "dateConditions": [FindSampleDateCondition.from_dict(_item) for _item in obj.get("dateConditions")] if obj.get("dateConditions") is not None else None,
            "numberConditions": [FindSampleNumberCondition.from_dict(_item) for _item in obj.get("numberConditions")] if obj.get("numberConditions") is not None else None,
            "booleanConditions": [FindSampleBooleanCondition.from_dict(_item) for _item in obj.get("booleanConditions")] if obj.get("booleanConditions") is not None else None,
            "fullTextSearchString": obj.get("fullTextSearchString"),
            "includeDeleted": obj.get("includeDeleted") if obj.get("includeDeleted") is not None else False,
            "userTags": obj.get("userTags"),
            "userTagMatchMode": obj.get("userTagMatchMode"),
            "runInputTags": obj.get("runInputTags"),
            "runInputTagMatchMode": obj.get("runInputTagMatchMode"),
            "connectorTags": obj.get("connectorTags"),
            "connectorTagMatchMode": obj.get("connectorTagMatchMode"),
            "techTags": obj.get("techTags"),
            "techTagMatchMode": obj.get("techTagMatchMode"),
            "instrumentRunIds": obj.get("instrumentRunIds")
        })
        return _obj


