# coding: utf-8

"""
    StatusCake API

    StatusCake API endpoints to manage monitoring resources.  # Authentication  Documentation on API authentication can be found [here](https://developers.statuscake.com/guides/api/authentication).  # Ratelimiting  Documentation on API ratelimiting can be found [here](https://developers.statuscake.com/guides/api/ratelimiting).  # Errors  Documentation on error handling can be found [here](https://developers.statuscake.com/guides/api/errors).  # Handling Input Parameters  Documentation on input parameters, including how to pass arrays to API endpoints can be found [here](https://developers.statuscake.com/guides/api/parameters). 

    The version of the OpenAPI document: 1.2.0
    Contact: support@statuscake.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from statuscake.models.uptime_test_status import UptimeTestStatus
from typing import Optional, Set
from typing_extensions import Self

class UptimeTestPeriod(BaseModel):
    """
    UptimeTestPeriod
    """ # noqa: E501
    created_at: datetime = Field(description="When the status period was created (RFC3339 format)")
    duration: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Status period duration (ms)")
    ended_at: Optional[datetime] = Field(default=None, description="When the status period ended (RFC3339 format)")
    status: UptimeTestStatus
    __properties: ClassVar[List[str]] = ["created_at", "duration", "ended_at", "status"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UptimeTestPeriod from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UptimeTestPeriod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "duration": obj.get("duration"),
            "ended_at": obj.get("ended_at"),
            "status": obj.get("status")
        })
        return _obj

