# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    CertificateChainDepth: Optional[float]
    Ciphers: Optional[Sequence[str]]
    ClientCertificateId: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    FallCount: Optional[float]
    Interval: Optional[float]
    IsSecure: Optional[bool]
    MonitorPort: Optional[str]
    Protocols: Optional[Sequence[str]]
    RequestBody: Optional[str]
    RequestMethod: Optional[str]
    RequestUrl: Optional[str]
    RequestVersion: Optional[str]
    ResponseBody: Optional[str]
    ResponseStatusCodes: Optional[Sequence[float]]
    Revision: Optional[float]
    RiseCount: Optional[float]
    ServerAuth: Optional[str]
    ServerAuthCaIds: Optional[Sequence[str]]
    ServerAuthCrlIds: Optional[Sequence[str]]
    Timeout: Optional[float]
    RequestHeader: Optional[Sequence["_RequestHeader"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateChainDepth=json_data.get("CertificateChainDepth"),
            Ciphers=json_data.get("Ciphers"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FallCount=json_data.get("FallCount"),
            Interval=json_data.get("Interval"),
            IsSecure=json_data.get("IsSecure"),
            MonitorPort=json_data.get("MonitorPort"),
            Protocols=json_data.get("Protocols"),
            RequestBody=json_data.get("RequestBody"),
            RequestMethod=json_data.get("RequestMethod"),
            RequestUrl=json_data.get("RequestUrl"),
            RequestVersion=json_data.get("RequestVersion"),
            ResponseBody=json_data.get("ResponseBody"),
            ResponseStatusCodes=json_data.get("ResponseStatusCodes"),
            Revision=json_data.get("Revision"),
            RiseCount=json_data.get("RiseCount"),
            ServerAuth=json_data.get("ServerAuth"),
            ServerAuthCaIds=json_data.get("ServerAuthCaIds"),
            ServerAuthCrlIds=json_data.get("ServerAuthCrlIds"),
            Timeout=json_data.get("Timeout"),
            RequestHeader=json_data.get("RequestHeader"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequestHeader:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeader = RequestHeader


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag

