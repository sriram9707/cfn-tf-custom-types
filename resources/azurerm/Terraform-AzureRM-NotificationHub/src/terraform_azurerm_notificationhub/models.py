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
    Location: Optional[str]
    Name: Optional[str]
    NamespaceName: Optional[str]
    ResourceGroupName: Optional[str]
    ApnsCredential: Optional[Sequence["_ApnsCredential"]]
    GcmCredential: Optional[Sequence["_GcmCredential"]]
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
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NamespaceName=json_data.get("NamespaceName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ApnsCredential=json_data.get("ApnsCredential"),
            GcmCredential=json_data.get("GcmCredential"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApnsCredential:
    ApplicationMode: Optional[str]
    BundleId: Optional[str]
    KeyId: Optional[str]
    TeamId: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApnsCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApnsCredential"]:
        if not json_data:
            return None
        return cls(
            ApplicationMode=json_data.get("ApplicationMode"),
            BundleId=json_data.get("BundleId"),
            KeyId=json_data.get("KeyId"),
            TeamId=json_data.get("TeamId"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApnsCredential = ApnsCredential


@dataclass
class GcmCredential:
    ApiKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcmCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcmCredential"]:
        if not json_data:
            return None
        return cls(
            ApiKey=json_data.get("ApiKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcmCredential = GcmCredential


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

