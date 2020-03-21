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
    Parallelism: Optional[float]
    Project: Optional[str]
    SecurityGroupId: Optional[str]
    Rule: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Parallelism=json_data.get("Parallelism"),
            Project=json_data.get("Project"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    CidrList: Optional[Sequence[str]]
    IcmpCode: Optional[float]
    IcmpType: Optional[float]
    Ports: Optional[Sequence[str]]
    Protocol: Optional[str]
    TrafficType: Optional[str]
    UserSecurityGroupList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            CidrList=json_data.get("CidrList"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Ports=json_data.get("Ports"),
            Protocol=json_data.get("Protocol"),
            TrafficType=json_data.get("TrafficType"),
            UserSecurityGroupList=json_data.get("UserSecurityGroupList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule

