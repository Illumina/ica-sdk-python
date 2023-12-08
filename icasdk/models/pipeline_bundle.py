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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from icasdk.models.analysis_storage import AnalysisStorage
from icasdk.models.pipeline import Pipeline
from icasdk.models.region import Region
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PipelineBundle(BaseModel):
    """
    PipelineBundle
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    max_number_of_allowed_slots: Annotated[int, Field(strict=True, ge=-1)] = Field(alias="maxNumberOfAllowedSlots")
    active_pipelines: List[Pipeline] = Field(alias="activePipelines")
    canceled_pipelines: List[Pipeline] = Field(alias="canceledPipelines")
    retired_pipelines: List[Pipeline] = Field(alias="retiredPipelines")
    regions: List[Region]
    analysis_storages: List[AnalysisStorage] = Field(alias="analysisStorages")
    __properties: ClassVar[List[str]] = ["id", "name", "maxNumberOfAllowedSlots", "activePipelines", "canceledPipelines", "retiredPipelines", "regions", "analysisStorages"]

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
        """Create an instance of PipelineBundle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in active_pipelines (list)
        _items = []
        if self.active_pipelines:
            for _item in self.active_pipelines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['activePipelines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in canceled_pipelines (list)
        _items = []
        if self.canceled_pipelines:
            for _item in self.canceled_pipelines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['canceledPipelines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in retired_pipelines (list)
        _items = []
        if self.retired_pipelines:
            for _item in self.retired_pipelines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['retiredPipelines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in regions (list)
        _items = []
        if self.regions:
            for _item in self.regions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['regions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in analysis_storages (list)
        _items = []
        if self.analysis_storages:
            for _item in self.analysis_storages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['analysisStorages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PipelineBundle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "maxNumberOfAllowedSlots": obj.get("maxNumberOfAllowedSlots"),
            "activePipelines": [Pipeline.from_dict(_item) for _item in obj.get("activePipelines")] if obj.get("activePipelines") is not None else None,
            "canceledPipelines": [Pipeline.from_dict(_item) for _item in obj.get("canceledPipelines")] if obj.get("canceledPipelines") is not None else None,
            "retiredPipelines": [Pipeline.from_dict(_item) for _item in obj.get("retiredPipelines")] if obj.get("retiredPipelines") is not None else None,
            "regions": [Region.from_dict(_item) for _item in obj.get("regions")] if obj.get("regions") is not None else None,
            "analysisStorages": [AnalysisStorage.from_dict(_item) for _item in obj.get("analysisStorages")] if obj.get("analysisStorages") is not None else None
        })
        return _obj


