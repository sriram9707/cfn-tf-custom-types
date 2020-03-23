# Terraform::AWS::StoragegatewayNfsFileShare

Manages an AWS Storage Gateway NFS File Share.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::StoragegatewayNfsFileShare",
    "Properties" : {
        "<a href="#clientlist" title="ClientList">ClientList</a>" : <i>[ String, ... ]</i>,
        "<a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>" : <i>String</i>,
        "<a href="#gatewayarn" title="GatewayArn">GatewayArn</a>" : <i>String</i>,
        "<a href="#guessmimetypeenabled" title="GuessMimeTypeEnabled">GuessMimeTypeEnabled</a>" : <i>Boolean</i>,
        "<a href="#kmsencrypted" title="KmsEncrypted">KmsEncrypted</a>" : <i>Boolean</i>,
        "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
        "<a href="#locationarn" title="LocationArn">LocationArn</a>" : <i>String</i>,
        "<a href="#objectacl" title="ObjectAcl">ObjectAcl</a>" : <i>String</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#requesterpays" title="RequesterPays">RequesterPays</a>" : <i>Boolean</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#squash" title="Squash">Squash</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#nfsfilesharedefaults" title="NfsFileShareDefaults">NfsFileShareDefaults</a>" : <i>[ <a href="nfsfilesharedefaults.md">NfsFileShareDefaults</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::StoragegatewayNfsFileShare
Properties:
    <a href="#clientlist" title="ClientList">ClientList</a>: <i>
      - String</i>
    <a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>: <i>String</i>
    <a href="#gatewayarn" title="GatewayArn">GatewayArn</a>: <i>String</i>
    <a href="#guessmimetypeenabled" title="GuessMimeTypeEnabled">GuessMimeTypeEnabled</a>: <i>Boolean</i>
    <a href="#kmsencrypted" title="KmsEncrypted">KmsEncrypted</a>: <i>Boolean</i>
    <a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
    <a href="#locationarn" title="LocationArn">LocationArn</a>: <i>String</i>
    <a href="#objectacl" title="ObjectAcl">ObjectAcl</a>: <i>String</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#requesterpays" title="RequesterPays">RequesterPays</a>: <i>Boolean</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#squash" title="Squash">Squash</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#nfsfilesharedefaults" title="NfsFileShareDefaults">NfsFileShareDefaults</a>: <i>
      - <a href="nfsfilesharedefaults.md">NfsFileShareDefaults</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ClientList

The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultStorageClass

The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayArn

Amazon Resource Name (ARN) of the file gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuessMimeTypeEnabled

Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncrypted

Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationArn

The ARN of the backed storage used for storing file data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectAcl

Access Control List permission for S3 bucket objects. Defaults to `private`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequesterPays

Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Squash

Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsFileShareDefaults

_Required_: No

_Type_: List of <a href="nfsfilesharedefaults.md">NfsFileShareDefaults</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### FileshareId

Returns the <code>FileshareId</code> value.

#### Id

Returns the <code>Id</code> value.
