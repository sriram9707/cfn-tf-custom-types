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
    AutoUpgradeMinorVersion: Optional[bool]
    ForceUpdateTag: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ProtectedSettings: Optional[str]
    ProvisionAfterExtensions: Optional[Sequence[str]]
    Publisher: Optional[str]
    Settings: Optional[str]
    Type: Optional[str]
    TypeHandlerVersion: Optional[str]
    VirtualMachineScaleSetId: Optional[str]
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
            AutoUpgradeMinorVersion=json_data.get("AutoUpgradeMinorVersion"),
            ForceUpdateTag=json_data.get("ForceUpdateTag"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ProtectedSettings=json_data.get("ProtectedSettings"),
            ProvisionAfterExtensions=json_data.get("ProvisionAfterExtensions"),
            Publisher=json_data.get("Publisher"),
            Settings=json_data.get("Settings"),
            Type=json_data.get("Type"),
            TypeHandlerVersion=json_data.get("TypeHandlerVersion"),
            VirtualMachineScaleSetId=json_data.get("VirtualMachineScaleSetId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


