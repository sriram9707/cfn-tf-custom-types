# Terraform::Panos::BgpPeerGroup

CloudFormation equivalent of panos_bgp_peer_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::BgpPeerGroup",
    "Properties" : {
        "<a href="#aggregatedconfedaspath" title="AggregatedConfedAsPath">AggregatedConfedAsPath</a>" : <i>Boolean</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#exportnexthop" title="ExportNextHop">ExportNextHop</a>" : <i>String</i>,
        "<a href="#importnexthop" title="ImportNextHop">ImportNextHop</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>" : <i>Boolean</i>,
        "<a href="#softresetwithstoredinfo" title="SoftResetWithStoredInfo">SoftResetWithStoredInfo</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::BgpPeerGroup
Properties:
    <a href="#aggregatedconfedaspath" title="AggregatedConfedAsPath">AggregatedConfedAsPath</a>: <i>Boolean</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#exportnexthop" title="ExportNextHop">ExportNextHop</a>: <i>String</i>
    <a href="#importnexthop" title="ImportNextHop">ImportNextHop</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#removeprivateas" title="RemovePrivateAs">RemovePrivateAs</a>: <i>Boolean</i>
    <a href="#softresetwithstoredinfo" title="SoftResetWithStoredInfo">SoftResetWithStoredInfo</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AggregatedConfedAsPath

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportNextHop

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportNextHop

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemovePrivateAs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftResetWithStoredInfo

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualRouter

_Required_: Yes

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
