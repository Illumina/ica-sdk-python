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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from icasdk.models.region import Region
from icasdk.models.storage_configuration_details import StorageConfigurationDetails
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StorageConfigurationWithDetails(BaseModel):
    """
    StorageConfigurationWithDetails
    """ # noqa: E501
    id: StrictStr
    time_created: datetime = Field(alias="timeCreated")
    time_modified: datetime = Field(alias="timeModified")
    owner_id: StrictStr = Field(alias="ownerId")
    tenant_id: StrictStr = Field(alias="tenantId")
    tenant_name: Optional[StrictStr] = Field(default=None, alias="tenantName")
    name: StrictStr = Field(description="The name of the storage configuration")
    description: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1000)]] = Field(default=None, description="An optional description")
    type: StrictStr
    status: StrictStr
    error_message: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1000)]] = Field(default=None, description="An optional error message when something went wrong with the configuration", alias="errorMessage")
    region: Region
    is_default: StrictBool = Field(description="An indication if this is the default in region for new projects", alias="isDefault")
    storage_configuration_details: StorageConfigurationDetails = Field(alias="storageConfigurationDetails")
    __properties: ClassVar[List[str]] = ["id", "timeCreated", "timeModified", "ownerId", "tenantId", "tenantName", "name", "description", "type", "status", "errorMessage", "region", "isDefault", "storageConfigurationDetails"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('AWS_S3'):
            raise ValueError("must be one of enum values ('AWS_S3')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('INITIALIZING', 'OK', 'ERROR'):
            raise ValueError("must be one of enum values ('INITIALIZING', 'OK', 'ERROR')")
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
        """Create an instance of StorageConfigurationWithDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of region
        if self.region:
            _dict['region'] = self.region.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_configuration_details
        if self.storage_configuration_details:
            _dict['storageConfigurationDetails'] = self.storage_configuration_details.to_dict()
        # set to None if tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_name is None and "tenant_name" in self.model_fields_set:
            _dict['tenantName'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of StorageConfigurationWithDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timeCreated": obj.get("timeCreated"),
            "timeModified": obj.get("timeModified"),
            "ownerId": obj.get("ownerId"),
            "tenantId": obj.get("tenantId"),
            "tenantName": obj.get("tenantName"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "errorMessage": obj.get("errorMessage"),
            "region": Region.from_dict(obj.get("region")) if obj.get("region") is not None else None,
            "isDefault": obj.get("isDefault"),
            "storageConfigurationDetails": StorageConfigurationDetails.from_dict(obj.get("storageConfigurationDetails")) if obj.get("storageConfigurationDetails") is not None else None
        })
        return _obj


