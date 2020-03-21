# Terraform::Vault::AwsAuthBackendRoletagBlacklist

CloudFormation equivalent of vault_aws_auth_backend_roletag_blacklist

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::AwsAuthBackendRoletagBlacklist",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#disableperiodictidy" title="DisablePeriodicTidy">DisablePeriodicTidy</a>" : <i>Boolean</i>,
        "<a href="#safetybuffer" title="SafetyBuffer">SafetyBuffer</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::AwsAuthBackendRoletagBlacklist
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#disableperiodictidy" title="DisablePeriodicTidy">DisablePeriodicTidy</a>: <i>Boolean</i>
    <a href="#safetybuffer" title="SafetyBuffer">SafetyBuffer</a>: <i>Double</i>
</pre>

## Properties

#### Backend

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisablePeriodicTidy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafetyBuffer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
