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
    CompartmentId: Optional[str]
    DisplayName: Optional[str]
    EulaLink: Optional[str]
    Id: Optional[str]
    ListingId: Optional[str]
    ListingResourceId: Optional[str]
    ListingResourceVersion: Optional[str]
    OracleTermsOfUseLink: Optional[str]
    PublisherName: Optional[str]
    Signature: Optional[str]
    Summary: Optional[str]
    TimeCreated: Optional[str]
    TimeRetrieved: Optional[str]
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
            CompartmentId=json_data.get("CompartmentId"),
            DisplayName=json_data.get("DisplayName"),
            EulaLink=json_data.get("EulaLink"),
            Id=json_data.get("Id"),
            ListingId=json_data.get("ListingId"),
            ListingResourceId=json_data.get("ListingResourceId"),
            ListingResourceVersion=json_data.get("ListingResourceVersion"),
            OracleTermsOfUseLink=json_data.get("OracleTermsOfUseLink"),
            PublisherName=json_data.get("PublisherName"),
            Signature=json_data.get("Signature"),
            Summary=json_data.get("Summary"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeRetrieved=json_data.get("TimeRetrieved"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


