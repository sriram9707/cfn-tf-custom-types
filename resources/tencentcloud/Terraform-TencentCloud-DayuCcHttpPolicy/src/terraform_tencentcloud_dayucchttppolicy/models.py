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
    Action: Optional[str]
    CreateTime: Optional[str]
    Frequency: Optional[float]
    Id: Optional[str]
    Ip: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    Smode: Optional[str]
    Switch: Optional[bool]
    RuleList: Optional[Sequence["_RuleList"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            CreateTime=json_data.get("CreateTime"),
            Frequency=json_data.get("Frequency"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            Smode=json_data.get("Smode"),
            Switch=json_data.get("Switch"),
            RuleList=json_data.get("RuleList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleList:
    Operator: Optional[str]
    Skey: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleList"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Skey=json_data.get("Skey"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleList = RuleList

