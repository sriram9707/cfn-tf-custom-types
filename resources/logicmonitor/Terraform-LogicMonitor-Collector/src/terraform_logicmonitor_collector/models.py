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
    BackupCollectorId: Optional[float]
    CollectorGroupId: Optional[float]
    Description: Optional[str]
    EnableCollectorDeviceFailover: Optional[bool]
    EnableFailback: Optional[bool]
    EscalationChainId: Optional[float]
    Id: Optional[str]
    Properties: Optional[Sequence["_Properties"]]
    ResendInterval: Optional[float]
    SuppressAlertClear: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackupCollectorId=json_data.get("BackupCollectorId"),
            CollectorGroupId=json_data.get("CollectorGroupId"),
            Description=json_data.get("Description"),
            EnableCollectorDeviceFailover=json_data.get("EnableCollectorDeviceFailover"),
            EnableFailback=json_data.get("EnableFailback"),
            EscalationChainId=json_data.get("EscalationChainId"),
            Id=json_data.get("Id"),
            Properties=json_data.get("Properties"),
            ResendInterval=json_data.get("ResendInterval"),
            SuppressAlertClear=json_data.get("SuppressAlertClear"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Properties:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


