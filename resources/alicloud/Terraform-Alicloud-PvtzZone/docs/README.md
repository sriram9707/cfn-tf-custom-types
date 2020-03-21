# Terraform::Alicloud::PvtzZone

CloudFormation equivalent of alicloud_pvtz_zone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::PvtzZone",
    "Properties" : {
        "<a href="#lang" title="Lang">Lang</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#proxypattern" title="ProxyPattern">ProxyPattern</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#userclientip" title="UserClientIp">UserClientIp</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::PvtzZone
Properties:
    <a href="#lang" title="Lang">Lang</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#proxypattern" title="ProxyPattern">ProxyPattern</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#userclientip" title="UserClientIp">UserClientIp</a>: <i>String</i>
</pre>

## Properties

#### Lang

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserClientIp

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

#### CreationTime

Returns the <code>CreationTime</code> value.

#### IsPtr

Returns the <code>IsPtr</code> value.

#### RecordCount

Returns the <code>RecordCount</code> value.

#### UpdateTime

Returns the <code>UpdateTime</code> value.
