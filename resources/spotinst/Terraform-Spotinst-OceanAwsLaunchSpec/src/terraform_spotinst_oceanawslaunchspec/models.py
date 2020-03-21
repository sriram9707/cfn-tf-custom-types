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
    IamInstanceProfile: Optional[str]
    ImageId: Optional[str]
    OceanId: Optional[str]
    RootVolumeSize: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    UserData: Optional[str]
    AutoscaleHeadrooms: Optional[Sequence["_AutoscaleHeadrooms"]]
    Labels: Optional[Sequence["_Labels"]]
    Taints: Optional[Sequence["_Taints"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            ImageId=json_data.get("ImageId"),
            OceanId=json_data.get("OceanId"),
            RootVolumeSize=json_data.get("RootVolumeSize"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetIds=json_data.get("SubnetIds"),
            UserData=json_data.get("UserData"),
            AutoscaleHeadrooms=json_data.get("AutoscaleHeadrooms"),
            Labels=json_data.get("Labels"),
            Taints=json_data.get("Taints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscaleHeadrooms:
    CpuPerUnit: Optional[float]
    GpuPerUnit: Optional[float]
    MemoryPerUnit: Optional[float]
    NumOfUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscaleHeadrooms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscaleHeadrooms"]:
        if not json_data:
            return None
        return cls(
            CpuPerUnit=json_data.get("CpuPerUnit"),
            GpuPerUnit=json_data.get("GpuPerUnit"),
            MemoryPerUnit=json_data.get("MemoryPerUnit"),
            NumOfUnits=json_data.get("NumOfUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscaleHeadrooms = AutoscaleHeadrooms


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Taints:
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Taints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Taints"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Taints = Taints

