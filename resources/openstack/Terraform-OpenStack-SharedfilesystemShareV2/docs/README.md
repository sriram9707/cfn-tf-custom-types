# Terraform::OpenStack::SharedfilesystemShareV2

CloudFormation equivalent of openstack_sharedfilesystem_share_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::SharedfilesystemShareV2",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ispublic" title="IsPublic">IsPublic</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#sharenetworkid" title="ShareNetworkId">ShareNetworkId</a>" : <i>String</i>,
        "<a href="#shareproto" title="ShareProto">ShareProto</a>" : <i>String</i>,
        "<a href="#sharetype" title="ShareType">ShareType</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshotid" title="SnapshotId">SnapshotId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::SharedfilesystemShareV2
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ispublic" title="IsPublic">IsPublic</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#sharenetworkid" title="ShareNetworkId">ShareNetworkId</a>: <i>String</i>
    <a href="#shareproto" title="ShareProto">ShareProto</a>: <i>String</i>
    <a href="#sharetype" title="ShareType">ShareType</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshotid" title="SnapshotId">SnapshotId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPublic

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareNetworkId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareProto

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllMetadata

Returns the <code>AllMetadata</code> value.

#### ExportLocations

Returns the <code>ExportLocations</code> value.

#### HasReplicas

Returns the <code>HasReplicas</code> value.

#### Host

Returns the <code>Host</code> value.

#### ProjectId

Returns the <code>ProjectId</code> value.

#### ReplicationType

Returns the <code>ReplicationType</code> value.

#### ShareServerId

Returns the <code>ShareServerId</code> value.
