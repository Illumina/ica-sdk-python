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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from icasdk.models.analysis_data_input import AnalysisDataInput
from icasdk.models.analysis_parameter_input import AnalysisParameterInput
from icasdk.models.analysis_reference_data_parameter import AnalysisReferenceDataParameter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CwlAnalysisStructuredInput(BaseModel):
    """
    CwlAnalysisStructuredInput
    """ # noqa: E501
    object_type: StrictStr = Field(alias="objectType")
    inputs: List[AnalysisDataInput]
    parameters: Optional[List[AnalysisParameterInput]] = None
    reference_data_parameters: Optional[List[AnalysisReferenceDataParameter]] = Field(default=None, alias="referenceDataParameters")
    __properties: ClassVar[List[str]] = ["objectType", "inputs", "parameters", "referenceDataParameters"]

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('STRUCTURED', 'JSON'):
            raise ValueError("must be one of enum values ('STRUCTURED', 'JSON')")
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
        """Create an instance of CwlAnalysisStructuredInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in inputs (list)
        _items = []
        if self.inputs:
            for _item in self.inputs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reference_data_parameters (list)
        _items = []
        if self.reference_data_parameters:
            for _item in self.reference_data_parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['referenceDataParameters'] = _items
        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        # set to None if reference_data_parameters (nullable) is None
        # and model_fields_set contains the field
        if self.reference_data_parameters is None and "reference_data_parameters" in self.model_fields_set:
            _dict['referenceDataParameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CwlAnalysisStructuredInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objectType": obj.get("objectType"),
            "inputs": [AnalysisDataInput.from_dict(_item) for _item in obj.get("inputs")] if obj.get("inputs") is not None else None,
            "parameters": [AnalysisParameterInput.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None,
            "referenceDataParameters": [AnalysisReferenceDataParameter.from_dict(_item) for _item in obj.get("referenceDataParameters")] if obj.get("referenceDataParameters") is not None else None
        })
        return _obj

