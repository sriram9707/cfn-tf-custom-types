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
    AccessPrivateIpv4: Optional[str]
    AccessPublicIpv4: Optional[str]
    AccessPublicIpv6: Optional[str]
    AlwaysPxe: Optional[bool]
    BillingCycle: Optional[str]
    Created: Optional[str]
    DeployedFacility: Optional[str]
    Description: Optional[str]
    Facilities: Optional[Sequence[str]]
    Facility: Optional[str]
    ForceDetachVolumes: Optional[bool]
    HardwareReservationId: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    IpAddressTypes: Optional[Sequence[str]]
    IpxeScriptUrl: Optional[str]
    Locked: Optional[bool]
    Network: Optional[Sequence["_Network"]]
    NetworkType: Optional[str]
    OperatingSystem: Optional[str]
    Plan: Optional[str]
    Ports: Optional[Sequence["_Ports"]]
    ProjectId: Optional[str]
    ProjectSshKeyIds: Optional[Sequence[str]]
    PublicIpv4SubnetSize: Optional[float]
    RootPassword: Optional[str]
    SshKeyIds: Optional[Sequence[str]]
    State: Optional[str]
    Storage: Optional[str]
    Tags: Optional[Sequence[str]]
    Updated: Optional[str]
    UserData: Optional[str]
    WaitForReservationDeprovision: Optional[bool]
    IpAddress: Optional[Sequence["_IpAddress"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessPrivateIpv4=json_data.get("AccessPrivateIpv4"),
            AccessPublicIpv4=json_data.get("AccessPublicIpv4"),
            AccessPublicIpv6=json_data.get("AccessPublicIpv6"),
            AlwaysPxe=json_data.get("AlwaysPxe"),
            BillingCycle=json_data.get("BillingCycle"),
            Created=json_data.get("Created"),
            DeployedFacility=json_data.get("DeployedFacility"),
            Description=json_data.get("Description"),
            Facilities=json_data.get("Facilities"),
            Facility=json_data.get("Facility"),
            ForceDetachVolumes=json_data.get("ForceDetachVolumes"),
            HardwareReservationId=json_data.get("HardwareReservationId"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IpAddressTypes=json_data.get("IpAddressTypes"),
            IpxeScriptUrl=json_data.get("IpxeScriptUrl"),
            Locked=json_data.get("Locked"),
            Network=json_data.get("Network"),
            NetworkType=json_data.get("NetworkType"),
            OperatingSystem=json_data.get("OperatingSystem"),
            Plan=json_data.get("Plan"),
            Ports=json_data.get("Ports"),
            ProjectId=json_data.get("ProjectId"),
            ProjectSshKeyIds=json_data.get("ProjectSshKeyIds"),
            PublicIpv4SubnetSize=json_data.get("PublicIpv4SubnetSize"),
            RootPassword=json_data.get("RootPassword"),
            SshKeyIds=json_data.get("SshKeyIds"),
            State=json_data.get("State"),
            Storage=json_data.get("Storage"),
            Tags=json_data.get("Tags"),
            Updated=json_data.get("Updated"),
            UserData=json_data.get("UserData"),
            WaitForReservationDeprovision=json_data.get("WaitForReservationDeprovision"),
            IpAddress=json_data.get("IpAddress"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Network:
    Address: Optional[str]
    Cidr: Optional[float]
    Family: Optional[float]
    Gateway: Optional[str]
    Public: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Cidr=json_data.get("Cidr"),
            Family=json_data.get("Family"),
            Gateway=json_data.get("Gateway"),
            Public=json_data.get("Public"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


@dataclass
class Ports:
    Bonded: Optional[bool]
    Id: Optional[str]
    Mac: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ports"]:
        if not json_data:
            return None
        return cls(
            Bonded=json_data.get("Bonded"),
            Id=json_data.get("Id"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ports = Ports


@dataclass
class IpAddress:
    Cidr: Optional[float]
    ReservationIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddress"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            ReservationIds=json_data.get("ReservationIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddress = IpAddress


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


