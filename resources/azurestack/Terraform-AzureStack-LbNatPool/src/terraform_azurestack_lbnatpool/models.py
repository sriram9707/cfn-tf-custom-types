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
    BackendPort: Optional[float]
    FrontendIpConfigurationId: Optional[str]
    FrontendIpConfigurationName: Optional[str]
    FrontendPortEnd: Optional[float]
    FrontendPortStart: Optional[float]
    Id: Optional[str]
    LoadbalancerId: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ResourceGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackendPort=json_data.get("BackendPort"),
            FrontendIpConfigurationId=json_data.get("FrontendIpConfigurationId"),
            FrontendIpConfigurationName=json_data.get("FrontendIpConfigurationName"),
            FrontendPortEnd=json_data.get("FrontendPortEnd"),
            FrontendPortStart=json_data.get("FrontendPortStart"),
            Id=json_data.get("Id"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


