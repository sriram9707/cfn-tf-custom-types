# Terraform::AWS::LightsailKeyPair

CloudFormation equivalent of aws_lightsail_key_pair

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LightsailKeyPair",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#publickey" title="PublicKey">PublicKey</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LightsailKeyPair
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#publickey" title="PublicKey">PublicKey</a>: <i>String</i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgpKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicKey

_Required_: No

_Type_: String

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

#### EncryptedFingerprint

Returns the <code>EncryptedFingerprint</code> value.

#### EncryptedPrivateKey

Returns the <code>EncryptedPrivateKey</code> value.

#### Fingerprint

Returns the <code>Fingerprint</code> value.

#### PrivateKey

Returns the <code>PrivateKey</code> value.
