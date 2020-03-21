# Terraform::Panos::Bgp

CloudFormation equivalent of panos_bgp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::Bgp",
    "Properties" : {
        "<a href="#aggregatemed" title="AggregateMed">AggregateMed</a>" : <i>Boolean</i>,
        "<a href="#allowredistributedefaultroute" title="AllowRedistributeDefaultRoute">AllowRedistributeDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#alwayscomparemed" title="AlwaysCompareMed">AlwaysCompareMed</a>" : <i>Boolean</i>,
        "<a href="#asformat" title="AsFormat">AsFormat</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#bfdprofile" title="BfdProfile">BfdProfile</a>" : <i>String</i>,
        "<a href="#confederationmemberas" title="ConfederationMemberAs">ConfederationMemberAs</a>" : <i>String</i>,
        "<a href="#defaultlocalpreference" title="DefaultLocalPreference">DefaultLocalPreference</a>" : <i>String</i>,
        "<a href="#deterministicmedcomparison" title="DeterministicMedComparison">DeterministicMedComparison</a>" : <i>Boolean</i>,
        "<a href="#ecmpmultias" title="EcmpMultiAs">EcmpMultiAs</a>" : <i>Boolean</i>,
        "<a href="#enable" title="Enable">Enable</a>" : <i>Boolean</i>,
        "<a href="#enablegracefulrestart" title="EnableGracefulRestart">EnableGracefulRestart</a>" : <i>Boolean</i>,
        "<a href="#enforcefirstas" title="EnforceFirstAs">EnforceFirstAs</a>" : <i>Boolean</i>,
        "<a href="#installroute" title="InstallRoute">InstallRoute</a>" : <i>Boolean</i>,
        "<a href="#localrestarttime" title="LocalRestartTime">LocalRestartTime</a>" : <i>Double</i>,
        "<a href="#maxpeerrestarttime" title="MaxPeerRestartTime">MaxPeerRestartTime</a>" : <i>Double</i>,
        "<a href="#reflectorclusterid" title="ReflectorClusterId">ReflectorClusterId</a>" : <i>String</i>,
        "<a href="#rejectdefaultroute" title="RejectDefaultRoute">RejectDefaultRoute</a>" : <i>Boolean</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#staleroutetime" title="StaleRouteTime">StaleRouteTime</a>" : <i>Double</i>,
        "<a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::Bgp
Properties:
    <a href="#aggregatemed" title="AggregateMed">AggregateMed</a>: <i>Boolean</i>
    <a href="#allowredistributedefaultroute" title="AllowRedistributeDefaultRoute">AllowRedistributeDefaultRoute</a>: <i>Boolean</i>
    <a href="#alwayscomparemed" title="AlwaysCompareMed">AlwaysCompareMed</a>: <i>Boolean</i>
    <a href="#asformat" title="AsFormat">AsFormat</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#bfdprofile" title="BfdProfile">BfdProfile</a>: <i>String</i>
    <a href="#confederationmemberas" title="ConfederationMemberAs">ConfederationMemberAs</a>: <i>String</i>
    <a href="#defaultlocalpreference" title="DefaultLocalPreference">DefaultLocalPreference</a>: <i>String</i>
    <a href="#deterministicmedcomparison" title="DeterministicMedComparison">DeterministicMedComparison</a>: <i>Boolean</i>
    <a href="#ecmpmultias" title="EcmpMultiAs">EcmpMultiAs</a>: <i>Boolean</i>
    <a href="#enable" title="Enable">Enable</a>: <i>Boolean</i>
    <a href="#enablegracefulrestart" title="EnableGracefulRestart">EnableGracefulRestart</a>: <i>Boolean</i>
    <a href="#enforcefirstas" title="EnforceFirstAs">EnforceFirstAs</a>: <i>Boolean</i>
    <a href="#installroute" title="InstallRoute">InstallRoute</a>: <i>Boolean</i>
    <a href="#localrestarttime" title="LocalRestartTime">LocalRestartTime</a>: <i>Double</i>
    <a href="#maxpeerrestarttime" title="MaxPeerRestartTime">MaxPeerRestartTime</a>: <i>Double</i>
    <a href="#reflectorclusterid" title="ReflectorClusterId">ReflectorClusterId</a>: <i>String</i>
    <a href="#rejectdefaultroute" title="RejectDefaultRoute">RejectDefaultRoute</a>: <i>Boolean</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#staleroutetime" title="StaleRouteTime">StaleRouteTime</a>: <i>Double</i>
    <a href="#virtualrouter" title="VirtualRouter">VirtualRouter</a>: <i>String</i>
</pre>

## Properties

#### AggregateMed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRedistributeDefaultRoute

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysCompareMed

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsFormat

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BfdProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfederationMemberAs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultLocalPreference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeterministicMedComparison

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcmpMultiAs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableGracefulRestart

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceFirstAs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallRoute

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalRestartTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPeerRestartTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReflectorClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectDefaultRoute

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaleRouteTime

_Required_: No

_Type_: Double

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
