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
    AccountName: Optional[str]
    AccountPrivilege: Optional[str]
    DbClusterId: Optional[str]
    DbNames: Optional[Sequence[str]]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountName=json_data.get("AccountName"),
            AccountPrivilege=json_data.get("AccountPrivilege"),
            DbClusterId=json_data.get("DbClusterId"),
            DbNames=json_data.get("DbNames"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


