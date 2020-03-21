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
    AdditionalPrimaries: Optional[Sequence[str]]
    AutogenerateNsRecord: Optional[bool]
    DnsServers: Optional[str]
    Dnssec: Optional[bool]
    Expiry: Optional[float]
    Hostmaster: Optional[str]
    Id: Optional[str]
    Link: Optional[str]
    Networks: Optional[Sequence[float]]
    NxTtl: Optional[float]
    Primary: Optional[str]
    Refresh: Optional[float]
    Retry: Optional[float]
    Ttl: Optional[float]
    Zone: Optional[str]
    Secondaries: Optional[Sequence["_Secondaries"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalPrimaries=json_data.get("AdditionalPrimaries"),
            AutogenerateNsRecord=json_data.get("AutogenerateNsRecord"),
            DnsServers=json_data.get("DnsServers"),
            Dnssec=json_data.get("Dnssec"),
            Expiry=json_data.get("Expiry"),
            Hostmaster=json_data.get("Hostmaster"),
            Id=json_data.get("Id"),
            Link=json_data.get("Link"),
            Networks=json_data.get("Networks"),
            NxTtl=json_data.get("NxTtl"),
            Primary=json_data.get("Primary"),
            Refresh=json_data.get("Refresh"),
            Retry=json_data.get("Retry"),
            Ttl=json_data.get("Ttl"),
            Zone=json_data.get("Zone"),
            Secondaries=json_data.get("Secondaries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Secondaries:
    Ip: Optional[str]
    Notify: Optional[bool]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Secondaries"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secondaries"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Notify=json_data.get("Notify"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secondaries = Secondaries


