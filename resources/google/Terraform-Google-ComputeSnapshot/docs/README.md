# Terraform::Google::ComputeSnapshot

CloudFormation equivalent of google_compute_snapshot

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeSnapshot",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#sourcedisk" title="SourceDisk">SourceDisk</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#snapshotencryptionkey" title="SnapshotEncryptionKey">SnapshotEncryptionKey</a>" : <i>[ <a href="snapshotencryptionkey.md">SnapshotEncryptionKey</a>, ... ]</i>,
        "<a href="#sourcediskencryptionkey" title="SourceDiskEncryptionKey">SourceDiskEncryptionKey</a>" : <i>[ <a href="sourcediskencryptionkey.md">SourceDiskEncryptionKey</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeSnapshot
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#sourcedisk" title="SourceDisk">SourceDisk</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#snapshotencryptionkey" title="SnapshotEncryptionKey">SnapshotEncryptionKey</a>: <i>
      - <a href="snapshotencryptionkey.md">SnapshotEncryptionKey</a></i>
    <a href="#sourcediskencryptionkey" title="SourceDiskEncryptionKey">SourceDiskEncryptionKey</a>: <i>
      - <a href="sourcediskencryptionkey.md">SourceDiskEncryptionKey</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDisk

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotEncryptionKey

_Required_: No

_Type_: List of <a href="snapshotencryptionkey.md">SnapshotEncryptionKey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDiskEncryptionKey

_Required_: No

_Type_: List of <a href="sourcediskencryptionkey.md">SourceDiskEncryptionKey</a>

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

#### CreationTimestamp

Returns the <code>CreationTimestamp</code> value.

#### DiskSizeGb

Returns the <code>DiskSizeGb</code> value.

#### LabelFingerprint

Returns the <code>LabelFingerprint</code> value.

#### Licenses

Returns the <code>Licenses</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### SnapshotId

Returns the <code>SnapshotId</code> value.

#### SourceDiskLink

Returns the <code>SourceDiskLink</code> value.

#### StorageBytes

Returns the <code>StorageBytes</code> value.
