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
from icasdk.models.user import User
from icasdk.models.workgroup import Workgroup
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectPermissionV4(BaseModel):
    """
    ProjectPermissionV4
    """ # noqa: E501
    id: StrictStr
    time_created: datetime = Field(alias="timeCreated")
    time_modified: datetime = Field(alias="timeModified")
    owner_id: StrictStr = Field(alias="ownerId")
    tenant_id: StrictStr = Field(alias="tenantId")
    tenant_name: Optional[StrictStr] = Field(default=None, alias="tenantName")
    role_project: StrictStr = Field(description="Possible values are: NONE, VIEWER, CONTRIBUTOR, ADMINISTRATOR, DATA_PROVIDER. More types could be added in a future release.", alias="roleProject")
    role_flow: StrictStr = Field(description="Possible values are: NONE, VIEWER, CONTRIBUTOR. More types could be added in a future release.", alias="roleFlow")
    role_base: StrictStr = Field(description="Possible values are: NONE, VIEWER, CONTRIBUTOR. More types could be added in a future release.", alias="roleBase")
    role_bench: StrictStr = Field(description="Possible values are: NONE, CONTRIBUTOR, ADMINISTRATOR. More types could be added in a future release.", alias="roleBench")
    membership_type: StrictStr = Field(alias="membershipType")
    user: Optional[User] = None
    email_address: Optional[StrictStr] = Field(default=None, description="Only present when membershipType is EMAIL", alias="emailAddress")
    workgroup: Optional[Workgroup] = None
    invitation_accepted: Optional[StrictBool] = Field(default=None, description="Only present when membershipType is EMAIL", alias="invitationAccepted")
    invitation_rejected: Optional[StrictBool] = Field(default=None, description="Only present when user is invited by EMAIL", alias="invitationRejected")
    upload_allowed: StrictBool = Field(alias="uploadAllowed")
    download_allowed: StrictBool = Field(alias="downloadAllowed")
    __properties: ClassVar[List[str]] = ["id", "timeCreated", "timeModified", "ownerId", "tenantId", "tenantName", "roleProject", "roleFlow", "roleBase", "roleBench", "membershipType", "user", "emailAddress", "workgroup", "invitationAccepted", "invitationRejected", "uploadAllowed", "downloadAllowed"]

    @field_validator('membership_type')
    def membership_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('USER', 'EMAIL', 'WORKGROUP'):
            raise ValueError("must be one of enum values ('USER', 'EMAIL', 'WORKGROUP')")
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
        """Create an instance of ProjectPermissionV4 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of workgroup
        if self.workgroup:
            _dict['workgroup'] = self.workgroup.to_dict()
        # set to None if tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_name is None and "tenant_name" in self.model_fields_set:
            _dict['tenantName'] = None

        # set to None if email_address (nullable) is None
        # and model_fields_set contains the field
        if self.email_address is None and "email_address" in self.model_fields_set:
            _dict['emailAddress'] = None

        # set to None if invitation_accepted (nullable) is None
        # and model_fields_set contains the field
        if self.invitation_accepted is None and "invitation_accepted" in self.model_fields_set:
            _dict['invitationAccepted'] = None

        # set to None if invitation_rejected (nullable) is None
        # and model_fields_set contains the field
        if self.invitation_rejected is None and "invitation_rejected" in self.model_fields_set:
            _dict['invitationRejected'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectPermissionV4 from a dict"""
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
            "roleProject": obj.get("roleProject"),
            "roleFlow": obj.get("roleFlow"),
            "roleBase": obj.get("roleBase"),
            "roleBench": obj.get("roleBench"),
            "membershipType": obj.get("membershipType"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "emailAddress": obj.get("emailAddress"),
            "workgroup": Workgroup.from_dict(obj.get("workgroup")) if obj.get("workgroup") is not None else None,
            "invitationAccepted": obj.get("invitationAccepted"),
            "invitationRejected": obj.get("invitationRejected"),
            "uploadAllowed": obj.get("uploadAllowed"),
            "downloadAllowed": obj.get("downloadAllowed")
        })
        return _obj


